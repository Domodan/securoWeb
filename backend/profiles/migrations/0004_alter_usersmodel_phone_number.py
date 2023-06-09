# Generated by Django 3.2 on 2023-04-07 15:44

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_usersmodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
