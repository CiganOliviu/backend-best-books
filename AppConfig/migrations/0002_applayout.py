# Generated by Django 3.2.7 on 2022-04-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConfig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
