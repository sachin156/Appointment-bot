# Generated by Django 2.2.3 on 2019-09-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_remove_slots_slot_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='slot_day',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
