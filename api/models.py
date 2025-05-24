from django.db import models

class Registrant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Make email unique
    mobile = models.CharField(max_length=15, unique=True)  # Make mobile unique
    country_code = models.CharField(max_length=5)
    company = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
