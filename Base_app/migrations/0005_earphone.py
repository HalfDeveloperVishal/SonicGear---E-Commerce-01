# Generated by Django 5.1.7 on 2025-04-06 16:06

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_app', '0004_alter_cartitem_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earphone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Earphone',
                'verbose_name_plural': 'Earphones',
                'ordering': ['-created_at'],
            },
        ),
    ]
