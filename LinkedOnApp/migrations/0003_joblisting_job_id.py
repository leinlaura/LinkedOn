# Generated by Django 2.2.17 on 2021-03-31 21:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LinkedOnApp', '0002_remove_joblisting_job_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='job_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
