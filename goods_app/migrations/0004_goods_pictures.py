# Generated by Django 2.2.5 on 2019-10-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_app', '0003_goods_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='pictures',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
