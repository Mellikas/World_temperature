from django.contrib import admin
from .models import Temperature


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('region', 'country', 'city', 'year', 'month_name', 'avg_temp_C')
    list_filter = ('country', 'year')
    search_fields = ['country', 'year', 'month', 'region']


admin.site.register(Temperature, TemperatureAdmin)
