# Generated by Django 4.1.9 on 2023-05-24 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='senha1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='senha2',
        ),
    ]
