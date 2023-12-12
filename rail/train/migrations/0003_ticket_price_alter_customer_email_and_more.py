# Generated by Django 5.0 on 2023-12-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_customer_rename_station_id_route_station_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='post_index',
            field=models.DecimalField(decimal_places=0, max_digits=6, null=True),
        ),
    ]
