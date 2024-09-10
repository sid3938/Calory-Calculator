# Generated by Django 5.0.3 on 2024-09-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('serving_size', models.CharField(max_length=50)),
                ('calories', models.CharField(max_length=50)),
                ('carbohydrate', models.CharField(max_length=50)),
                ('cholesterol', models.CharField(max_length=50)),
                ('total_fat', models.CharField(max_length=50)),
                ('saturated_fat', models.CharField(max_length=50)),
                ('fiber', models.CharField(max_length=50)),
                ('protein', models.CharField(max_length=50)),
                ('sodium', models.CharField(max_length=50)),
                ('sugars', models.CharField(max_length=50)),
            ],
        ),
    ]
