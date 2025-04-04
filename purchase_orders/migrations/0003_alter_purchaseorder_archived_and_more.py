# Generated by Django 5.1.6 on 2025-03-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_purchaseorder_completed_alter_purchaseorder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='archived',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='completed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaseorderitem',
            name='archived',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
