# Generated by Django 3.0.6 on 2020-05-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='num_books',
            field=models.IntegerField(default=0),
        ),
    ]
