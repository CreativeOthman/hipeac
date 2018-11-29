# Generated by Django 2.1.3 on 2018-11-29 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hipeac', '0002_auto_20181129_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_type',
            field=models.ForeignKey(limit_choices_to={'type': 'session_type'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session_type', to='hipeac.Metadata'),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.ForeignKey(limit_choices_to={'type': 'employment_type'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employment_type', to='hipeac.Metadata'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='type',
            field=models.CharField(choices=[('gender', 'Gender'), ('title', 'Title'), ('meal_preference', 'Meal preference'), ('job_position', 'Position'), ('employment_type', 'Employment type'), ('application_area', 'Application area'), ('session_type', 'Session type'), ('topic', 'Topic')], max_length=32),
        ),
    ]
