# Generated by Django 4.0.4 on 2022-05-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0008_alter_author_age_alter_author_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=None, max_length=150, unique=True),
        ),
    ]
