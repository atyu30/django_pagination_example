from django.db import models

# Create your models here.

from django.contrib.auth.models import User  
# Create your models here.  
class Msg(models.Model):  
    title = models.CharField(max_length = 30)  
    content = models.TextField()  
    user = models.ForeignKey(User)  
    ip = models.IPAddressField()  
    datetime = models.DateTimeField(auto_now_add = True)  
    click_count = models.IntegerField(default = 0)  
  
    def __unicode__(self):  
        return self.title  
