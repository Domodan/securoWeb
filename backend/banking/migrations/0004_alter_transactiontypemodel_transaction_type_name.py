# Generated by Django 3.2 on 2023-04-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_transactionsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiontypemodel',
            name='transaction_type_name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
