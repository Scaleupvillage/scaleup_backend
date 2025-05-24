from django.db import models
from django.core.validators import RegexValidator

class Registrant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10)

    mobile_validator = RegexValidator(
        regex=r'^\d{12}$',
        message="Mobile number must be exactly 10 digits."
    )
    mobile = models.CharField(max_length=10, unique=True, validators=[mobile_validator])

    company = models.CharField(max_length=200)
    profession = models.CharField(max_length=200, default='Others')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
