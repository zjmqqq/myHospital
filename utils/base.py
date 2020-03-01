#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/02/14
from django.shortcuts import redirect
def checkLogin_p(func):
    '''
    判断是否登录
    :param func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):
        if request.session.get('pName',False):
            return func(request,*args,**kwargs)
        else:
            return redirect('/patient/login/')
    return wrapper


def checkLogin_d(func):
    '''
    判断是否登录
    :param func:
    :return:
    '''
    def wrapper(request,*args,**kwargs):
        if request.session.get('dName',False):
            return func(request,*args,**kwargs)
        else:
            return redirect('/doctor/login/')
    return wrapper