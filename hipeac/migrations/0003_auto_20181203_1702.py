# Generated by Django 2.1.3 on 2018-12-03 16:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hipeac", "0002_auto_20181203_1217"),
    ]

    operations = [
        migrations.AddField(
            model_name="magazine",
            name="application_areas",
            field=models.CharField(
                blank=True,
                max_length=250,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="magazine",
            name="projects",
            field=models.ManyToManyField(blank=True, related_name="magazines", to="hipeac.Project"),
        ),
        migrations.AddField(
            model_name="magazine",
            name="topics",
            field=models.CharField(
                blank=True,
                max_length=250,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z"),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="magazine",
            name="users",
            field=models.ManyToManyField(blank=True, related_name="magazines", to=settings.AUTH_USER_MODEL),
        ),
    ]
