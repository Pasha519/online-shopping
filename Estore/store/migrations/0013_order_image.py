# Generated by Django 4.0.6 on 2022-08-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_order_city_alter_order_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, upload_to='picture/'),
        ),
    ]
