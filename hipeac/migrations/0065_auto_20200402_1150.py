# Generated by Django 3.0.5 on 2020-04-02 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hipeac", "0064_auto_20200402_1146"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="phdmobility",
            options={
                "ordering": ["-start_date"],
                "verbose_name": "PhD mobility",
                "verbose_name_plural": "PhD mobilities",
            },
        ),
    ]
