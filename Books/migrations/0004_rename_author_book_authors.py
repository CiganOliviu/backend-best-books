# Generated by Django 4.0.4 on 2022-05-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_remove_book_author_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
