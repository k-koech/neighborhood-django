# Generated by Django 3.2.7 on 2021-09-27 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210927_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.neighborhood'),
        ),
    ]
