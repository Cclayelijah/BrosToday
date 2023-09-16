from django.contrib import admin
from .models import Workout
from .models import WorkoutType
from .models import BenchmarkTest

# Register your models here.
admin.site.register(Workout)
admin.site.register(WorkoutType)
admin.site.register(BenchmarkTest)