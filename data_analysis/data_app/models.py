from django.db import models


class Temperature(models.Model):
    region = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    month_name = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    avg_temp_F = models.FloatField(null=True, blank=True)
    avg_temp_C = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.country} {self.city} " \
               f"{self.year} {self.month_name}" \
               f"(temp.): {self.avg_temp_C}"
