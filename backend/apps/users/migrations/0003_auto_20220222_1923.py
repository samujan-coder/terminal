# Generated by Django 3.0.5 on 2022-02-22 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220222_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='invitation',
        ),
        migrations.RemoveField(
            model_name='user',
            name='invitation_token',
        ),
    ]