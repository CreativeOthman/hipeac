# Generated by Django 2.1.7 on 2019-03-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipeac', '0027_auto_20190313_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='techtransferapplication',
            name='team_string',
            field=models.TextField(blank=True, null=True, verbose_name='Team (text)'),
        ),
    ]