# Generated by Django 4.1.5 on 2023-03-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_alter_dispatchbooking_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='cloth_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]