# Generated by Django 4.2.3 on 2023-07-28 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0006_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
    ]
