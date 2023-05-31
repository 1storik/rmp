# Generated by Django 4.2.1 on 2023-05-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeatingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_heating', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
