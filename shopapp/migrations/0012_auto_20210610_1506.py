# Generated by Django 3.0.5 on 2021-06-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0011_auto_20210610_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
