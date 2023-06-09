# Generated by Django 4.2 on 2023-04-12 09:39

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='demo_password',
            field=users.models.CustomPasswordField(max_length=255, verbose_name='demo password'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='live_password',
            field=users.models.CustomPasswordField(max_length=255, verbose_name='live password'),
        ),
    ]
