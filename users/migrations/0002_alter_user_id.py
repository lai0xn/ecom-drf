# Generated by Django 5.0.7 on 2024-07-28 16:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a78ba2ea-1384-4b84-b4ba-7d6351daf9d4'), editable=False, primary_key=True, serialize=False),
        ),
    ]
