# Generated by Django 4.2.10 on 2024-05-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number1', models.CharField(max_length=30)),
                ('number2', models.CharField(max_length=30)),
            ],
        ),
    ]
