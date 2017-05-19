from __future__ import unicode_literals

from django.db import models
class SmsMessage(models.Model):

	MTYPE = (('0',u'qq'), ('1',u'aa'), ('2',u'ss'), ('3',u'ee'), ('4',u'mm'))
	message_type = models.CharField(max_length=4, choices = MTYPE, default = '1')
	mobile = models.CharField(unique=True, max_length=32, default='', null=True, blank=True)
	message_text = models.CharField(max_length=2046, null=True, blank=True, default=None)
	need_notice = models.BooleanField(default=False)

# class Student(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     YEAR_IN_SCHOOL_CHOICES = (
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#     )
#     year_in_school = models.CharField(max_length=2,
#                                       choices=YEAR_IN_SCHOOL_CHOICES,
#                                       default=FRESHMAN)
#
#     def is_upperclass(self):
#         return self.year_in_school in (self.JUNIOR, self.SENIOR)


