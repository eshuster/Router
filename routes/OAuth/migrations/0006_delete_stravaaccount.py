# Generated by Django 3.0.6 on 2020-07-04 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OAuth', '0005_auto_20200701_1807'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StravaAccount',
        ),
    ]