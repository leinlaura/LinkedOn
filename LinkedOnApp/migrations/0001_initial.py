# Generated by Django 2.2.17 on 2021-03-31 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(blank=True, max_length=128)),
                ('company', models.CharField(blank=True, max_length=128)),
                ('about', models.CharField(blank=True, max_length=1000)),
                ('searchingInfo', models.CharField(blank=True, max_length=1000)),
                ('profileImage', models.ImageField(blank=True, upload_to='profile_images')),
                ('isEmployer', models.BooleanField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LinkedOnApp.Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='LinkedOnApp.Category')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LinkedOnApp.UserProfile')),
            ],
        ),
    ]
