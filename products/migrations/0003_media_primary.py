# Generated by Django 5.0.7 on 2024-08-16 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
