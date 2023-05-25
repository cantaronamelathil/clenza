# Generated by Django 4.1.5 on 2023-05-18 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0017_rename_appointment_dispatchbooking_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchbooking',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Booking.appointment'),
        ),
    ]