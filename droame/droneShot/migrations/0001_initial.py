# Generated by Django 4.1.7 on 2023-03-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DroneShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_name', models.CharField(max_length=100)),
                ('drone_type', models.CharField(max_length=100)),
            ],
        ),
    ]
