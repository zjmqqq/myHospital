#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/01/23
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
    url(r'^index_pat/', views.index_pat),
    url(r'^detail/', views.detail),
    url(r'^editInfo/', views.edit_info),
    url(r'^regRec/', views.reg_rec),
    url(r'^withdrawNum/', views.withdraw_num),
    url(r'^historicalInquiry/', views.historical_inquiry),
    url(r'^addData/', views.add_data),
    url(r'^chooseType/', views.choose_type),
    url(r'^chooseDep/(\w+)', views.choose_dep),
    url(r'^chooseDoc/(\w+)', views.choose_doc),
    url(r'^chooseDay/(\w+)', views.choose_day),
    url(r'^chooseTime/(\w+)', views.choose_time),
    url(r'^confirm/(\w+)', views.confirm),
]
