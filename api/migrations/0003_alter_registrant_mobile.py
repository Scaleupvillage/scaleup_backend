# Generated by Django 5.2.1 on 2025-05-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_registrant_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='mobile',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
