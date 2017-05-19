# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
import datetime

class CommonInfo(models.Model):
    name = models.CharField(max_length=128,default='')
    name_pinyin = models.CharField(max_length=128, null=True, blank=True, default=None)

    desc = models.TextField(null=True, blank=True, default='')

    class Meta:
        abstract = True
        ordering = ['name_pinyin']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
class Profile_Team(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

class TechType(models.Model):
    TECH_TYPE = ((u'1',u'企业'),(u'2',u'个人'),(u'3',u'团体'))
    name = models.CharField(max_length=8,choices=TECH_TYPE,default=u'1')

class Profile(models.Model):
    CHANNEL = (('1',u'男'),('2',u'女'))
    username = models.CharField(max_length=128,default='')
    login_at = models.DateTimeField(auto_now=True)
    logout_at = models.DateTimeField(auto_now=True)
    age = models.SmallIntegerField(null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=64, choices = CHANNEL, default = '1')
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_team = models.ManyToManyField(Profile_Team,blank=True,related_name='profile')
    ttype = models.OneToOneField(TechType,related_name='ttype')

    def __unicode__(self):
        return (self.username+"  --"+self.gender)
    def format_time(self):
        aftertime = datetime.datetime.strftime(self.login_at,'%Y-%m-%d %H:%M:%S')
        return aftertime











