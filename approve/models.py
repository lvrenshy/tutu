from django.db import models
from user.models import *
from share.models import *
from tips.models import *
# Create your models here.
class approve(models.Model):
    # id=models.AutoField()
    approve_user=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    content_share_id=models.ForeignKey(to=share,to_field='id',on_delete=models.CASCADE,null=True)
    content_tips_id=models.ForeignKey(to=tips,to_field='id',on_delete=models.CASCADE,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class review(models.Model):
    # id=models.AutoField()
    content=models.CharField(max_length=10000)
    content_share_id=models.ForeignKey(to=share,to_field='id',on_delete=models.CASCADE,null=True)
    content_tips_id=models.ForeignKey(to=tips,to_field='id',on_delete=models.CASCADE,null=True)
    # 评论人id
    reviewer = models.ForeignKey(to=user, to_field='name', on_delete=models.CASCADE)
    # 被评论人id
    userid=models.CharField(max_length=255,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
    # 存储当前时间
    uptime=models.DateTimeField(auto_now_add=True)
