# Generated by Django 3.2.25 on 2024-05-25 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0032_sonline'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='usuario_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_us', to=settings.AUTH_USER_MODEL),
        ),
    ]
