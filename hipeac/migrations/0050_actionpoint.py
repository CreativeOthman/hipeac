# Generated by Django 2.2.7 on 2019-11-28 13:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hipeac', '0049_auto_20191127_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NO', 'Discarded'), ('UN', 'Not started'), ('IN', 'In progress'), ('OK', 'Completed'), ('FI', 'Finalized')], default='UN', max_length=2)),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('progress', models.TextField(blank=True, null=True, verbose_name='Progress description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owners', models.ManyToManyField(related_name='action_points', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
