# Generated by Django 4.0.5 on 2022-06-26 12:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_prices', '0005_remove_product_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='None<django.db.models.fields.related.ForeignKey>',),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='supermarketbranch',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
    ]
