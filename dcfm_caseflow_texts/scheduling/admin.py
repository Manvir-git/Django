# Original path: scheduling/admin.py


from django.contrib import admin
from .models import Judge, Bench, TimeStandard, ScheduleSlot
admin.site.register([Judge, Bench, TimeStandard, ScheduleSlot])
