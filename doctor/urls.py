#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/02/24
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/01/23
from django.conf.urls import url
from . import  views
urlpatterns = [
    #url(r'^test/', views.test),
    #url(r'^index/(\w+)', views.index,name='n1'),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^index_doc/', views.index_doc),
    url(r'^scheduling/', views.scheduling),




]