# -*- coding: utf-8 -*-
__author__ = 'root'
__date = '2017/04/05 22:31'

import xadmin
from .models import EmailVerifyRecord
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)