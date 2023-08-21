# Generated by Django 4.2.3 on 2023-08-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0007_alter_book_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='Username', max_length=255)),
                ('ISBN', models.CharField(db_column='ISBN', max_length=25)),
                ('rating', models.IntegerField(db_column='Rating')),
            ],
        ),
    ]
