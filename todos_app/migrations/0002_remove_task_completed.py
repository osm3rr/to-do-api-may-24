# Generated by Django 5.0.6 on 2024-05-08 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
