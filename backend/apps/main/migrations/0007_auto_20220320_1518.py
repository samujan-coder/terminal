# Generated by Django 3.0.5 on 2022-03-20 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220320_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='chase_bot',
            new_name='twap_bot',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='chase_bot_completed_trades',
            new_name='twap_bot_completed_trades',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='chase_bot_duration',
            new_name='twap_bot_duration',
        ),
    ]
