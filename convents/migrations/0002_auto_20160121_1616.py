# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 16:16
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('actors', '0003_auto_20160121_1608'),
        ('convents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.PositiveSmallIntegerField(choices=[('1\u201310', 1), ('11\u201330', 2), ('31\u2013100', 3), ('101\u20131000', 4), ('> 1000', 5)])),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, size=None)),
                ('awards', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('link', models.URLField(blank=True, null=True)),
                ('is_bid', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(to='tags.Genre')),
                ('participants', models.ManyToManyField(to='actors.Participant')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConventionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='convents.Convention')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'convents_convention_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='conventiontradition',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 21, 16, 16, 32, 344586, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conventiontradition',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 21, 16, 16, 34, 973172, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convention',
            name='traditions',
            field=models.ManyToManyField(to='convents.ConventionTradition'),
        ),
        migrations.AlterUniqueTogether(
            name='conventiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
