# Generated by Django 5.2.1 on 2025-05-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_registration_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='unique_id',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
    ]
