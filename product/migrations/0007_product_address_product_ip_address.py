# Generated by Django 5.0 on 2023-12-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_productvideo_product_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
