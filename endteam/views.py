from django.shortcuts import render
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
import json
from datetime import datetime
from . import models
import jwt
# Create your views here.
# 书写结团信息
def write(request):
    print(1111111111111111111111111111111111111111111111111111111111111111111)
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'

    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        team = json.loads(request.body)
        teamname = team['teamname']
        print(teamname,444444444444444444444444444444444444444444444444444444444444444)
        name=decoded['user_id']
        fell=team['feel']
        cc=team['title']
        aa={
            'spare1':cc,
            'feeling':fell,
            'launch_name_id':name,
            'team_name_id':teamname
        }
        models.teamshow.objects.create(**aa)
        models.team.objects.filter(team_name=teamname).update(status_id_id=2)
        return JsonResponse({'code':'结团成功！！！！'})


    else:
        return JsonResponse({'code': 'token已过期'})
