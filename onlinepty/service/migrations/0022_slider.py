# Generated by Django 5.0.3 on 2024-04-10 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_service_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services', verbose_name='imagen')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='services', verbose_name='imagen1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='services', verbose_name='imagen2')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
    ]