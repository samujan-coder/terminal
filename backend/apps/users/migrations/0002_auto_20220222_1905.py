# Generated by Django 3.0.5 on 2022-02-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='api_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='secret_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]