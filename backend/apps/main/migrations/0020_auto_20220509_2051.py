# Generated by Django 3.0.5 on 2022-05-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220509_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]