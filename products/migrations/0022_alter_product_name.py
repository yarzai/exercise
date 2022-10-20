# Generated by Django 4.1 on 2022-10-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(error_messages={'blank': 'Please enter a value.', 'unique': 'Please enter a unique name.'}, help_text='Name should be unique.', max_length=150),
        ),
    ]
