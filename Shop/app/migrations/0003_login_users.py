# Generated by Django 4.2.10 on 2024-06-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_users',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
            ],
        ),
    ]
