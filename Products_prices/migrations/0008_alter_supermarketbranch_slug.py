# Generated by Django 4.0.5 on 2022-06-26 12:21

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('Products_prices', '0007_brand_slug_catagory_slug_supermarket_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supermarketbranch',
            name='slug',
            field=models.SlugField(default=uuid.uuid1,null=True, blank=True),
        ),
    ]
