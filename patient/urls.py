#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/01/23
from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
    url(r'^index_pat/', views.index_pat),
    url(r'^editInfo/', views.editInfo),
    url(r'^regRec/', views.regRec),
    url(r'^withdrawNum/', views.withdrawNum),
    url(r'^historicalInquiry/', views.historicalInquiry),

    url(r'^addData/', views.addData),


    url(r'^chooseType/', views.chooseType),
    url(r'^chooseDep/(\w+)', views.chooseDep),
    url(r'^chooseDoc/(\w+)', views.chooseDoc),
    url(r'^chooseDay/(\w+)', views.chooseDay),
    url(r'^chooseTime/(\w+)', views.chooseTime),
    url(r'^confirm/(\w+)', views.confirm),





    url(r'^myTry', views.myTry),
    url(r'^test', views.test),




]