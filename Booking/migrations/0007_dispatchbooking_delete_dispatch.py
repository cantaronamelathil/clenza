# Generated by Django 4.1.5 on 2023-03-13 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Booking', '0006_dispatch_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatchBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatchdate', models.DateField()),
                ('slot', models.IntegerField(choices=[(0, '09:00 - 09:30 AM'), (1, '10:00 - 10:30 AM'), (2, '11:00 - 11:30 AM'), (3, '12:00 - 12:30 PM'), (4, '01:00 - 01:30 PM'), (5, '14:00 - 14:30 PM'), (6, '15:00 - 15:30 PM'), (7, '16:00 - 16:30 PM'), (8, '17:00 - 17:30 PM')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Dispatch',
        ),
    ]
