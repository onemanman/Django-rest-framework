# Generated by Django 4.0.6 on 2022-08-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_attribute_deviceattribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
