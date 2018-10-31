from django.db import models
from user.models import *
from travelteam.models import *
# Create your models here.
class teamshow(models.Model):
    team_name=models.ForeignKey(to=team,to_field='team_name',on_delete=models.CASCADE)
    process_introduce=models.CharField(max_length=2000,null=True)
#     不知道process_introduce，看数据里面都是null所以给了个char类型允许为空
    image=models.CharField(max_length=1000,null=True)
    # 图片不知道怎么放，暂时写为字符串格式，后期再改
    feeling=models.CharField(max_length=10000,null=True)
    launch_name=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
