# Generated by Django 4.0.4 on 2022-05-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_rename_owned_book_physically_owned_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(default=None, to='Books.author'),
        ),
    ]