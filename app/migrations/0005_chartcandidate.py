# Generated by Django 4.1.2 on 2023-02-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_email', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('chat', models.CharField(max_length=500)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
