# Generated by Django 4.0.4 on 2022-05-01 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0006_remove_author_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Books.field'),
        ),
    ]
