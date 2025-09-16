from django.contrib import admin
from .models import HabitModel, ProgressModel

@admin.register(ProgressModel)
class ProgressModelAdmin(admin.ModelAdmin):
    list_display= ('habit_id', 'date')

admin.site.register(HabitModel)


