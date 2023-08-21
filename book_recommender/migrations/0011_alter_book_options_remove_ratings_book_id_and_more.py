# Generated by Django 4.2.3 on 2023-08-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_recommender', '0010_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='book_id',
        ),
        migrations.AddField(
            model_name='ratings',
            name='ISBN',
            field=models.CharField(blank=True, db_column='ISBN', max_length=25, null=True),
        ),
    ]