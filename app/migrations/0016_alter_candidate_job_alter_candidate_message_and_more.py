# Generated by Django 4.1.2 on 2022-10-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_about_about_candidate_about_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.CharField(max_length=5, verbose_name='Job code'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='message',
            field=models.TextField(verbose_name='Presentation'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('', 'Select personality'), ('I am outgoing', ' I am outgoing'), ('I am social', 'I am social'), ('I am antisocial', 'I am antisocial'), ('I am discreet', 'I am discreet'), ('I am serious', 'I am serious')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='salary',
            field=models.CharField(max_length=50, verbose_name='Salary expectation'),
        ),
    ]