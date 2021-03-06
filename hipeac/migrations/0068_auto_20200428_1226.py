# Generated by Django 3.0.5 on 2020-04-28 10:26

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("hipeac", "0067_auto_20200428_1224"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="is_virtual",
            field=models.BooleanField(default=False, help_text="Is it a virtual event?"),
        ),
        migrations.AlterField(
            model_name="event",
            name="city",
            field=models.CharField(blank=True, help_text="Empty for virtual events", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="country",
            field=django_countries.fields.CountryField(
                blank=True, db_index=True, help_text="Empty for virtual events", max_length=2, null=True
            ),
        ),
    ]
