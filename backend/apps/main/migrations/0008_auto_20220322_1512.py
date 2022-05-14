# Generated by Django 3.0.5 on 2022-03-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220320_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='iceberg_prices_sum',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='trade',
            name='take_profit',
            field=models.BooleanField(default=False),
        ),
    ]
