# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-05 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'Prakash Rai', max_length=20)),
                ('interests', models.CharField(max_length=100)),
                ('profile', models.TextField(max_length=500)),
                ('blog_description', models.TextField(default=b'Mathematics and Computer Science Blog', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]
