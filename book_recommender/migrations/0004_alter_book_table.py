# Generated by Django 4.2.3 on 2023-07-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='public.books',
        ),
    ]