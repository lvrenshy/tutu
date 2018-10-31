from django.shortcuts import render
from django.http import HttpResponse, response, JsonResponse
from django.shortcuts import render, redirect, reverse
import json
import math
from datetime import datetime
from . import models
# from share import models

# Create your views here.
import jwt


# 按条件搜索团团详细信息-----------------------------------------有待优化----------------------------
def abcd(request):
    content=json.loads(request.body)['content']
    if not content:
        abcd=[]
        efg=[]
        len = models.team.objects.count()
        l = math.ceil(len / 2)
        # 拿到前两个团的团名
        if not request.body:
            ff = list(models.team.objects.filter(id__in=[1, 2]).values('team_name'))
            for i in ff:
                a1 = []
                t_name = list(models.team.objects.filter(team_name=i["team_name"]).values('launch_name_id'))[0]
                aa = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('starttime', 'introduce','team_name_id','team_number'))
                # print('aa',aa)
                start_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                tt=[]
                # 拿到开团人
                ttname1=list(models.team.objects.filter(team_name=i["team_name"]).values('launch_name_id'))
                # 拿到跟团人
                ttname2=list(models.followuser.objects.filter(team_name=i["team_name_id"]).values('u_name_id'))
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                abcd.append(a1)
            ll = {'page': l}
            efg.append(ll)
            abcd.append(efg)
            return JsonResponse({"acount": abcd})
        else:
            bb = []

            abcd=[]
            efg=[]
            ff = list(models.team.objects.values('id'))
            for i in ff:
                bb.append(i['id'])
            bb.sort()
            print(bb, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
            page = int(json.loads(request.body)['page'])
            for i in range((page - 1) * 2, page * 2):
                a1 = []
                ppname = list(models.team.objects.filter(id=bb[i]).values('team_name'))[0]
                t_name = list(models.team.objects.filter(id=bb[i]).values('launch_name_id'))[0]
                aa = list(
                    models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('starttime', 'introduce',
                                                                                            'team_name_id',
                                                                                            'team_number'))
                start_stage = list(
                    models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                abcd.append(a1)
            ll = {'page': l}
            efg.append(ll)
            abcd.append(efg)
            return JsonResponse({"acount": abcd})
    else:
        if not request.body:
            ff = list(models.team.objects.filter(id__in=[1, 2]).values('team_name'))
            print(22223333333333333)
            len = models.team.objects.filter(team_name__iregex=content).count()
            # 拿到搜索字段所对应页数
            if len > 1:
                abcd=[]
                efg=[]
                l = math.ceil(len / 2)
                aa = list(models.team.objects.filter(team_name__iregex=content).values('team_name'))
                ff = []
                ff.append(aa[0])
                ff.append(aa[1])
                print(ff)
                for i in ff:
                    a1=[]
                    t_name = list(models.team.objects.filter(team_name=i["team_name"]).values('launch_name_id'))[0]
                    aa = list(
                        models.teaminfo.objects.filter(team_name_id=i['team_name']).values('starttime', 'introduce',
                                                                                           'team_name_id',
                                                                                           'team_number'))
                    # print('aa',aa)
                    start_stage = list(
                        models.teaminfo.objects.filter(team_name_id=i['team_name']).values('start_stage'))
                    end_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('end_stage'))
                    ss = start_stage[0]['start_stage']
                    es = end_stage[0]['end_stage']
                    uu = {'luxian': ss + '--' + es}
                    a1.append(t_name)
                    a1.append(uu)
                    for i in list(aa):
                        a1.append(i)
                    abcd.append(a1)

                ll = {'page': l}
                efg.append(ll)
                abcd.append(efg)
                return JsonResponse({"acount": abcd})


            # 有bug,在搜索内容为空时。
            else:
                abcd=[]
                efg=[]
                a1=[]
                l = 1
                aa = list(models.team.objects.filter(team_name__iregex=content).values('team_name'))
                ff = []
                ff.append(aa[0])

                print(ff)

                t_name = list(models.team.objects.filter(team_name=ff[0]["team_name"]).values('launch_name_id'))[0]
                aa = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('starttime', 'introduce',
                                                                                           'team_name_id',
                                                                                           'team_number'))
                # print('aa',aa)
                start_stage = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                abcd.append(a1)

            ll = {'page': l}
            efg.append(ll)
            abcd.append(efg)
            return JsonResponse({"acount": a1})
        else:
            abcd=[]
            efg=[]
            # ff = list(models.team.objects.values('id'))
            page=int(json.loads(request.body)['page'])
            # 拿到模糊搜索查到的次数
            len = models.team.objects.filter(team_name__iregex=content).count()
            if len > 1:
                l = math.ceil(len / 2)
                # 拿到模糊搜索出的所有团名
                aa = list(models.team.objects.filter(team_name__iregex=content).values('team_name'))
                print(11111111111111111111111111111111)
                for i in range((page-1)*2,page*2):
                    bb = []
                    print(2222222222222222222222222222222222)
                    aa[i]['launch_name_id']=aa[i].pop('team_name')
                    bb.append(aa[i])

                    d4 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('starttime','introduce','team_name_id','team_number'))[0]
                    d6 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('start_stage'))[0]
                    d7 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('end_stage'))[0]
                    ss = d6['start_stage']
                    es = d7['end_stage']
                    uu = {'luxian': ss + '--' + es}
                    bb.append(uu)
                    bb.append(d4)
                    abcd.append(bb)
                ll = {'page': l}
                efg.append(ll)
                abcd.append(efg)
                return JsonResponse({'acount':abcd})

            else:

                efg=[]
                a1 = []
                l = 1
                aa = list(models.team.objects.filter(team_name__iregex=content).values('team_name'))
                ff = []
                ff.append(aa[0])

                print(ff)

                t_name = list(models.team.objects.filter(team_name=ff[0]["team_name"]).values('launch_name_id'))[0]
                aa = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('starttime', 'introduce',
                                                                                           'team_name_id',
                                                                                           'team_number'))
                # print('aa',aa)
                start_stage = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)

                ll = {'page': l}
                efg.append(ll)
                a1.append(efg)
                return JsonResponse({"acount": a1})

def search(request):
    if not request.body:
        abcd = []
        efg = []
        len = models.team.objects.count()
        l = math.ceil(len / 2)
        ff = list(models.team.objects.filter(id__in=[1, 2]).values('team_name'))
        for i in ff:
            a1 = []
            t_name = list(models.team.objects.filter(team_name=i["team_name"]).values('launch_name_id'))[0]
            aa = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('starttime', 'introduce',
                                                                                         'team_name_id', 'team_number'))
            # print('aa',aa)
            start_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('start_stage'))
            end_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('end_stage'))
            ss = start_stage[0]['start_stage']
            es = end_stage[0]['end_stage']
            uu = {'luxian': ss + '--' + es}
            a1.append(t_name)
            a1.append(uu)
            for i in list(aa):
                a1.append(i)
            abcd.append(a1)
        ll = {'page': l}
        efg.append(ll)
        abcd.append(efg)
        return JsonResponse({"acount": abcd})
    else:
        ss=json.loads(request.body)
        # 如果有页码没有搜索内容时(即不输入搜索字段，点击页码查看)
        if ss['page'] and not ss['content']:
            len = models.team.objects.count()
            l = math.ceil(len / 2)
            bb = []
            abcd = []
            efg = []
            ff = list(models.team.objects.values('id'))
            for i in ff:
                bb.append(i['id'])
            bb.sort()
            print(bb, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
            page = int(ss['page'])
            for i in range((page - 1) * 2, page * 2):
                a1 = []
                ppname = list(models.team.objects.filter(id=bb[i]).values('team_name'))[0]
                t_name = list(models.team.objects.filter(id=bb[i]).values('launch_name_id'))[0]
                aa = list(models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('starttime', 'introduce','team_name_id','team_number'))
                start_stage = list(models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=ppname['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                abcd.append(a1)
            ll = {'page': l}
            efg.append(ll)
            abcd.append(efg)
            return JsonResponse({"acount": abcd})
        # 如果有搜索内容没有页码时(即输入搜索内容后点击搜索后)
        elif ss['content'] and not ss['page']:
            abcd = []
            efg = []
            # ff = list(models.team.objects.values('id'))
            # 拿到模糊搜索查到的次数
            len = models.team.objects.filter(team_name__iregex=ss['content']).count()
            if len > 1:
                l = math.ceil(len / 2)
                # 拿到模糊搜索出的所有团名
                aa = list(models.team.objects.filter(team_name__iregex=ss['content']).values('team_name'))
                print(11111111111111111111111111111111)
                for i in range(0,2):
                    bb = []
                    print(2222222222222222222222222222222222)
                    aa[i]['launch_name_id'] = aa[i].pop('team_name')
                    bb.append(aa[i])

                    d4 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('starttime', 'introduce', 'team_name_id', 'team_number'))[0]
                    d6 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('start_stage'))[0]
                    d7 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('end_stage'))[0]
                    ss = d6['start_stage']
                    es = d7['end_stage']
                    uu = {'luxian': ss + '--' + es}
                    bb.append(uu)
                    bb.append(d4)
                    abcd.append(bb)
                ll = {'page': l}
                efg.append(ll)
                abcd.append(efg)
                return JsonResponse({'acount': abcd})
            elif len==1:
                aa = list(models.team.objects.filter(team_name__iregex=ss['content']).values('team_name'))[0]
                print(11111111111111111111111111111111)
                # for i in range(0, 2):
                bb = []
                print(2222222222222222222222222222222222)
                aa['launch_name_id'] = aa.pop('team_name')
                bb.append(aa)
                d4 = list(models.teaminfo.objects.filter(team_name_id=aa['launch_name_id']).values('starttime', 'introduce','team_name_id','team_number'))[0]
                d6 = list(models.teaminfo.objects.filter(team_name_id=aa['launch_name_id']).values('start_stage'))[0]
                d7 = list(models.teaminfo.objects.filter(team_name_id=aa['launch_name_id']).values('end_stage'))[0]
                ss = d6['start_stage']
                es = d7['end_stage']
                uu = {'luxian': ss + '--' + es}
                bb.append(uu)
                bb.append(d4)
                abcd.append(bb)
                ll = {'page': 1}
                efg.append(ll)
                abcd.append(efg)
                return JsonResponse({'acount': abcd})
            else:
                return JsonResponse({'acount':'暂无搜索内容'})

        elif not ss['content'] and not ss['page']:
            abcd = []
            efg = []
            len = models.team.objects.count()
            l = math.ceil(len / 2)
            ff = list(models.team.objects.filter(id__in=[1, 2]).values('team_name'))
            for i in ff:
                a1 = []
                t_name = list(models.team.objects.filter(team_name=i["team_name"]).values('launch_name_id'))[0]
                aa = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('starttime', 'introduce',
                                                                                             'team_name_id',
                                                                                             'team_number'))
                # print('aa',aa)
                start_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=i['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                abcd.append(a1)
            ll = {'page': l}
            efg.append(ll)
            abcd.append(efg)
            return JsonResponse({"acount": abcd})

        elif ss['content'] and ss['page']:
            abcd = []
            efg = []
            # ff = list(models.team.objects.values('id'))
            page = int(json.loads(request.body)['page'])
            # 拿到模糊搜索查到的次数
            len = models.team.objects.filter(team_name__iregex=ss['content']).count()
            if len > 1:
                l = math.ceil(len / 2)
                # 拿到模糊搜索出的所有团名
                aa = list(models.team.objects.filter(team_name__iregex=ss['content']).values('team_name'))
                print(11111111111111111111111111111111)
                for i in range((page - 1) * 2, page * 2):
                    bb = []
                    print(2222222222222222222222222222222222)
                    aa[i]['launch_name_id'] = aa[i].pop('team_name')
                    bb.append(aa[i])
                    d4 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('starttime','introduce','team_name_id','team_number'))[0]
                    d6 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('start_stage'))[0]
                    d7 = list(models.teaminfo.objects.filter(team_name_id=aa[i]['launch_name_id']).values('end_stage'))[0]
                    ss = d6['start_stage']
                    es = d7['end_stage']
                    uu = {'luxian': ss + '--' + es}
                    bb.append(uu)
                    bb.append(d4)
                    abcd.append(bb)
                ll = {'page': l}
                efg.append(ll)
                abcd.append(efg)
                return JsonResponse({'acount': abcd})
            elif len==1:
                efg = []
                a1 = []
                l = 1
                aa = list(models.team.objects.filter(team_name__iregex=ss['content']).values('team_name'))
                ff = []
                ff.append(aa[0])
                print(ff)
                t_name = list(models.team.objects.filter(team_name=ff[0]["team_name"]).values('launch_name_id'))[0]
                aa = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('starttime', 'introduce','team_name_id','team_number'))
                # print('aa',aa)
                start_stage = list(
                    models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('start_stage'))
                end_stage = list(models.teaminfo.objects.filter(team_name_id=ff[0]['team_name']).values('end_stage'))
                ss = start_stage[0]['start_stage']
                es = end_stage[0]['end_stage']
                uu = {'luxian': ss + '--' + es}
                a1.append(t_name)
                a1.append(uu)
                for i in list(aa):
                    a1.append(i)
                ll = {'page': l}
                efg.append(ll)
                a1.append(efg)
                return JsonResponse({"acount": a1})
            else:
                return JsonResponse({'acount':'暂无搜索内容'})
# 根据团名查询团内成员
def teamers(request):
    # 拿到团名
    ssss=json.loads(request.body)['teamname']
    a=list(models.team.objects.filter(team_name=ssss).values('launch_name_id'))[0]
    b=list(models.followuser.objects.filter(team_name_id=ssss).values('u_name_id'))
    abc=[]
    abc.append(a['launch_name_id'])
    if b:
        for i in b:
            abc.append(i['u_name_id'])
    return JsonResponse({'code':abc})

# 查看开过的团
def startTeam(request, content):
    # try:
    i = {'team_name': 'bilibili', 'launch_name_id': '17745566199'}
    models.team.objects.create(**i)
    print(content)
    users = models.team.objects.filter(launch_name_id_id='content').values('team_name')
    print(users)
    user = list(users)
    return JsonResponse({'code': user})



# 团队展示
def show(request):
    with open("travelteam/follow_user.json", encoding='utf-8') as fp:
        data = json.load(fp)
    for i in data:
        print(i)
        models.followuser.objects.create(**i)
    return HttpResponse("OK")
    # return HttpResponse('show team')


# 查看团的详细信息
def teaminfo(request):
    team = json.loads(request.body)
    teamname = team['teamname']
    info = list(
        models.teaminfo.objects.filter(team_name_id=teamname).values('team_name_id', 'introduce', 'team_number'))
    starttime = list(models.teaminfo.objects.filter(team_name_id=teamname).values('starttime'))
    endtime = list(models.teaminfo.objects.filter(team_name_id=teamname).values('endtime'))
    startstage = list(models.teaminfo.objects.filter(team_name_id=teamname).values('start_stage'))
    endstage = list(models.teaminfo.objects.filter(team_name_id=teamname).values('end_stage'))
    time = {'time': starttime[0]['starttime'] + '——' + endtime[0]['endtime']}
    stage = {'stage': startstage[0]['start_stage'] + '——' + endstage[0]['end_stage']}
    teamer = list(models.team.objects.filter(team_name=teamname).values('launch_name_id_id'))
    aa = []
    aa.append(info)
    aa.append(time)
    aa.append(stage)
    aa.append(teamer[0])
    return JsonResponse({'code': aa})


# 写团团
def write(request):
    return HttpResponse('write team')


# 参团
def inpartTeam(request):
    if request.method == 'POST':
        # try:
        age = request.POST.get('age')
        real_name = request.POST.get('real_name')
        license_num = request.POST.get('license_num')
        telephone = request.POST.get('telephone')
        weichat = request.POST.get('weichat')
        team_name_id = request.POST.get('team_name_id')
        users = {
            'age': age,
            'real_name': real_name,
            'license_num': license_num,
            'telephone': telephone,
            'weichat': weichat,
            'team_name_id': team_name_id
        }
        uu = []
        uu.append(users)
        for i in uu:
            models.followuser.objects.create(**i)
        return JsonResponse({'code': '参团成功'})
        # except  Exception as ex:
        #     return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code': '406'})


# 管理团
def guanliteam(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'

    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    us_name = decoded['user_id']
    tt = json.loads(request.body)
    t_name = tt['teamname']

    fowinfo = models.followuser.objects.filter(team_name_id=t_name).values('real_name', 'weichat', 'telephone')

    fwinfo = list(fowinfo)
    if len(fwinfo) == 1:
        aa = []
        aa.append(fwinfo[0])
        wantnum = models.teaminfo.objects.filter(team_name_id=t_name).values('team_number')
        nownum = models.followuser.objects.filter(team_name_id=t_name).count()
        but_team = {'nownum': nownum}
        # aa.append(list(wantnum))
        print(list(wantnum)[0])
        # 预期人数
        team_number = list(wantnum)[0]
        bb = []
        bb.append(team_number)
        bb.append(but_team)
        cc = []
        cc.append(aa)
        cc.append(bb)
        return JsonResponse({'code': cc})
    else:
        changdu = len(fwinfo)
        print(changdu)
        cc = []
        # id = models.followuser.objects.filter(team_name_id=t_name).values('id')
        for i in range(changdu):
            aa = []
            aa.append(fwinfo[i])
            cc.append(aa)
        wantnum = models.teaminfo.objects.filter(team_name_id=t_name).values('team_number')
        nownum = models.followuser.objects.filter(team_name_id=t_name).count()
        but_team = {'nownum': nownum + 1}
        # aa.append(list(wantnum))
        print(list(wantnum)[0])
        # 预期人数
        team_number = list(wantnum)[0]
        bb = []
        bb.append(team_number)
        bb.append(but_team)

        cc.append(bb)
        return JsonResponse({'code': cc})
        # return JsonResponse({'code':'saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'})


# 判断团的状态时
def statusteam(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'

    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        team = json.loads(request.body)
        teamname = team['teamname']
        status = list(models.team.objects.filter(team_name=teamname).values('status_id'))
        if status[0]['status_id'] == 0:
            return JsonResponse({'code': '未开团'})
        elif status[0]['status_id'] == 1:
            return JsonResponse({'code': '进行中'})
        elif status[0]['status_id'] == 2:
            return JsonResponse({'code': '已结团'})
    else:
        return JsonResponse({'code': 'token已过期'})


# 分页
def limit(request):
    return HttpResponse('team limit')


# 点赞
def approve(request):
    return HttpResponse('team approve')


# 评论
def review(request):
    return HttpResponse('team review')


# 建表
def jianbiao(request):
    with open("travelteam/attraction_info.json", encoding='utf-8') as fp:
        data = json.load(fp)

    for i in data:
        print(i)
        models.attractioninfo.objects.create(**i)
    return HttpResponse("OK")
