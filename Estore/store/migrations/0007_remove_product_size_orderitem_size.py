# Generated by Django 4.0.6 on 2022-08-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], default='s', max_length=5),
        ),
    ]
