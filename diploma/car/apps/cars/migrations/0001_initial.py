# Generated by Django 4.0.4 on 2022-05-22 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('-category',),
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_name', models.CharField(max_length=40, verbose_name='марка')),
            ],
            options={
                'verbose_name': 'марка',
                'verbose_name_plural': 'марки',
                'ordering': ('-mark_name',),
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('model', models.CharField(max_length=20, verbose_name='модель машины')),
                ('speed', models.IntegerField(verbose_name='скорость машины')),
                ('motor', models.CharField(choices=[('modified', 'Модифицированный'), ('non_modified', 'Не модифицированный')], max_length=40, verbose_name='состояние мотора')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.category', verbose_name='категория')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.mark', verbose_name='марка машины')),
            ],
            options={
                'verbose_name': 'машина',
                'verbose_name_plural': 'машины',
                'ordering': ('-mark',),
            },
        ),
    ]
