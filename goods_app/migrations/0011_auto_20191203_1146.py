# Generated by Django 2.2.6 on 2019-12-03 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0010_myuser_budget'),
        ('goods_app', '0010_auto_20191109_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Some',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_field', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='offer_person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='user_app.MyUser'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]