# Generated by Django 2.1.3 on 2018-12-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipeac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]