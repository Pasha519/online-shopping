# Generated by Django 4.0.6 on 2022-08-18 17:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_order_email_remove_order_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
