# Generated by Django 5.0 on 2023-12-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_ticket_price_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='post_index',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=6),
        ),
    ]
