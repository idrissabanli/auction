# Generated by Django 2.2.5 on 2019-10-01 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
        ('goods_app', '0002_goods_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category_app.Category'),
        ),
    ]
