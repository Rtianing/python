# coding = utf-8
# @Time: 2021/8/11 17:08
# @Author: 任添宁
# @File: urls.py
# @Software: PyCharm
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from.import views
urlpatterns = [
    url(r'^$',views.index,name='index'),

]


