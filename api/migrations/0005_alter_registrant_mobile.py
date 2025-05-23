# Generated by Django 5.2.1 on 2025-05-24 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_registrant_profession_alter_registrant_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='mobile',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{12}$')]),
        ),
    ]
