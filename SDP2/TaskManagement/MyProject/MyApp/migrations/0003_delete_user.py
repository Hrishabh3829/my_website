# Generated by Django 4.2.8 on 2024-03-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
