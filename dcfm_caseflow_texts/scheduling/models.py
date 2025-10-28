# Original path: scheduling/models.py


from django.db import models

class Judge(models.Model):
    name = models.CharField(max_length=128)
    specializations = models.JSONField(default=list, blank=True)  # e.g., ["CIVIL","WRIT"]
    active = models.BooleanField(default=True)
    def __str__(self): return self.name

class Bench(models.Model):
    name = models.CharField(max_length=64, unique=True)
    judges = models.ManyToManyField(Judge, related_name='benches')
    courtroom = models.CharField(max_length=32, blank=True)
    capacity_per_day = models.PositiveIntegerField(default=30)
    specialization_tags = models.JSONField(default=list, blank=True)
    def __str__(self): return self.name

class TimeStandard(models.Model):
    case_type = models.CharField(max_length=16)
    category = models.CharField(max_length=16)
    first_listing_days = models.PositiveIntegerField(default=30)
    disposal_days = models.PositiveIntegerField(default=365)
    def __str__(self): return f"{self.case_type}/{self.category}"

class ScheduleSlot(models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity_units = models.PositiveIntegerField(default=1)
    allocated_case = models.ForeignKey('cases.Case', null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        unique_together = ('bench','date','start_time','end_time')
    def __str__(self): return f"{self.bench} {self.date} {self.start_time}-{self.end_time}"
