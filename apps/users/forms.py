# -*- coding: utf-8 -*-
__author__ = 'root'
__date = '2017/04/05 22:31'

from django import forms


class LoginFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)
