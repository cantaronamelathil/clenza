# Generated by Django 4.1.5 on 2023-03-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useracount', '0007_alter_accounts_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'Customer'), ('VENDOR', 'Vendor'), ('WORKER', 'worker')], max_length=50),
        ),
    ]
