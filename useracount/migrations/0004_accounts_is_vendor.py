# Generated by Django 4.1.5 on 2023-02-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useracount', '0003_remove_accounts_is_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
    ]