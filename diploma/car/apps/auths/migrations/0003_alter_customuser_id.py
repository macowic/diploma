# Generated by Django 4.0.4 on 2022-05-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_alter_customuser_datetime_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
