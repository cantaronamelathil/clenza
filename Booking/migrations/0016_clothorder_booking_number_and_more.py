# Generated by Django 4.1.5 on 2023-05-17 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0015_appointment_booking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothorder',
            name='booking_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dispatchbooking',
            name='Appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.appointment'),
        ),
    ]
