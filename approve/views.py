from django.shortcuts import render
import json
# Create your views here.
import jwt
from tips import models
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
from django.db.models.aggregates import Count
from . import models

# Create your views here.
# 用户首页刷新
def show(request):
    print(request.method)
    return HttpResponse('i am showinfo')
def login(request):
    # print(request.method)
    with open("approve/review.json",encoding='utf-8') as fp:
        data=json.load(fp)
    for i in data:
        print(i)
        models.review.objects.create(**i)
    return HttpResponse("OK")
    # return HttpResponse('i am login')
# 点赞数量最多的锦囊(锦囊名)，显示前七个
def maxtip(request):
    # 找到锦囊id和被点赞的次数封装成一个字典
    print(444444444444444444444)
    a=models.approve.objects.values("content_tips_id_id").annotate(cishu=Count("content_tips_id_id")).order_by('-cishu')
    a=list(a)[0:7]
    print(a[0:7])
    fff=[]
    for i in a:
        uu=models.tips.objects.filter(id=i['content_tips_id_id']).values('tip_name')
        # print(list(uu))
        user=(list(uu))
        for xx in user:
            xx['sharename'] = xx.pop('tip_name')
            fff.append(xx)
    print(fff)
        # user.append(uu)
    # return JsonResponse({'code':fff})
    return HttpResponse(json.dumps(fff, ensure_ascii=False))
# 点赞数量最多的分享(分享名)，显示前七个
def maxsh(request):
    # 查询content_share_id_id值出现最多次的七个，与次数一起封装成字典，一一对应
    a = models.approve.objects.values("content_share_id_id").annotate(cishu=Count("content_share_id_id")).order_by('-cishu')
    a = list(a)[0:7]
    # print(a[0:7])
    fff = []
    for i in a:
        uu = models.share.objects.filter(id=i['content_share_id_id']).values('share_name')
        # print(list(uu))
        user = (list(uu))
        for xx in user:
            xx['sharename']=xx.pop('share_name')
            fff.append(xx)
    print(fff)
    return HttpResponse(json.dumps(fff, ensure_ascii=False))
    # return JsonResponse({'code': fff})
    # return HttpResponse('此为点赞最多分享')
# 查看点赞过的分享(分享名)
def showshare(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    ff=[]
    try:
        users = models.approve.objects.filter(approve_user_id=decoded['user_id']).values('content_share_id_id')

        ll = len(users)
        if ll>0:
            user = list(users)
            for i in range(ll):
                xx = user[i]['content_share_id_id']

                # 查询点赞过的分享名
                uu = models.share.objects.filter(id=xx).values('share_name')
                ff.append(list(uu)[0])
            print(ff,'ffffffffffffffff')
            return JsonResponse({'code': ff})
        else:
            return JsonResponse({'code':412})
    except Exception as ex:
        return JsonResponse({'code':'408'})

# 查看点过赞的详细分享内容
def showApproveShare(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        share_name = json.loads(request.body)
        sid = share_name['sharename']
        cc = models.share.objects.filter(share_name=sid).values('share_user_id', 'share_name', 'content')
        bb = list(cc)
        return JsonResponse({'code': bb})
    else:
        return JsonResponse({'code': 'token过期'})



    # return HttpResponse('show approve')
# 查看点过赞的锦囊(锦囊名)
def showtip(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        ff=[]
        try:
            users = models.approve.objects.filter(approve_user_id=decoded['user_id']).values('content_tips_id_id')
            ll=len(users)
            if ll>0:
                user = list(users)
                for i in range(ll):
                    xx = user[i]['content_tips_id_id']
                    print(xx)
                    # 查询点赞过的分享名
                    uu = models.tips.objects.filter(id=xx).values('tip_name')
                    ff.append(list(uu)[0])
                    print(ff)
                print(ff,'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
                return JsonResponse({'code': ff})
            else:
                return JsonResponse({'code': 412})
        except Exception as ex:
            return JsonResponse({'code':'408'})
    else:
        return JsonResponse({'code':'token过期'})
# 查看点过赞的锦囊详细内容
def showApproveTips(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:

        tip_name=json.loads(request.body)
        tid=tip_name['tipname']

        cc=models.tips.objects.filter(tip_name=tid).values('user_name_id','tip_name','content','stage')
        bb=list(cc)

        return JsonResponse({'code':bb})
    else:
        return JsonResponse({'code':'token过期'})

# 查看我的评论的分享
def showshareReview(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])

    bb=[]
    # try:

    users=models.review.objects.filter(reviewer_id=decoded['user_id']).values('content_share_id','content')
    print(users)
    if users:
        uu=list(users)
        # print(uu)
        for i in range(len(uu)):
            # print(len(uu))

            if uu[i]['content_share_id']:
                aa = []
                content=models.review.objects.filter(reviewer_id=decoded['user_id'],content_share_id=uu[i]['content_share_id']).values('content')
                share_name = models.share.objects.filter(id=uu[i]['content_share_id']).values('share_name')
                aa.append(list(content)[0])

                aa.append(list(share_name)[0])
                # print(aa)
                bb.append(list(aa))
        # print(bb)

        return JsonResponse({'code':bb})
    else:
        return JsonResponse({'code':'你还未评论过任何分享哦'})

# 查看我评论的锦囊
def showtipReview(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    bb = []
    users = models.review.objects.filter(reviewer_id=decoded['user_id']).values('content_tips_id', 'content')
    if users:
        uu = list(users)
        # print(uu)
        for i in range(len(uu)):
            # print(len(uu))

            if uu[i]['content_tips_id']:
                aa = []
                content = models.review.objects.filter(reviewer_id=decoded['user_id'],content_tips_id=uu[i]['content_tips_id']).values('content')
                tip_name = models.tips.objects.filter(id=uu[i]['content_tips_id']).values('tip_name')
                aa.append(list(content)[0])

                aa.append(list(tip_name)[0])
                bb.append(list(aa))

        return JsonResponse({'code': bb})
    else:
        return JsonResponse({'code':'你还未点赞过任何锦囊哦'})

# 查询评论过的锦囊的详细内容
def reviewinfotip(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        tip=json.loads(request.body)
        tipid=tip['tipname']
        cc = models.tips.objects.filter(tip_name=tipid).values('user_name_id', 'tip_name', 'content', 'stage')
        bb = list(cc)

        return JsonResponse({'code': bb})


    else:
        return JsonResponse({'code':'token过期'})

# 查看评论过分享的详细内容
def reviewinfoshare(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        tip = json.loads(request.body)
        tipid = tip['sharename']
        cc = models.share.objects.filter(share_name=tipid).values('share_user_id', 'share_name', 'content')
        bb = list(cc)

        return JsonResponse({'code': bb})


    else:
        return JsonResponse({'code': 'token过期'})

# 点赞分享
def approveshare(request):
    ss=json.loads(request.body)['sharename']
    shareid=list(models.share.objects.filter(share_name=ss).values('id'))[0]
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        search=models.approve.objects.filter(content_share_id_id=shareid['id'],approve_user_id=decoded['user_id']).count()
        if search==0:
            uu={
                'approve_user_id':decoded['user_id'],
                'content_share_id_id':shareid['id']
            }
            models.approve.objects.create(**uu)
            return JsonResponse({'code':210})
        else:
            models.approve.objects.filter(content_share_id_id=shareid['id'],approve_user_id=decoded['user_id']).delete()
            return JsonResponse({'code': 410})
    else:
        return JsonResponse({'code':'token已过期'})
# 点赞锦囊
def approvetip(request):
    ss=json.loads(request.body)['tipname']
    shareid=list(models.tips.objects.filter(tip_name=ss).values('id'))[0]
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        search=models.approve.objects.filter(content_tips_id_id=shareid['id'],approve_user_id=decoded['user_id']).count()
        print(search,'ssssssssssssshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        if search==0:
            print(111111111111111111111111111111111111111)
            uu={
                'approve_user_id':decoded['user_id'],
                'content_tips_id_id':shareid['id']
            }
            models.approve.objects.create(**uu)
            print(22222222222222222222222222222222222222222222222222)
            return JsonResponse({'code':210})
        else:
            models.approve.objects.filter(content_tips_id_id=shareid['id'],approve_user_id=decoded['user_id']).delete()
            return JsonResponse({'code': 410})
    else:
        return JsonResponse({'code':'token已过期'})
# 评论分享

