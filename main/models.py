from django.contrib.auth.models import User
from django.db import models
from django.contrib.staticfiles import finders
import django.utils.timezone


class Spot(models.Model):
    name = models.CharField(max_length=100, unique=True)
    windfinder_id = models.CharField(max_length=100, default="")
    x = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    y = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def x_str(self):
        return str(self.x).replace(',', '.')

    def y_str(self):
        return str(self.y).replace(',', '.')

    def __str__(self):
        return self.name


class Session(models.Model):
    when = models.DateField('when', default=django.utils.timezone.now)
    planned = models.IntegerField(default=0)
    riders = models.ManyToManyField(User)
    owner = models.ForeignKey(User,
                              related_name='owner',
                              on_delete=models.DO_NOTHING)
    spot = models.ForeignKey(Spot, on_delete=models.DO_NOTHING)

    def spot_image(self):
        img = 'main/' + self.spot.name.replace(' ', '').lower() + '.png'
        if finders.find(img) is not None:
            return '/static/' + img
        return '/static/main/default.png'

    def rider_names(self):
        names = map(lambda r: r.username, self.riders.all())
        return ', '.join(names)

    def __str__(self):
        return '%s: %s Riders: %d' % (self.when.strftime("%d.%m.%Y"),
                                      self.spot.name, self.riders.count())
