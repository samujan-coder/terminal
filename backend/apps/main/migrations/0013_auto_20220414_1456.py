# Generated by Django 3.0.5 on 2022-04-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220412_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='hft_bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trade',
            name='hft_default_price_difference',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='trade',
            name='hft_order_ids',
            field=models.TextField(default='[]'),
        ),
        migrations.AddField(
            model_name='trade',
            name='hft_orders_on_each_side',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trade',
            name='hft_orders_price_difference',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
    ]
