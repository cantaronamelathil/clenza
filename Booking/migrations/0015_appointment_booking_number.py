# Generated by Django 4.1.5 on 2023-04-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0014_alter_dispatchbooking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='booking_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]