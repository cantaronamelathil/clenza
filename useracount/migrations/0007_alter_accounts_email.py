# Generated by Django 4.1.5 on 2023-03-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useracount', '0006_alter_accounts_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(blank=True, db_column='email', max_length=100, null=True, unique=True),
        ),
    ]