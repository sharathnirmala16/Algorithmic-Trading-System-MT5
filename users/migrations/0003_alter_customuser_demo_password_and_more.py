# Generated by Django 4.2 on 2023-04-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_demo_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='demo_password',
            field=models.CharField(max_length=255, verbose_name='demo password'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='live_password',
            field=models.CharField(max_length=255, verbose_name='live password'),
        ),
    ]
