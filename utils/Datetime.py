#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/02/14
import datetime
def myDate():
    today = datetime.date.today()
    dayList = []
    for i in range(7):
        tomorrow = today + datetime.timedelta(days=i)
        # tomorrow_str = tomorrow.strftime('%Y-%m-%d')
        dayList.append(tomorrow)
    return dayList

