# Generated by Django 3.0.10 on 2022-05-18 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
