# Generated by Django 5.0.6 on 2024-05-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ethanai_register", "0003_alter_financial_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="financial",
            name="cost_price",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="financial",
            name="market_price",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="financial",
            name="quantity",
            field=models.IntegerField(null=True),
        ),
    ]