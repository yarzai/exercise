# Generated by Django 4.1 on 2022-10-02 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price']},
        ),
    ]
