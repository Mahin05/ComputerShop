# Generated by Django 3.2.7 on 2021-09-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerShop', '0002_auto_20210913_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='computer_pic'),
        ),
    ]