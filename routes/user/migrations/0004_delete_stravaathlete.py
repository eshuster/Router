# Generated by Django 3.0.6 on 2020-07-04 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OAuth', '0006_delete_stravaaccount'),
        ('user', '0003_auto_20200606_0752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StravaAthlete',
        ),
    ]