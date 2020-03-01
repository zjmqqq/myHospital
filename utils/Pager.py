#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/02/08
class PageInfo(object):
    def __init__(self,current_page,per_page,page_count,show_page,base_url):
        '''
        网页分页
        :param current_page: 当前页
        :param per_page: 每页数量
        :param page_count: 数据总行数
        :param show_page:  每页显示个数
        :param base_url:  前缀url
        '''
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        a,b = divmod(page_count,per_page)
        if b:
            a +=1
        self.all_page = a
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page-1)*self.per_page
    def end(self):
        return self.current_page * self.per_page
    def pager(self):
        page_list = []
        if self.all_page<self.show_page:
            begin = 1
            stop = self.all_page + 1
        else:
            if self.current_page <= self.show_page//2:
                begin = 1
                stop = self.show_page+1
            elif self.current_page >= self.all_page - self.show_page//2:
                begin = self.all_page - self.show_page + 1
                stop = self.all_page + 1
            else:
                begin = self.current_page - self.show_page//2
                stop = self.current_page + self.show_page//2 +1
        if self.current_page <= 1:
            prev = '<li><a href="#">上一页</a></li>'
        else:
            prev = '<li><a href="%s/?page=%s">上一页</a></li>' %(self.base_url,self.current_page - 1,)
        page_list.append(prev)
        for i in range(begin,stop):
            if i == self.current_page:
                temp = '<li class = "active"><a href="%s/?page=%s">%s</a></li>' %(self.base_url,i,i)
            else:
                temp = '<li><a href="%s/?page=%s">%s</a></li>' %(self.base_url,i,i)

            page_list.append(temp)
        if self.current_page >= self.all_page:
            next = '<li><a href="#">下一页</a></li>'

        else:
            next = '<li><a href="%s/?page=%s">下一页</a></li>' % (self.base_url,self.current_page + 1,)
        page_list.append(next)
        return ''.join(page_list)