# Generated by Django 4.1.2 on 2022-11-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_restaurants_delete_random_delete_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
