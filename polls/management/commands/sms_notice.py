# -*- coding: utf-8 -*-
import urllib2
import pycurl
import StringIO
import json
import decimal
import urllib
from django.core.cache import cache
from django.conf import settings
from polls.models import *
from django.core.management.base import BaseCommand, CommandError
import httplib
import pdb
from django.conf import settings
version = "v2"
sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"
from django.core.exceptions import ObjectDoesNotExist



def tpl_send_sms(tpl_id, tpl_value, mobile):
    params = urllib.urlencode({'apikey': settings.SMS_YUNPIAN_APIKEY, 'tpl_id': tpl_id,
                               'tpl_value': urllib.urlencode(tpl_value), 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(settings.SMS_HOST, port=443, timeout=30)
    conn.request("POST", sms_tpl_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    print response_str
    return response_str
class Command(BaseCommand):
    args = '<Ref Ref ...>'
    help = 'Send notice to user...'
    def handle(self, *args, **options):
        # smsmessage = SmsMessage(message_type='0',mobile='13040871401',message_text='1231231',need_notice=True)
        # smsmessage.save()
        ss = SmsMessage.objects.filter(need_notice=True)
        # pdb.set_trace()
        for message in ss:
            if message.message_type == '0':

                tpl_id = 1733098
                tpl_value1 = message.message_text
                mobile = message.mobile
                tpl_value = {'#number#':tpl_value1}
                tpl_send_sms(tpl_id, tpl_value,mobile)
                message.need_notice = False
                message.save()
        # try:
        #     ss = SmsMessage.objects.get(need_notice=True)
        # except ObjectDoesNotExist:
        #     print "ssssssss"
        # for message in SmsMessage.objects.filter(need_notice=True):
        #     print message
            # pdb.set_trace()
            # if message.message_type == 0:
            # tpl_id = 1733098
                # ref = message.message_text
            # ref = 123123123
            # tpl_value = {'#number#': ref}
                # mobile = message.mobile
            # mobile = 13040871401
            # tpl_send_sms(tpl_id, tpl_value, mobile)
                # message.need_notice = False
                # message.save()


            # elif message.message_type == 1:
            #     tpl_id = 1733032
            #     ref = message.ref
            #     tpl_value = {'#number#': ref}
            #     mobile = message.mobile
            #     tpl_send_sms(tpl_id, tpl_value, mobile)
            #     message.need_notice = False
            #     message.save()
            # elif message.message_type == 2:
            #     tpl_id = 1733092
            #     ref = message.ref
            #     tpl_value = {'#number#': ref}
            #     mobile = message.mobile
            #     tpl_send_sms(tpl_id, tpl_value, mobile)
            #     message.need_notice = False
            #     message.save()
            # elif message.message_type == 3:
            #     tpl_id = 1731233
            #     ref = message.ref
            #     tpl_value = {'#number#': ref}
            #     mobile = message.mobile
            #     tpl_send_sms(tpl_id, tpl_value, mobile)
            #     message.need_notice = False
            #     message.save()
            # elif message.message_type == 4:
            #     tpl_id = 1733232
            #     ref = message.ref
            #     tpl_value = {'#number#': ref}
            #     mobile = message.mobile
            #     tpl_send_sms(tpl_id, tpl_value, mobile)
            #     message.need_notice = False
            #     message.save()




