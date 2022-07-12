# Generated by Django 4.0.5 on 2022-07-12 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products_prices', '0022_alter_item_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='User Email')),
                ('phone_no', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Phone Number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products_prices.consumer'),
        ),
        migrations.DeleteModel(
            name='Cunsomer',
        ),
    ]