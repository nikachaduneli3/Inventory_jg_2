# Generated by Django 5.1.6 on 2025-03-29 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_item_stock_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stock_qty',
        ),
    ]
