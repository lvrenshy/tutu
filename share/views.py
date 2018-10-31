from django.shortcuts import render
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
import json
import jwt
from datetime import datetime
from . import models
import math
# from tips import models
from approve import models
# Create your views here.
# 分享展示
def show(request):
    with open("share/share.json",encoding='utf-8') as fp:
        data=json.load(fp)
    for i in data:
        # print(i['content'])
        models.share.objects.create(**i)

    return HttpResponse("OK")
    # return HttpResponse('show share')
# 分享展示（前台get请求方式应改为post请求方式）
def search(request):
    a1=[]

    len = models.share.objects.count()
    l = math.ceil(len / 3)
    if not request.body:
    # 拿到前两个团的团名
        ff = list(models.share.objects.filter(id__in=[1,2,3]).values('share_name','id'))
        # print(ff)
        for i in ff:

            aa=list(models.share.objects.filter(share_name=i['share_name']).values('share_user_id', 'share_name','content'))
            print(aa,1111111111111111111111111111111111111111111)
            for i in list(aa):
                a1.append(i)
        ll = {'page': l}
        a1.append(ll)
        print(a1)
        tipnum = []
        for i in ff:
            sss = list(models.share.objects.filter(share_name=i['share_name']).values('id'))[0]['id']
            tipnum.append(sss)
        mmm = []
        for i in tipnum:
            sharenum = models.approve.objects.filter(content_share_id_id=i).count()
            mmm.append(sharenum)
        a1.append(mmm)
        return JsonResponse({"acount": a1})
    else:
        tipnum = []
        bb=[]
        page=int(json.loads(request.body)['page'])
        ff = list(models.share.objects.values('share_user_id', 'share_name','content'))
        for i in range((page-1)*3,page*3):
            bb.append(ff[i])

        for i in bb:
            sss = list(models.share.objects.filter(share_name=i['share_name']).values('id'))[0]['id']
            tipnum.append(sss)
        mmm = []
        for i in tipnum:
            sharenum = models.approve.objects.filter(content_share_id_id=i).count()
            mmm.append(sharenum)
        ll = {'page': l}
        bb.append(ll)
        bb.append(mmm)
        return JsonResponse({"acount": bb})
# 写分享
def write(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        ss=json.loads(request.body)
        ab={
            'content':ss['content'],

            'share_name':ss['sharename'],
            'share_user_id':decoded['user_id']
        }
        models.share.objects.create(**ab)
        return JsonResponse({'code':'成功哦'})
    else:
        return JsonResponse({'code':'token过期'})

# 分页
def limit(request,con):
    # try:
        print(111111111111111111)
        if not con:
            len = models.share.objects.all().count()
        else:
            print(con)
            len = models.share.objects.filter(share_name__icontains=con).count()
            print(len)
        return JsonResponse({"acount": len})
    # except Exception as ex:
    #     return JsonResponse({"code": "409"})

    # return HttpResponse('share limit')
# 显示分享点赞数量
def approvenunm(request):
    pass
    # approve_count=models.share.objects.filter()



# 点赞
def approve(request):

    return HttpResponse('share approve')

# 展示评论
def showreview(request):
    cc = json.loads(request.body)['sharename']
    # 拿到分享id
    id = list(models.share.objects.filter(share_name=cc).values('id'))[0]['id']

    a2=[]
    cc=list(models.review.objects.filter(content_share_id_id=id).values('content','reviewer_id'))
    for i in cc:
        a1 = []
        # 把一级评论内容添加进a1
        a1.append({
            'content':i['content']
        })
        # 拿到二级评论的评论人id和评论内容
        mm=list(models.review.objects.filter(userid=i['reviewer_id']).values('content','reviewer_id'))
        a1.append(mm)
        a2.append(a1)

    return JsonResponse({'code':a2})


# 评论锦囊(评论接口)
def review(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    if decoded:
        # # 拿到要评论的分享名
        # print(11111111111111111111111111111111111)
        cc = json.loads(request.body)['sharename']
        # # 拿到被评论人id
        # ff = json.loads(request.body)['name']
        # content = json.loads(request.body)['content']
        # print(2222222222222222222222222222222222222222222)

        # 拿到锦囊名对应的锦囊id
        print(111111111111111111111111111111111111111111111)
        id = list(models.share.objects.filter(share_name=cc).values('id'))[0]['id']
        # 拿到一级评论内容,按时间降序排序
        ff = list(models.review.objects.filter(content_share_id_id=id).values('content').order_by('-uptime'))
        b1 = []
        cccccc = []
        print(222222222222222222222222222222222)
        # 拿到评论过该锦囊的评论人名
        user_name = list(models.review.objects.filter(content_tips_id_id=id).values('reviewer_id'))
        for i in ff:
            aaaaaa = []
            aaaaaa.append({'one': i['content']})
            aaaaaa.append({'name': i['share_user_id']})
            bbbbbb = []

            # 通过一级评论人名字拿到二级评论内容通过时间排序
            mm = list(models.review.objects.filter(userid=i['reviewer_id']).values('content', 'reviewer_id').order_by('-uptime'))
            if mm:
                kkkk=[]
                for i in mm:
                    bbbbbb.append({'two': i['content']})
                    bbbbbb.append({'twoname': i['reviewer_id']})
                    kkkk.append(bbbbbb)
                cccccc.append(kkkk)
            b1.append(cccccc)
        return JsonResponse({'code': b1})
    else:
        return JsonResponse({'code': 'token已过期'})


# 书写评论
def writereview(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    cc = json.loads(request.body)['sharename']
    # 如果有内容和锦囊名
    if json.loads(request.body)['sharename'] and json.loads(request.body)['content']:
        content = json.loads(request.body)['content']
        # 拿到分享id
        id = list(models.share.objects.filter(share_name=cc).values('id'))[0]['id']
        ff = {
            'content': content,
            'content_share_id_id': id,
            'reviewer_id': decoded['user_id']
        }
        models.review.objects.create(**ff)
        # ff = list(models.review.objects.filter(content_tips_id_id=id).values('content').order_by('-uptime'))
        # b1 = []
        # cccccc = []
        # print(222222222222222222222222222222222)
        # # 拿到评论过该锦囊的评论人名
        # user_name = list(models.review.objects.filter(content_tips_id_id=id).values('reviewer_id'))
        # for i in ff:
        #     aaaaaa = []
        #     # 一级评论
        #     aaaaaa.append({'one': i['content']})
        #     for i in user_name:
        #         bbbbbb = []
        #
        #         # 通过一级评论人名字拿到二级评论内容通过时间排序
        #         mm = list(
        #             models.review.objects.filter(userid=i['reviewer_id']).values('content').order_by('-uptime'))
        #         if mm:
        #             bbbbbb.append({'two': mm[0]['content']})
        #             aaaaaa.append(bbbbbb)
        #     cccccc.append(aaaaaa)
        # b1.append(cccccc)
        return JsonResponse({'code': 200})
    # 如果有评论人
    elif json.loads(request.body)['name']:
        ff = json.loads(request.body)['name']
        content = json.loads(request.body)['content']
        id = list(models.share.objects.filter(share_name=cc).values('id'))[0]['id']
        sss = {
            'content': content,
            'userid': ff,
            'reviewer_id': decoded['user_id'],
            'content_share_id_id':id
        }
        models.review.objects.create(**sss)
        # id = list(models.tips.objects.filter(tip_name=cc).values('id'))[0]['id']
        # # 拿到一级评论内容,按时间降序排序
        # ff = list(models.review.objects.filter(content_tips_id_id=id).values('content').order_by('-uptime'))
        # b1 = []
        # cccccc = []
        # print(222222222222222222222222222222222)
        # # 拿到评论过该锦囊的评论人名
        # user_name = list(models.review.objects.filter(content_tips_id_id=id).values('reviewer_id'))
        # for i in ff:
        #     aaaaaa = []
        #     # 一级评论
        #     aaaaaa.append({'one': i['content']})
        #     for i in user_name:
        #         bbbbbb = []
        #
        #         # 通过一级评论人名字拿到二级评论内容通过时间排序
        #         mm = list(
        #             models.review.objects.filter(userid=i['reviewer_id']).values('content').order_by('-uptime'))
        #         if mm:
        #             bbbbbb.append({'two': mm[0]['content']})
        #             aaaaaa.append(bbbbbb)
        #     cccccc.append(aaaaaa)
        # b1.append(cccccc)
        return JsonResponse({'code': 200})
