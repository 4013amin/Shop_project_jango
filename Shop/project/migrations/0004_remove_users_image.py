# Generated by Django 4.2.10 on 2024-07-28 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_users_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
    ]
