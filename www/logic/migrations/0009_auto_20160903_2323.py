# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0008_auto_20160831_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mergemsg',
            old_name='conversation_id',
            new_name='zg_user_id',
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='be_interested_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='bl_user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='last_words',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='qlm_have_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='qlm_user_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='recommend_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mergemsg',
            name='zg_have_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='district',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='province',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='mergemsg',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='recommend_id',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.RemoveField(
            model_name='mergemsg',
            name='from_user_id',
        ),
        migrations.RemoveField(
            model_name='mergemsg',
            name='msg_type',
        ),
        migrations.RemoveField(
            model_name='mergemsg',
            name='payload',
        ),
        migrations.RemoveField(
            model_name='mergemsg',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='mergemsg',
            name='words',
        ),
        migrations.AlterIndexTogether(
            name='mergemsg',
            index_together=set([('zg_user_id', 'qlm_user_id', 'be_interested_id')]),
        ),
    ]
