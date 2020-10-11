# Generated by Django 3.1.1 on 2020-09-21 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activitydate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='note',
            name='notedate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
