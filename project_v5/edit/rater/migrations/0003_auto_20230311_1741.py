# Generated by Django 2.2.5 on 2023-03-11 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_auto_20230311_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='googleplaceid',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.RemoveField(
            model_name='book',
            name='phoneno',
        ),
    ]
