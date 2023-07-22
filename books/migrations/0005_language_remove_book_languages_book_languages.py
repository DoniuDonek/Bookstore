# Generated by Django 4.0.8 on 2023-07-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options_book_formats_book_languages_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='languages',
        ),
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(blank=True, to='books.language'),
        ),
    ]
