from django.conf.urls import patterns, include, url  
from views import MsgList  
  
urlpatterns = patterns('',  
    # Examples:  
    url(r'^$',MsgList.as_view(), name = 'index'),  
)  
