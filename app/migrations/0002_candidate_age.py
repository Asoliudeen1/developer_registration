# Generated by Django 4.1.2 on 2022-10-05 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='age',
            field=models.CharField(default=datetime.datetime(2022, 10, 5, 1, 48, 40, 56038, tzinfo=datetime.timezone.utc), max_length=3),
            preserve_default=False,
        ),
    ]
