# Generated by Django 4.0.6 on 2022-08-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
