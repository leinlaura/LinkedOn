# Generated by Django 2.2.17 on 2021-03-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkedOnApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
