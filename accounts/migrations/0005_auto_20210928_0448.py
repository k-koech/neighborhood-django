# Generated by Django 3.2.7 on 2021-09-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210928_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='police',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
