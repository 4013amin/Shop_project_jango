# Generated by Django 4.2.10 on 2024-07-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]