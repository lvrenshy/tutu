from django.shortcuts import render
import json
import jwt
import datetime
import uuid
from datetime import datetime,timedelta
from qiniu import Auth
from django.db import connection
import time
# Create your views here.
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
from approve import models
from . import models
from travelteam import models
import random

from share import models
from tips import models
from question import models
from .miaodi import sendIndustrySms

# Create your views here.
# 用户首页刷新
def show(request):
    print(request.method)
    return HttpResponse('i am showinfo')
# 用户登录
def login(request):
    if request.method=='POST':
        try:
            data=json.loads(request.body)

            cc = []
            cc.append(data)
            print(cc)
            for i in cc:
                name = i['name']
                print(name)
                password = i['password']
                users=models.user.objects.filter(name=name).values()
                # 如果list(users)存在
                if list(users):
                    # 取到数据库中该用户名对应的密码
                    pwd=models.user.objects.filter(name=name).values('password')
                    # 将取到的密码转化为列表
                    list_pwd=list(pwd)
                    # 取到数组的项（要用[0]的方式取到），取到其中password的value值
                    pwd=list_pwd[0]["password"]
                    # 将取到的密码与输入的密码进行比对
                    if password==pwd:
                        print('begin token---------------------')
                        datetimeInt=datetime.utcnow() + timedelta(days=0, seconds=8000)
                        print(datetimeInt)
                        print(time.mktime(datetimeInt.timetuple()))
                        option = {
                            'iss': 'tutu.com',  #token的签发者
                            'exp': datetimeInt ,
                            'iat': datetime.utcnow(),
                            'aud': 'webkit',   #token的接收者，这里指定为浏览器
                            'user_id': name    #放入用户信息，唯一标识，解析后可以使用该信息
                        }
                        # 加盐
                        SECRET_KEY='123456'
                        # 将token加密
                        token=jwt.encode(option,SECRET_KEY,'HS256').decode()
                        print(token)
                        response = JsonResponse({"code": name}, status=200, content_type='application/json',charset='utf-8')
                        # 把token放入headers中
                        response["token"] = token
                        response["name"] = name
                        # 给token权限，不加这行无法发送token
                        response["Access-Control-Expose-Headers"] = "token"
                        # 将headers中的token进行解密
                        decoded=jwt.decode(token,SECRET_KEY,audience='webkit',algorithms=['HS256'])
                        # 拿到token中携带的user_id(以备不时之需)
                        print(decoded['user_id'])
                        return response
                    else:
                        return JsonResponse({"结果":"您输入的密码不正确"})
            else:
                return JsonResponse({"结果":"您的用户名有误"})
        except Exception as ex:
            return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code':'406'})

# 用户注册
def regist(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            print(data)
            cc=[]
            cc.append(data)
            print(cc)
            for i in cc:

                name=i['user']
                password=i['password']
                password2=i['conpassword']
                print(name)
                print(password)
                users = models.user.objects.filter(name=name).count()
                if users==0:
                    if password==password2:
                        user={
                            "name":name,
                            "password":password
                        }

                        print(user)
                        # print(name)
                        # 把用户名和密码封装成一个字典传到数据库中
                        ff=models.user.objects.create(**user)
                        datetimeInt = datetime.utcnow() + timedelta(days=0, seconds=8000)
                        option = {
                            'iss': 'tutu.com',  # token的签发者
                            'exp': datetimeInt,  # 过期时间
                            'aud': 'webkit',  # token的接收者，这里指定为浏览器
                            'user_id': name  # 放入用户信息，唯一标识，解析后可以使用该信息
                        }
                        # 加盐
                        SECRET_KEY = '123456'
                        # 将token加密
                        token = jwt.encode(option, SECRET_KEY, 'HS256').decode()
                        print(token)
                        response = JsonResponse({"code": name}, status=200, content_type='application/json',
                                                charset='utf-8')
                        # 把token放入headers中
                        response["token"] = token
                        response["name"] = name
                        # 给token权限，不加这行无法发送token
                        response["Access-Control-Expose-Headers"] = "token"
                        # 将headers中的token进行解密
                        decoded = jwt.decode(token, SECRET_KEY, audience='webkit', algorithms=['HS256'])
                        # 拿到token中携带的user_id(以备不时之需)
                        print(decoded['user_id'])
                        return response

                    else:
                        return JsonResponse({"code": "两次密码不一致"})
            else:
                return JsonResponse({"code": "你所输入的用户名已被占用"})
        except Exception as ex:
            return JsonResponse({"code": "408"})
    else:
        return JsonResponse({"code": "406"})

#发送验证码
def sendcode(request):
    '''
    :param          mobile
    :return:        (1): code:412       手机号码输入不正确，或者已被注册
                    (2): code:200       发送短信成功
    '''
    # print(now_date + 60)
    #
    # timeArray = time.localtime(now_date)
    #
    # otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    #
    # print(otherStyleTime)
    if request.method == "POST":
        data = json.loads(request.body)
        user=int(data['username'])
        print(user)#验证表单
        # if form.validate():
        #
        code=random.randrange(1000,9999)
        code=str(code)
        print(code)
        smsContent='【涂途】您的验证码为{0}，请于{1}分钟内正确输入，如非本人操作，请忽略此短信。'.format(code,5)
        sendIndustrySms(user,smsContent)

        print(1111111111111111)
        # sendIndustrySms(mobble,smsContent)


        # #将获取到的验证码存储到数据库中
        now_date = time.time() + 120;
        print(222222222222222222)

        cursor = connection.cursor()

        sql = "DELETE from securty WHERE user = {0}".format(user)
        print(33333333333333333333333)
        n = cursor.execute(sql)

        sql = "insert into securty() VALUE({0},{1},{2},{3})".format(user,code,now_date,1)
        print(4444444444444444444444)
        bb = cursor.execute(sql)

        print(55555555555555555)
        return JsonResponse({'code': 200, 'message': '发送成功'})
        # else:
        #     message = form.errors.popitem()[1][0]                 #弹出第一条验证失败错误信息
        #     print(type(jsonify({'code':406})))
        #     return JsonResponse({'code':412,'message':message})
        # response=JsonResponse({'code':200,'message':'发送成功'})
        # response['Access-Control-Allow-Origin']='*'

# 验证验证码
def yezheng(request):

    now_dates = time.time()

    data = json.loads(request.body)

    user = int(data['username'])
    yecode = int(data["yecode"])

    print(yecode)
    try:
        cursor = connection.cursor()

        sql = "select * from securty WHERE user = {0}".format(user)

        bb = cursor.execute(sql)

        res = cursor.fetchone()


        if (res[1] == yecode) and (float(res[2]) >= now_dates):

            sql = "UPDATE securty set state = 2 WHERE user = {0}".format(user)
            bb = cursor.execute(sql)
            r = {"code":200}
        else:
            r = {"code":403}

        return JsonResponse(r)

    except Exception as ex:
        return JsonResponse({'code':408})


# # 修改密码
def changepassword(request):
    if request.method=='POST':
        asd = request.META.get("HTTP_TOKEN")
        print(asd)
        SECRET_KEY = '123456'
        # 将headers中的token进行解密
        decoded = jwt.decode(asd, SECRET_KEY,audience='webkit', algorithms=['HS256'],options={'verify_exp':True})
        print('use token---------------------')
        print(decoded)
        endtime = decoded['exp']
        print(endtime)
        # timestamp = endtime
        # # 转换成localtime
        # time_local = time.localtime(timestamp)
        # # 转换成新的时间格式(2016-05-05 20:28:54)
        # dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        # 拿到token中时间，判断是否过期
        # token_time=time.mktime(endtime.timetuple())
        # print(token_time)
        now_time=datetime.now()+timedelta()
        n_time=time.mktime(now_time.timetuple())
        print(n_time)
        timex=endtime-n_time
        print(timex)
        # 拿到token中携带用户名
        print(decoded['user_id'])

        print(asd)
        if timex>0:
            try:
                data=json.loads(request.body)
                cc=[]
                cc.append(data)
                for i in cc:
                    password=i['password']
                    newpassword=i['newPassword']
                    pwd=models.user.objects.filter(name=decoded['user_id']).values('password')
                    if password==pwd[0]['password']:
                        user=models.user.objects.filter(name=decoded['user_id']).update(password=newpassword)
                        # 成功修改密码
                        return JsonResponse({'code':'200'})
                    else:
                        # 您输入的密码有误
                        return JsonResponse({'code':'408'})
            except Exception as ex:
                return JsonResponse({'code':'408'})
        else:
            return JsonResponse({'code':'token已过期请重新登录'})
    else:
        return JsonResponse({'code':'406'})

# 根据token判断是否登录
def panduan(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    return JsonResponse({'code':decoded['user_id']})
# updateinfo修改签名
def updateInfo(request):
    if request.method=='POST':
        asd = request.META.get("HTTP_TOKEN")
        SECRET_KEY = '123456'
        # 将headers中的token进行解密
        decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
        try:
            uu=json.loads(request.body)
            users=models.userinfo.objects.filter(name_id=decoded['user_id']).update(signature=uu['signature'])
            return JsonResponse({'code':'修改成功'})
        except Exception as ex:
            return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code':'406'})
# 查看参加过的团
def showInpart(request):
    # if request.method == 'GET':
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    aa=[]
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:
        users = models.team.objects.filter(launch_name_id_id=decoded['user_id']).values('team_name')
        user = list(users)
        for i in user:
            aa.append(i)
        uu = models.followuser.objects.filter(u_name_id=decoded['user_id']).values('team_name_id')
        for i in uu:
            aa.append(i)
        return JsonResponse({'code': aa})
    except Exception as ex:
        return JsonResponse({'code': '408'})
# 我要开团
def createteam(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'

    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    us_name=decoded['user_id']
    if decoded:
        try:
            infomation=json.loads(request.body)
            # 此时infomation中放的是团队信息
            aa={
                'team_name':infomation['teamname'],
                'launch_name_id_id':us_name,
                'status_id_id':0
                }
            models.team.objects.create(**aa)
            print((infomation['starttime']).replace('-','/'),'开始时间',1111111111111111111)
            print((infomation['endtime']).replace('-','/'),'结束时间','1111111111111111111')
            bb={
                'team_name_id':infomation['teamname'],
                'start_stage':infomation['startstage'],
                'end_stage':infomation['endstage'],
                'starttime':(infomation['starttime']).replace('-','/'),
                'endtime':(infomation['endtime']).replace('-','/'),
                'introduce':infomation['intro'],
                'team_number':infomation['num'],
            }

            models.teaminfo.objects.create(**bb)
            return JsonResponse({'code':'开团成功'})
        except Exception as ex:
            return JsonResponse({'code':'不知道什么原因你开团失败了'})
    else:
        return JsonResponse({'code':'TOKEN已过期请重新登录'})
# 我要参团
def jointeam(request):
    print(1111111111111111111111111111111111111111111)
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'

    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    us_name = decoded['user_id']

    if decoded:
        print(1111111111111111111111111111111111,request.body)
        uu = json.loads(request.body)
        # 我想要参加的团名
        want_team_name=uu['teamname']
        # 找到我参过的团和跟过的团
        myteam=models.team.objects.filter(launch_name_id_id=us_name).values('team_name')
        myteam2=models.followuser.objects.filter(u_name_id=us_name).values('team_name_id')
        # 找到我开过团的团名
        m_team=list(myteam)
        # 找到我跟过团的团名
        m_team2=list(myteam2)
        aa=[]
        print(want_team_name)
        for i in m_team:
            aa.append(i['team_name'])
        for i in m_team2:
            aa.append(i['team_name_id'])
        if not want_team_name in aa:
            infomation = {
                'u_name_id': us_name,
                'team_name_id': uu['teamname'],
                'telephone': uu['phone'],
                'age': uu['age'],
                'real_name': uu['realname'],
                'license_num': uu['card'],
                'weichat': uu['weichart']

            }
            print(infomation)
            models.followuser.objects.create(**infomation)
            return JsonResponse({'code': '跟团成功！！！'})
        else:
            return JsonResponse({'code': '你不能加入自己的团哦！！！'})
        # print(m_team)
        # a=uu['teamname']
        # print(a)
        # # 此处infomation代表参团者输入信息(age,rel_name,license_num,telephone,weichat,team_name_id,u_name_id)
        #
        # # 如果开过团
        # if m_team:
        #
        #     for i in m_team:
        #         # 判断是否要参加自己开过的团
        #         if i['team_name']==a:
        #             return JsonResponse({'code':'你不能参加自己的团哦！'})
        #
        #         else:
        #             infomation = {
        #                 'u_name_id': us_name,
        #                 'team_name_id': uu['teamname'],
        #                 'telephone': uu['telephone'],
        #                 'age': uu['age'],
        #                 'real_name': uu['realname'],
        #                 'license_num': uu['card'],
        #                 'weichat': uu['weichart']
        #
        #             }
        #             models.followuser.objects.create(**infomation)
        #             return JsonResponse({'code':'跟团成功！！！'})
        # else:
        #     infomation = {
        #         'u_name_id': us_name,
        #         'team_name_id': uu['teamname'],
        #         'telephone': uu['telephone'],
        #         'age': uu['age'],
        #         'real_name': uu['realname'],
        #         'license_num': uu['card'],
        #         'weichat': uu['weichart']
        #
        #     }
        #     models.followuser.objects.create(**infomation)
        #     return JsonResponse({'code': '跟团成功！！！'})
    else:
        return JsonResponse({'code':'TOKEN已过期请重新登录'})





# 查看我参加过的团的详细信息
def showmyteaminfo(request):
    return HttpResponse('ssssssssssss')

# 查看发表过的分享
def showShare(request):
    if request.method =="POST":
        asd = request.META.get("HTTP_TOKEN")
        SECRET_KEY = '123456'
        # 将headers中的token进行解密
        decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
        try:
            users = models.share.objects.filter(share_user_id=decoded['user_id']).values('share_name', 'content')
            user = list(users)
            return JsonResponse({'code': user})
        except Exception as ex:
            return JsonResponse({'code': '408'})


# 查看我发表过的分享的详细内容
def showmyshareinfo(request):
    return HttpResponse('sssssssssssssssssss')

# 删除发表过的分享-----------------------------------------------------
def deleteShare(request):
    if request.method=='GET':
        try:
            # 此处id要前台给过来，暂时测试写死
            models.share.objects.filter(id=22).delete()
            return JsonResponse({'code':'删除成功'})
        except Exception as ex:
            return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code':'406'})


# 查看发表过的锦囊
def showTips(request):

    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:

        users=models.tips.objects.filter(user_name_id=decoded['user_id']).values('content','stage','tip_name')

        print(users)
        user=list(users)
        return JsonResponse({'code':user})
    except Exception as ex:
        return JsonResponse({'code':'408'})

# 删除发表过的锦囊---------------------------------------------
def deleteTips(request):
    if request.method=='GET':
        try:
            models.tips.objects.filter(id=24).delete()
            return JsonResponse({'code':'删除成功'})
        except Exception as ex:
            return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code':'406'})


# 查看提出的问题
def showAsk(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:
        users=models.question.objects.filter(launch_user_id=decoded['user_id']).values()
        user=list(users)
        return JsonResponse({'code':user})
    except Exception as ex:
        return JsonResponse({'code':'408'})





# 查看我的回答
def showAnswer(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:
        users=models.answer.objects.filter(answser_user_id=decoded['user_id']).values()
        user=list(users)
        return JsonResponse({'code':user})
    except Exception as ex:
        return JsonResponse({'code':'408'})






# 查看点过赞的分享
def showApproveShare(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:
        users=models.approve.objects.filter(approve_user_id=decoded['user_id']).values('content_share_id_id')
        user=list(users)
        xx=user[0]['content_share_id_id']
        uu=models.share.objects.filter(id=1).values()
        uu1=list(uu)

        return JsonResponse({'code':uu1})
    except Exception as ex:
        return JsonResponse({'code':'408'})

# 查看我的评论
def showReview(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    try:
        users=models.review.objects.filter(reviewer_id=decoded['user_id']).values('content')
        user=list(users)
        return JsonResponse({'code':user})
    except  Exception as ex:
        return JsonResponse({'code':'408'})


# 写私信
def sixin(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        author=decoded['user_id']
        # 拿到私信内容
        content=json.loads(request.body)['sendcontent']
        #拿到私信人
        userid=json.loads(request.body)['username']
        aa={
            'author_id':author,
            'userid':userid,
            'content':content
        }
        print(aa,'sssssssssssssssssssssssssssssssssss')
        models.sixin.objects.create(**aa)
        return JsonResponse({'code':200})
    else:
        return JsonResponse({'code':'请去登录'})

#查看私信
def checksixin(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    print(decoded)
    if decoded:
        # 如果被私信人是我,找到私信人和私信内容
        aa=list(models.sixin.objects.filter(userid=decoded['user_id']).values('author_id','content').order_by('uptime'))
        print(aa,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        bb=[]
        for i in aa:
            aaa={
                'name': i['author_id'],
                'content': i['content']
            }
            bb.append(aaa)
        #如果私信人是我，拿到被私信人和私信内容
        cc=list(models.sixin.objects.filter(author=decoded['user_id']).values('userid','content').order_by('uptime'))
        dd=[]
        print(cc,'ccccccccccccccccccccccccccccccccccccc')
        for i in cc:

            ccc={
                'name':i['userid'],
                'content':i['content']
            }
            dd.append(ccc)
        abcd=[]
        abcd.append(bb)
        abcd.append(dd)
        print(abcd,'ssssssssssssssssssssssssssssssssssssssssss')
        return JsonResponse({'code': abcd})
    else:
        return JsonResponse({'code': '请去登录'})

def nnn(request):
    if request.method == 'GET':
        print('nihao')

def qiniu(request):
  if request.method == 'GET':
      try:
          # 填写七牛云的密钥
          access_key = "PfBG3HayGCpokh-sp1KD2cnVCjJpWmqY5LQWV7QG"
          secret_key = "6_PuVQscFj2QB1R5-ZgSmwQH8MUT7IQE2LyOtz7X"

          # 构建健全对象
          q = Auth(access_key, secret_key)
          file = request.GET.get("key")
          print(file)
          # 要上传的空间
          bucket_name = "petapp"

          # 上传到七牛后保存的文件名
          key = str(uuid.uuid4()) + "." + file.split(".")[1]

          # 生成上传的TOKEN,可以指定过期时间
          token = q.upload_token(bucket_name, key, 3600)
          return JsonResponse({"token": token, "filename": key})

      except Exception as ex:
          print(ex)
          return JsonResponse({"code": "409"})


def ceshi(request):
    datetimeInt = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
    SECRECT_KEY = 'secret'
    option = {
        'iss': 'jobapp.com',  # token的签发者
        'exp': datetimeInt,  # 过期时间
        'aud': 'webkit',  # token的接收者，这里指定为浏览器
        'user_id': '001'  # 放入用户信息，唯一标识，解析后可以使用该消息
    }
    # encoded2 = jwt.encode(payload=option,key= SECRECT_KEY, algorithm='HS256')
    # 这时token类型为字节类型，如果传个前端要进行token.decode()
    token = jwt.encode(option, SECRECT_KEY, 'HS256')
    print(token)
    return JsonResponse({"code": "808"})


