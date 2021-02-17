# Generated by Django 3.1.2 on 2021-02-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulatorApp', '0011_auto_20210210_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceeffects',
            name='high_sales',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=12),
        ),
        migrations.AlterField(
            model_name='priceeffects',
            name='low_sales',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=12),
        ),
        migrations.AlterField(
            model_name='priceeffects',
            name='med_sales',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=12),
        ),
    ]
