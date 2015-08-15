# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(related_name='book_add', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_edited_by', models.ForeignKey(related_name='book_edit', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
