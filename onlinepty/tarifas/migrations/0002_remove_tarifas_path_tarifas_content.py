# Generated by Django 5.0.3 on 2024-04-14 04:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarifas',
            name='path',
        ),
        migrations.AddField(
            model_name='tarifas',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
