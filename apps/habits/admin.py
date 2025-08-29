from django.contrib import admin
from .models import HabitModel, ProgressModel

admin.site.register(HabitModel)
admin.site.register(ProgressModel)

