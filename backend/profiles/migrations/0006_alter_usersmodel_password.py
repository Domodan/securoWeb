# Generated by Django 3.2 on 2023-04-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_usersmodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
