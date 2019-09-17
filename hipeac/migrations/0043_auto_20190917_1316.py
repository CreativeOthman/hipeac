# Generated by Django 2.2.5 on 2019-09-17 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hipeac', '0042_auto_20190912_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=32, verbose_name='category')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('value', models.TextField(verbose_name='value')),
                ('deadline', models.DateTimeField(null=True, verbose_name='deadline')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['category', 'user', 'object_id'], name='hipeac_noti_categor_ffe850_idx'),
        ),
    ]
