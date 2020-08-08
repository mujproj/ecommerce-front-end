# Generated by Django 2.2.11 on 2020-04-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='emailID',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
