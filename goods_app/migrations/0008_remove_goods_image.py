# Generated by Django 2.2.6 on 2019-11-06 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods_app', '0007_auto_20191105_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='image',
        ),
    ]