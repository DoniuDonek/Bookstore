# Generated by Django 4.0.8 on 2023-07-20 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_languages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]
