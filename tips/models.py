from django.db import models
from user.models import *
# Create your models here.
class tips(models.Model):
    # id=models.AutoField()
    user_name=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE,default=0)
    content=models.CharField(max_length=10000)
    stage=models.CharField(max_length=255)
    tip_name=models.CharField(max_length=140,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)