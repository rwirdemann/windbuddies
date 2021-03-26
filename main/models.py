from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone


class Session(models.Model):
    when = models.DateField('when', default=django.utils.timezone.now)
    spot = models.CharField(max_length=100)
    planned = models.IntegerField(default=0)
    riders = models.ManyToManyField(User)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.DO_NOTHING)

    def spot_image(self):
        return '/static/main/' + self.spot.replace(' ', '').lower() + '.png'

    def rider_names(self):
        names = map(lambda r: r.username, self.riders.all())
        return ', '.join(names)

    def __str__(self):
        return '%s: %s Riders: %d' % (self.when.strftime("%d.%m.%Y"),
                                      self.spot, self.riders.count())
