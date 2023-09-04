# Generated by Django 4.2.4 on 2023-09-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_auto_20190630_1408"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("HC", "Health Care"),
                    ("VS", "Vitamins & Supplements"),
                    ("DG", "Devices & Diagnostics"),
                ],
                max_length=2,
            ),
        ),
    ]
