# Generated by Django 3.2 on 2021-05-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_emailotpauthenticationsystem_expire_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailotpauthenticationsystem',
            name='Expire_Time',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
