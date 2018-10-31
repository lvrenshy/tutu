from django.db import models
from user.models import user
# Create your models here.
class teamstatus(models.Model):
    status_id=models.IntegerField(unique=True)
    status_name=models.CharField(max_length=20)
    spare1 = models.CharField(max_length=255, null=True)
class team(models.Model):
    team_name=models.CharField(max_length=20,unique=True)
    # launch_name=models.ForeignKey(to='user',to_field='password',on_delete=models.CASCADE)
    status_id=models.ForeignKey(to=teamstatus,to_field='status_id',on_delete=models.CASCADE,default=0)
    launch_name_id=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class teaminfo(models.Model):
    team_number=models.IntegerField(null=True)
    team_name=models.ForeignKey(to='team',to_field='team_name',on_delete=models.CASCADE)
    starttime=models.CharField(max_length=60)
    endtime=models.CharField(max_length=60)
    introduce=models.CharField(max_length=100)
    start_stage=models.CharField(max_length=200)
    end_stage=models.CharField(max_length=200)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
# #
class city(models.Model):
    city_name=models.CharField(max_length=255,unique=True)
    city_content=models.CharField(max_length=10000)
    city_id=models.IntegerField(unique=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class teamroute(models.Model):
    team_name=models.ForeignKey(to='team',to_field='team_name',on_delete=models.CASCADE)
    city_name=models.ForeignKey(to='city',to_field='city_name',on_delete=models.CASCADE)
    route=models.CharField(max_length=10000)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class attractionbaseinfo(models.Model):
    city_name=models.ForeignKey(to='city',to_field='city_name',on_delete=models.CASCADE)
    attraction_name=models.CharField(max_length=200,unique=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)

class attractioninfo(models.Model):
    attraction_name = models.ForeignKey(to='attractionbaseinfo', to_field='attraction_name', on_delete=models.CASCADE)
    attraction_intro=models.CharField(max_length=10000)
    attraction_img=models.CharField(max_length=10000)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
    # 图片不知道怎么放，暂时写为字符串格式，后期再改
class followuser(models.Model):
    # user_name=models.ForeignKey(to='user',to_field='name',on_delete=models.CASCADE)
    u_name=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    team_name=models.ForeignKey(to='team',to_field='team_name',on_delete=models.CASCADE)
    age=models.IntegerField(null=True)
    real_name=models.CharField(max_length=100,null=True)
    license_num=models.CharField(max_length=100,null=True)
    telephone=models.CharField(max_length=40,null=True)
    weichat=models.CharField(max_length=255,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)

#     # 把telephone类型改为int后，数据录入时总说长度不够，不得已只能改回char


