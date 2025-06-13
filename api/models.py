from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
import random

class Registration(models.Model):
    unique_id = models.CharField(max_length=5, unique=True, blank=True, null=True)  # new un ique 5-digit ID

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{7,15}$',
            )
        ]
    )
    
    country_code = models.CharField(
       max_length=5,
        validators=[
            RegexValidator(
                regex=r'^\+\d{1,4}$',
                message="Country code must be in format '+XXX' (e.g., +971)"
            )
        ]
    )
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=50)

    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "api_registration"

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        while True:
            unique_id = f"{random.randint(10000, 99999)}"  # Generate 5-digit number as string
            if not Registration.objects.filter(unique_id=unique_id).exists():
                return unique_id
