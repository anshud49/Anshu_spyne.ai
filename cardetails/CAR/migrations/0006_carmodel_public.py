# Generated by Django 5.1.3 on 2024-11-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0005_alter_carmodel_car_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
