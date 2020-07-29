# Generated by Django 3.0.8 on 2020-07-28 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=100, null=True)),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('expires_at', models.DateTimeField()),
                ('expires_in', models.DateTimeField()),
                ('token_type', models.CharField(max_length=100)),
                ('refresh_token', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OAuth Tokens',
            },
        ),
    ]
