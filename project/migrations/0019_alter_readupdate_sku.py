# Generated by Django 3.2.9 on 2021-12-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_rename_sku_readupdate_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readupdate',
            name='sku',
            field=models.CharField(max_length=750, null=True, unique=True),
        ),
    ]
