# Generated by Django 3.0.6 on 2020-05-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200520_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
