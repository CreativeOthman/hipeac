# Generated by Django 2.2.6 on 2020-02-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hipeac", "0059_openregistration_city"),
    ]

    operations = [
        migrations.RemoveField(model_name="openregistration", name="bool_q1",),
        migrations.RemoveField(model_name="openregistration", name="bool_q2",),
        migrations.RemoveField(model_name="openregistration", name="bool_q3",),
        migrations.RemoveField(model_name="openregistration", name="bool_q4",),
        migrations.RemoveField(model_name="openregistration", name="open_q1",),
        migrations.RemoveField(model_name="openregistration", name="open_q2",),
        migrations.RemoveField(model_name="openregistration", name="open_q3",),
        migrations.RemoveField(model_name="openregistration", name="open_q4",),
        migrations.AddField(model_name="openregistration", name="fields", field=models.TextField(default="{}"),),
    ]
