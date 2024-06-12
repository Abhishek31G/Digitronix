# Generated by Django 5.0.6 on 2024-05-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0016_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
