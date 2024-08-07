from django.db import models


class AircraftManager(models.Manager):
    def active_aircrafts(self):
        return self.filter(modified__isnull=False)
    

class Aircraft(models.Model):
    user_id = models.IntegerField()
    guid = models.UUIDField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    modified = models.DateTimeField()

    objects = AircraftManager()


    class Meta:
        unique_together = ('guid', 'reference')

    def __str__(self):
        return f"{self.make} {self.model} ({self.reference})"