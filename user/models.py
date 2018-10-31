from django.db import models
import json
# Create your models here.
class userpermission(models.Model):
    permission_id=models.IntegerField(unique=True)
    permission_name=models.CharField(max_length=60,unique=True)
class user(models.Model):
    # id = models.AutoField(),AutoField：自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性。
    name=models.CharField(max_length=60,unique=True)
    password=models.CharField(max_length=200)
    permission=models.ForeignKey(to='userpermission',to_field='permission_id',on_delete=models.CASCADE,default=0)
    spare1=models.CharField(max_length=255,null=True)
    spare2=models.CharField(max_length=255,null=True)
#     def __str__(self):
#         user={}
#         user['name']=self.name
#         user['password']=self.password
#         user['permission']=self.permission
#         # user['pub_time']=self.pub_time
#         return json.dumps(user,ensure_ascii=False)
#

class userinfo(models.Model):
    # 设置name为外键
    # to_field  设置所关联对象的关联字段。默认为关联对象的主键字段。
    # 经过筛查，在创建多对一的关系的,需要在Foreign的第二参数中加入on_delete=models.CASCADE  主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    name=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    avatar=models.CharField(max_length=20,null=True)
    signature=models.CharField(max_length=60,null=True)
    experience=models.CharField(max_length=60,null=True)
    tel=models.IntegerField(unique=True,null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)

class sixin(models.Model):
    author=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)
    userid = models.CharField(max_length=255, null=True)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
    # 存储当前时间
    uptime = models.DateTimeField(auto_now_add=True)




