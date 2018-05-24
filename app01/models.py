# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)
    fileName = models.CharField(verbose_name='文件名', max_length=100, blank=False)
    submit_time = models.DateTimeField(verbose_name='上传时间')
    uploadByFile = models.BooleanField(verbose_name="是否通过文件上传>?", default=True)
    RESULT_CHOICES = ((1, '未处理'), (2, '正在处理'), (3, '已处理'),)
    result = models.IntegerField(verbose_name='处理结果', choices=RESULT_CHOICES, default=1)
    def __str__(self):
        return self.fileName

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, blank=False)
    SEX_CHOICES = ((1, '男'), (2, '女'),)
    sex = models.IntegerField(verbose_name='性别', choices=SEX_CHOICES, null=True)
    tel = models.CharField(verbose_name='手机', max_length=20, blank=False, null=True)
    debt = models.IntegerField(verbose_name="欠款", blank=False)
    deadline = models.DateTimeField(verbose_name="截止日期")
    delay = models.IntegerField(verbose_name="期限")
    inFile = models.ForeignKey("File")
    RESULT_CHOICES = ((1, '未处理'), (2, '正在处理'), (3, '已处理'),)
    result = models.IntegerField(verbose_name='处理结果', choices=RESULT_CHOICES, default=1)
    importdate = models.DateTimeField(verbose_name='导入时间')
    def __str__(self):
        return self.name

class version(models.Model):
    version =  models.CharField(verbose_name="版本号", max_length = 20)
    def __str__(self):
        return self.version



