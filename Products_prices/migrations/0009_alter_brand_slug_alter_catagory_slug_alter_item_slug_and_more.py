# Generated by Django 4.0.5 on 2022-06-26 16:02

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('Products_prices', '0008_alter_supermarketbranch_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='supermarketbranch',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True, blank=True),
        ),
    ]
