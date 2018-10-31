from django.db import models
from user.models import *
from share.models import *
from travelteam.models import *
from tips.models import *
# Create your models here.
class questionstyle(models.Model):
    # id=models.AutoField()
    style_id=models.IntegerField(unique=True)
    style_name=models.CharField(max_length=30)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class question(models.Model):
    question_id=models.IntegerField(unique=True)
    launch_user=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    question_style=models.ForeignKey(to=questionstyle,to_field='style_id',on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)
class answer(models.Model):
    answser_user=models.ForeignKey(to=user,to_field='name',on_delete=models.CASCADE)
    question_id=models.ForeignKey(to=question,to_field='question_id',on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)
    spare1 = models.CharField(max_length=255, null=True)
    spare2 = models.CharField(max_length=255, null=True)



