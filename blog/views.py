#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView  
from models import Msg  
ITEMS_PER_PAGE = 3  
  
  
class MsgList(ListView):  
    model = Msg#数据模型  
    context_object_name = 'msg_list'#模板中变量  
    template_name = 'index.html'#模板文件  
    paginate_by = ITEMS_PER_PAGE#一个页面显示的条目  
