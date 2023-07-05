# Generated by Django 4.1.7 on 2023-06-23 15:04

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_user_cellphone_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='complement',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='cpfCnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='user',
            name='foreignerDocument',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Default', 'Default')], default='Default', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='user_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='postalCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=255),
        ),
    ]