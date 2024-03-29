# Generated by Django 4.1.5 on 2023-02-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='end_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='slot',
            field=models.IntegerField(choices=[(0, '09:00 – 09:30 AM'), (1, '10:00 – 10:30 AM'), (2, '11:00 – 11:30 AM'), (3, '12:00 – 12:30 PM'), (4, '01:00 – 01:30 PM'), (5, '14:00 – 14:30 PM'), (6, '15:00 – 15:30 PM'), (7, '16:00 – 16:30 PM'), (8, '17:00 – 17:30 PM')]),
        ),
    ]
