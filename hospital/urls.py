#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/02/24
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/01/23
from django.conf.urls import url
from . import  views
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^about/', views.about),
    url(r'^introduce/', views.introduce),

]