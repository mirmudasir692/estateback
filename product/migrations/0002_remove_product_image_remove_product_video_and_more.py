# Generated by Django 5.0 on 2023-12-19 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.discount'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(db_default=models.Value(0.0), decimal_places=5, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='total_area',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product'),
        ),
        migrations.AddField(
            model_name='productvideo',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='product.product'),
        ),
    ]
