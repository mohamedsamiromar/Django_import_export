# Generated by Django 3.2.9 on 2021-12-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20211216_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readupdate',
            name='attachment_links',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='readupdate',
            name='image_links',
            field=models.CharField(max_length=3072, null=True),
        ),
        migrations.AlterField(
            model_name='readupdate',
            name='sku',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
