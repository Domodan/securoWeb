# Generated by Django 3.2 on 2023-03-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionTypeModel',
            fields=[
                ('transaction_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type_name', models.CharField(max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Transaction Types',
            },
        ),
    ]
