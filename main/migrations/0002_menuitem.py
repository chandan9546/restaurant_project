# Generated by Django 5.1.3 on 2025-05-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('starter', 'Starter'), ('main', 'Main Course'), ('dessert', 'Dessert'), ('drink', 'Drink')], max_length=50)),
                ('image', models.ImageField(upload_to='menu_images/')),
            ],
        ),
    ]
