# Generated by Django 5.0.7 on 2024-08-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('second_contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('wilaya', models.CharField(max_length=100)),
                ('delivered', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('delivered', 'delivered'), ('pending', 'pending'), ('confirmed', 'confirmed'), ('shipping', 'shipping'), ('canceled', 'canceled'), ('ordered', 'ordered')], default='pending', max_length=10)),
                ('shipping', models.CharField(choices=[('home', 'home'), ('stop desk', 'stop desk')], max_length=30)),
                ('custom_text', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('custom_text', models.TextField(null=True)),
            ],
        ),
    ]
