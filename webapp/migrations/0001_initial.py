# Generated by Django 4.2.4 on 2023-09-04 05:29

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.quarter')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('subtext', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(default='thumbnails/himnic.png', upload_to='thumbnails/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('quarter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.quarter')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.topic')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('subtext', models.CharField(max_length=255)),
                ('volume', models.IntegerField()),
                ('issue', models.IntegerField()),
                ('thumbnail', models.ImageField(default='thumbnails/himnic.png', upload_to='thumbnails/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('quarter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.quarter')),
            ],
        ),
    ]
