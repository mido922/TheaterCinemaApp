# Generated by Django 4.1.4 on 2023-01-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_rename_endtime_newshow_endtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newshow',
            name='remainingSeats',
            field=models.IntegerField(default=0),
        ),
    ]