from django.db import models
import django.utils.timezone

class Session(models.Model):
    when = models.DateField('when', default=django.utils.timezone.now)
    spot = models.CharField(max_length=100)
    planned = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s Riders: %d' % (self.when.strftime("%d.%m.%Y"), self.spot, self.planned)