# Generated by Django 4.0.6 on 2022-08-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_orderitem_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
