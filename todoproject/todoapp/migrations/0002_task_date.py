# Generated by Django 4.2 on 2023-04-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1991-02-08'),
            preserve_default=False,
        ),
    ]
