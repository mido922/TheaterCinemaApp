# Generated by Django 4.1.4 on 2023-01-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=100)),
                ('seatNumber', models.IntegerField(verbose_name='default = 0')),
                ('reservee', models.CharField(default='untitled', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='newshow',
            name='date',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AlterField(
            model_name='newshow',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
