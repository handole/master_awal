# Generated by Django 2.1.3 on 2018-11-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akun',
            name='tahun',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='giat',
            name='tahun',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='tahun',
            field=models.DateField(null=True),
        ),
    ]
