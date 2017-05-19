# _*_ coding:utf-8 _*_
from django.contrib import admin
from account.models import *
from django.conf.urls import url
from django.http import HttpResponse
import xlwt
import os
import pdb
import datetime

def write_excel():
    # pdb.set_trace()
    # os.remove('d:\demo.xls')
    workbook = xlwt.Workbook(encoding='utf-8')
    data_sheet = workbook.add_sheet('demo')
    row0 = ['username','login_at']
    # row1 = ['de','dd','dd','dd','dd','dd']
    profiles = Profile.objects.all()
    length = len(profiles)
    column = []
    # for i in range(len(row0)):
    #     data_sheet.write(0,i,row0[i])
    #     data_sheet.write(1,i,row1[i])
    for i in range(length):
        login_time = datetime.datetime.strftime(profiles[i].login_at,"%Y-%m-%d %H:%M:%S")
        column = [profiles[i].username,login_time]
        for j in range(len(row0)):
            if i == 0:
                data_sheet.write(0,j,row0[j])

            data_sheet.write(i+1,j,column[j])
        column = []
    # for i in range(length):
    #     for j in range(len(row0)):
    #         data_sheet.write(0,j,row0[j],set_style('Times New Roman',220,True))
            # data_sheet.write(i+1,j,profiles[j],set_style('Times New Roman',220,True))

    workbook.save('d:\demo.xls')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('format_time','username')
    view_on_site = True
    show_full_result_count = True
    # list_select_related = True
    # list_display_links = ('username',)
    list_editable = ('username',)
    list_filter = ('username',)

    def get_urls(self):
        urls = super(ProfileAdmin, self).get_urls()
        my_urls = [
            url(r'^my_view/$',self.my_view),
        ]
        return my_urls+urls


    def my_view(self,request):
        write_excel()
        return HttpResponse("前往D盘查看")