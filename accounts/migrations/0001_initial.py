# Generated by Django 3.2.7 on 2021-09-26 02:01

import cloudinary.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('id_number', models.IntegerField()),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('profile_photo', cloudinary.models.CloudinaryField(default='image/upload/v1631717620/default_uomrne.jpg', max_length=255, verbose_name='image')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(default=datetime.datetime.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('password_reset', models.CharField(default='e5viu3snjorndvd', max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('occupants_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('business_email', models.CharField(max_length=200)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.neighborhood'),
        ),
    ]