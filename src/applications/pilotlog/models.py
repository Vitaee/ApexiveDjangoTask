# Django Stuff
from django.db import models


class AircraftManager(models.Manager):
    def high_performance(self):
        return self.filter(high_performance=True)

    def complex_aircraft(self):
        return self.filter(complex=True)

    def pressurized_aircraft(self):
        return self.filter(pressurized=True)
    

class Aircraft(models.Model):
    guid = models.UUIDField(unique=True)
    user_id = models.IntegerField()
    make = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100, blank=True)
    reference = models.CharField(max_length=100, blank=True)
    modified = models.DateTimeField()
    equipment_type = models.CharField(max_length=100, blank=True)
    type_code = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=4, blank=True)
    category = models.CharField(max_length=100, blank=True)
    aircraft_class = models.CharField(max_length=100, blank=True)
    gear_type = models.CharField(max_length=100, blank=True)
    engine_type = models.CharField(max_length=100, blank=True)
    complex = models.BooleanField(default=False)
    high_performance = models.BooleanField(default=False)
    pressurized = models.BooleanField(default=False)
    taa = models.BooleanField(default=False)

    objects = AircraftManager() 

    def __str__(self):
        return f"{self.make} {self.model} ({self.reference})"

    class Meta:
        ordering = ['make', 'model']
        verbose_name_plural = "aircraft"

class Flight(models.Model):
    guid = models.UUIDField(unique=True)
    user_id = models.IntegerField()
    aircraft = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, null=True, blank=True
    )
    date_utc = models.DateField()
    date_base = models.DateField()
    date_local = models.DateField()
    remarks = models.TextField(blank=True)
    modified = models.DateTimeField()
    from_airport = models.CharField(max_length=100, blank=True)
    to_airport = models.CharField(max_length=100, blank=True)
    route = models.TextField(blank=True)
    time_out = models.TimeField(null=True, blank=True)
    time_off = models.TimeField(null=True, blank=True)
    time_on = models.TimeField(null=True, blank=True)
    time_in = models.TimeField(null=True, blank=True)
    on_duty = models.TimeField(null=True, blank=True)
    off_duty = models.TimeField(null=True, blank=True)
    total_time = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    pic = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sic = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    night = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    solo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cross_country = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    nvg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nvg_ops = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    day_takeoffs = models.IntegerField(null=True, blank=True)
    day_landings_full_stop = models.IntegerField(null=True, blank=True)
    night_takeoffs = models.IntegerField(null=True, blank=True)
    night_landings_full_stop = models.IntegerField(null=True, blank=True)
    all_landings = models.IntegerField(null=True, blank=True)
    actual_instrument = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    simulated_instrument = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    hobbs_start = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    hobbs_end = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    tach_start = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    tach_end = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    holds = models.IntegerField(null=True, blank=True)
    approach1 = models.CharField(max_length=100, blank=True)
    approach2 = models.CharField(max_length=100, blank=True)
    approach3 = models.CharField(max_length=100, blank=True)
    approach4 = models.CharField(max_length=100, blank=True)
    approach5 = models.CharField(max_length=100, blank=True)
    approach6 = models.CharField(max_length=100, blank=True)
    dual_given = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    dual_received = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    simulated_flight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    ground_training = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    instructor_name = models.CharField(max_length=100, blank=True)
    instructor_comments = models.TextField(blank=True)
    person1 = models.CharField(max_length=100, blank=True)
    person2 = models.CharField(max_length=100, blank=True)
    person3 = models.CharField(max_length=100, blank=True)
    person4 = models.CharField(max_length=100, blank=True)
    person5 = models.CharField(max_length=100, blank=True)
    person6 = models.CharField(max_length=100, blank=True)
    flight_review = models.BooleanField(default=False)
    checkride = models.BooleanField(default=False)
    ipc = models.BooleanField(default=False)
    nvg_proficiency = models.BooleanField(default=False)
    faa6158 = models.BooleanField(default=False)
    custom_text = models.TextField(blank=True)
    custom_numeric = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    custom_hours = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    custom_counter = models.IntegerField(null=True, blank=True)
    custom_date = models.DateField(null=True, blank=True)
    custom_datetime = models.DateTimeField(null=True, blank=True)
    custom_toggle = models.BooleanField(default=False)
    pilot_comments = models.TextField(blank=True)

    def __str__(self):
        return f"Flight on {self.date_utc} ({self.remarks})"
