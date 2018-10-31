from django.db import models
from user.models import *
# Create your models here.
class share(models.Model):
    # id=models.AutoField()
    share_user=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)
    share_name=models.CharField(max_length=150,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)