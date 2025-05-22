from django.db import models

class Registrant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
