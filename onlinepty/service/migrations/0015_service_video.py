# Generated by Django 5.0.3 on 2024-04-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_remove_service_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Video'),
        ),
    ]