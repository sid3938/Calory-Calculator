# Generated by Django 5.0.3 on 2024-09-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Counter', '0002_alter_fooditem_calories_alter_fooditem_carbohydrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='serving_size',
            field=models.CharField(max_length=50),
        ),
    ]
