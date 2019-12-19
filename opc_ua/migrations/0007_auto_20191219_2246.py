# Generated by Django 2.2.7 on 2019-12-19 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opc_ua', '0006_auto_20191204_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagebit',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='messageevent',
            name='event_dt',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 19, 46, 7, 747070, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetag',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='messagetag',
            name='url',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tag',
            name='url',
            field=models.CharField(max_length=120),
        ),
    ]
