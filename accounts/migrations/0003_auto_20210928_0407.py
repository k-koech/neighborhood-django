# Generated by Django 3.2.7 on 2021-09-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_neighborhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='police',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
