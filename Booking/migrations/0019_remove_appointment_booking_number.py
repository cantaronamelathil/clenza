# Generated by Django 4.1.5 on 2023-05-19 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0018_alter_dispatchbooking_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='booking_number',
        ),
    ]