# Generated by Django 4.0.5 on 2022-06-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products_prices', '0003_remove_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products_prices.supermarketbranch'),
        ),
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='Products_prices.product'),
        ),
        migrations.AlterField(
            model_name='supermarketbranch',
            name='city',
            field=models.CharField(blank=True, help_text='set the City name', max_length=50, null=True, unique=True),
        ),
    ]
