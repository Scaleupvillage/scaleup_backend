# Generated by Django 5.2.1 on 2025-05-27 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_registration_submitted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{7,15}$')]),
        ),
    ]
