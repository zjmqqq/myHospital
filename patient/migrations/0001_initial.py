# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-13 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('cId', models.AutoField(primary_key=True, serialize=False, verbose_name='评论ID')),
                ('content', models.CharField(max_length=200, verbose_name='评论内容')),
                ('cTime', models.DateTimeField(verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='contreteTime_a',
            fields=[
                ('ctId', models.AutoField(primary_key=True, serialize=False)),
                ('a_8_00', models.BooleanField(default=True, verbose_name='8:00')),
                ('a_8_30', models.BooleanField(default=True, verbose_name='8:30')),
                ('a_9_00', models.BooleanField(default=True, verbose_name='9:00')),
                ('a_9_30', models.BooleanField(default=True, verbose_name='9:30')),
                ('a_10_00', models.BooleanField(default=True, verbose_name='10:00')),
                ('a_10_30', models.BooleanField(default=True, verbose_name='10:30')),
                ('a_11_00', models.BooleanField(default=True, verbose_name='11:00')),
                ('a_11_30', models.BooleanField(default=True, verbose_name='11:30')),
            ],
        ),
        migrations.CreateModel(
            name='contreteTime_p',
            fields=[
                ('ctId', models.AutoField(primary_key=True, serialize=False)),
                ('p_13_30', models.BooleanField(default=True, verbose_name='13:30')),
                ('p_14_00', models.BooleanField(default=True, verbose_name='14:00')),
                ('p_14_30', models.BooleanField(default=True, verbose_name='14:30')),
                ('p_15_00', models.BooleanField(default=True, verbose_name='15:00')),
                ('p_15_30', models.BooleanField(default=True, verbose_name='15:30')),
                ('p_16_00', models.BooleanField(default=True, verbose_name='16:00')),
                ('p_16_30', models.BooleanField(default=True, verbose_name='16:30')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False, verbose_name='部门ID')),
                ('departmentName', models.CharField(max_length=200, verbose_name='部门名字')),
                ('icon', models.CharField(default='fa fa-hospital-o', max_length=200, verbose_name='图片')),
                ('introduce', models.CharField(default='', max_length=200, verbose_name='部门介绍')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('dId', models.AutoField(primary_key=True, serialize=False, verbose_name='医生ID')),
                ('dName', models.CharField(max_length=200, verbose_name='医生姓名')),
                ('dPassword', models.CharField(max_length=200, verbose_name='医生密码')),
                ('dGender', models.CharField(max_length=200, verbose_name='医生性别')),
                ('dIdcard', models.CharField(max_length=200, verbose_name='医生身份证号')),
                ('dBirthday', models.CharField(max_length=200, verbose_name='医生生日')),
                ('dTel', models.CharField(max_length=200, unique=True, verbose_name='医生手机号码')),
                ('dIntroduce', models.CharField(max_length=200, verbose_name='医生介绍')),
                ('dSpecial', models.CharField(max_length=200, verbose_name='医生特长')),
                ('charge', models.IntegerField(default=12, verbose_name='挂号费用')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.department', verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('nId', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=1000)),
                ('publishTime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('pId', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('pName', models.CharField(max_length=200, verbose_name='用户姓名')),
                ('pPassword', models.CharField(max_length=200, verbose_name='用户密码')),
                ('pIdCard', models.CharField(max_length=200, verbose_name='用户身份证号')),
                ('pTel', models.CharField(max_length=200, unique=True, verbose_name='用户手机号码')),
                ('balance', models.IntegerField(default=0, verbose_name='余额')),
                ('pEmail', models.EmailField(default='', max_length=254, verbose_name='邮箱号')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('rId', models.AutoField(primary_key=True, serialize=False, verbose_name='预约ID')),
                ('subTime', models.DateTimeField(verbose_name='提交时间')),
                ('regTime', models.DateField(verbose_name='预约时间')),
                ('ap', models.BooleanField(default=True, verbose_name='上午/下午')),
                ('regState', models.BooleanField(default=True, verbose_name='预约状态')),
                ('visitState', models.BooleanField(default=False, verbose_name='就诊状态')),
                ('evaluateState', models.BooleanField(default=False, verbose_name='是否评论')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.department', verbose_name='部门名称')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.doctor', verbose_name='医生姓名')),
                ('evaluate', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.comment', verbose_name='评论')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patients', verbose_name='病人名字')),
            ],
        ),
        migrations.CreateModel(
            name='registrationType',
            fields=[
                ('tId', models.AutoField(primary_key=True, serialize=False, verbose_name='')),
                ('type', models.CharField(max_length=20, verbose_name='医生类型')),
            ],
        ),
        migrations.CreateModel(
            name='scheduling',
            fields=[
                ('sId', models.AutoField(primary_key=True, serialize=False, verbose_name='排班ID')),
                ('sTime', models.DateField(verbose_name='排班日期')),
                ('remainNumber', models.IntegerField(verbose_name='剩余号码')),
                ('ap', models.BooleanField(default=True, verbose_name='上午/下午')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.doctor', verbose_name='医生名字')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.registrationType', verbose_name='医生类型'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='registrationType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.registrationType', verbose_name='是否专家'),
        ),
        migrations.AddField(
            model_name='contretetime_p',
            name='scheduling_p',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.scheduling', verbose_name='排班ID'),
        ),
        migrations.AddField(
            model_name='contretetime_a',
            name='scheduling_a',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.scheduling', verbose_name='排班ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.doctor', verbose_name='医生名称'),
        ),
        migrations.AddField(
            model_name='comment',
            name='patients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patients', verbose_name='用户名称'),
        ),
    ]
