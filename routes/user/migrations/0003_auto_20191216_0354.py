# Generated by Django 3.0 on 2019-12-16 03:54

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191216_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.IntegerField(choices=[(1, 'ADMIN'), (2, 'USER')], default=user.models.Profile.ProfileTypes['USER']),
        ),
    ]