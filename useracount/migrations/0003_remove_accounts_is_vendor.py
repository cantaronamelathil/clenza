# Generated by Django 4.1.5 on 2023-02-07 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useracount', '0002_alter_accounts_first_name_alter_accounts_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='is_vendor',
        ),
    ]