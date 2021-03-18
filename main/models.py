from django.db import models
import django.utils.timezone


class Rider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Session(models.Model):
    when = models.DateField('when', default=django.utils.timezone.now)
    spot = models.CharField(max_length=100)
    planned = models.IntegerField(default=0)
    riders = models.ManyToManyField(Rider)

    def spot_image(self):
        return '/static/main/' + self.spot.replace(' ', '').lower() + '.png'

    def __str__(self):
        return '%s: %s Riders: %d' % (self.when.strftime("%d.%m.%Y"),
                                      self.spot, self.riders.count())
