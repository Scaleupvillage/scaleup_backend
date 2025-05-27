from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{7,15}$',
                # message="Mobile number must be exactly 10 digits."
            )
        ]
    )
    country_code = models.CharField(
        max_length=5,
        default='+971',
        validators=[
            RegexValidator(
                regex=r'^\+\d{1,4}$',
                message="Country code must be in format '+XXX' (e.g., +971)"
            )
        ]
    )
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=50)

    # New field to store the timestamp sent from frontend
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "api_registration"
