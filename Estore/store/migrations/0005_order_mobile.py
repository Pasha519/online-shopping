# Generated by Django 4.0.6 on 2022-08-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]