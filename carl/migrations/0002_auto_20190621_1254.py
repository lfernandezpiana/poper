# Generated by Django 2.2.2 on 2019-06-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='participantes',
            field=models.ManyToManyField(to='carl.Comediante'),
        ),
    ]