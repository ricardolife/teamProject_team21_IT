# Generated by Django 2.2.5 on 2023-03-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='restaurant',
            new_name='book',
        ),
    ]
