# Generated by Django 5.0.3 on 2024-04-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0028_rename_logo_category_path_category_path1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='path',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Path1'),
        ),
        migrations.AlterField(
            model_name='category',
            name='path1',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Path2'),
        ),
    ]
