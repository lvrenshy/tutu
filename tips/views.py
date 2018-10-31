from django.shortcuts import render
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
import json
from datetime import datetime
from . import models
import math
import jwt
from approve import models
# Create your views here.
# 锦囊展示
def show(request):
    with open("tips/tips.json",encoding='utf-8') as fp:
        data=json.load(fp)
    for i in data:
        print(i)
        models.tips.objects.create(**i)
    return HttpResponse("OK")
    # return HttpResponse('show tips')
# 展示锦囊(前台请求方式get应改为post)
def search(request):
    a1=[]

    len = models.tips.objects.count()
    l = math.ceil(len / 3)
    if not request.body:

        ff = list(models.tips.objects.filter(id__in=[1,2,3]).values('tip_name'))
        # print(ff)
        for i in ff:
            aa=list(models.tips.objects.filter(tip_name=i['tip_name']).values('user_name_id', 'tip_name','content'))
            for i in list(aa):
                a1.append(i)

        # else:
        #     print(22223333333333333)
        #     len = models.share.objects.filter(share_name__iregex=content).count()
        #     # 拿到搜索字段所对应页数
        #     l = math.ceil(len / 3)
        #     aa = list(models.share.objects.filter(share_name__iregex=content).values('share_name'))
        #     ff=[]
        #     ff.append(aa[0])
        #     ff.append(aa[1])
        #     print(ff)
        #     for i in ff:
        #
        #         aa = list(models.share.objects.filter(share_name=i['share_name']).values('share_user_id', 'share_name','content'))
        #         for i in list(aa):
        #             a1.append(i)
        ll = {'page': l}
        a1.append(ll)
        print(a1)
        tipnum=[]
        for i in ff:
            sss=list(models.tips.objects.filter(tip_name=i['tip_name']).values('id'))[0]['id']
            tipnum.append(sss)
        mmm=[]
        for i in tipnum:
            sharenum=models.approve.objects.filter(content_tips_id_id=i).count()
            mmm.append(sharenum)
        a1.append(mmm)
        return JsonResponse({"acount": a1})
    else:
        bb=[]
        page = int(json.loads(request.body)['page'])
        ff = list(models.tips.objects.values('user_name_id', 'tip_name','content'))
        for i in range((page-1)*3,page*3):
            bb.append(ff[i])
        tipnum = []
        for i in bb:
            sss = list(models.tips.objects.filter(tip_name=i['tip_name']).values('id'))[0]['id']
            tipnum.append(sss)
        mmm = []
        for i in tipnum:
            sharenum = models.approve.objects.filter(content_tips_id_id=i).count()
            mmm.append(sharenum)
        bb.append(mmm)
        ll = {'page': l}
        bb.append(ll)
        return JsonResponse({"acount": bb})
# 写锦囊
def write(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        ss=json.loads(request.body)
        ab={
            'content':ss['content'],

            'tip_name':ss['tipname'],
            'user_name_id':decoded['user_id']
        }
        models.tips.objects.create(**ab)
        return JsonResponse({'code':'成功哦'})
    else:
        return JsonResponse({'code':'token过期'})



# 展示锦囊
def showreview(request):
    cc = json.loads(request.body)['tipname']
    # 拿到锦囊id
    id = list(models.tips.objects.filter(tip_name=cc).values('id'))[0]['id']

    a2=[]
    cc=list(models.review.objects.filter(content_tips_id_id=id).values('content','reviewer_id'))
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
        cc=json.loads(request.body)['tipname']
        # # 拿到被评论人id
        # ff = json.loads(request.body)['name']
        # content = json.loads(request.body)['content']
        # print(2222222222222222222222222222222222222222222)

        # 拿到锦囊名对应的锦囊id
        print(111111111111111111111111111111111111111111111)
        if cc:
            id=list(models.tips.objects.filter(tip_name=cc).values('id'))[0]['id']
            # 拿到一级评论内容,按时间降序排序
            ff = list(models.review.objects.filter(content_tips_id_id=id).values('content','reviewer_id').order_by('-uptime'))
            b1 = []
            cccccc=[]
            print(222222222222222222222222222222222)
            # 拿到评论过该锦囊的评论人名
            user_name=list(models.review.objects.filter(content_tips_id_id=id).values('reviewer_id'))
            for i in ff:
                aaaaaa = []
                # 拿到一级评论内容和评论人
                aaaaaa.append({'one':i['content']})
                aaaaaa.append({'name':i['reviewer_id']})
                # 通过一级评论人，锦囊id拿到二级评论人和二级评论内容
                mm=list(models.review.objects.filter(userid=i['reviewer_id'],content_tips_id_id=id).values('content','reviewer_id').order_by('-uptime'))
                if mm:
                    kkkk = []
                    for i in mm:

                        bbbbbb = []
                        bbbbbb.append({'two':i['content']})
                        bbbbbb.append({'twoname':i['reviewer_id']})
                        kkkk.append(bbbbbb)
                    aaaaaa.append(kkkk)
                else:
                    k=[]
                    bb=[]
                    k.append(bb)
                    aaaaaa.append(k[0])

                cccccc.append(aaaaaa)
            b1.append(cccccc)
            return JsonResponse({'code':b1[0]})

    else:
        return JsonResponse({'code':'token已过期'})



# 书写评论
def writereview(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'])
    cc = json.loads(request.body)['tipname']
    # 如果有内容和锦囊名
    if json.loads(request.body)['tipname'] and json.loads(request.body)['content']:
        content = json.loads(request.body)['content']
        # 拿到分享id
        id = list(models.tips.objects.filter(tip_name=cc).values('id'))[0]['id']
        ff = {
            'content': content,
            'content_tips_id_id': id,
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
        id = list(models.tips.objects.filter(tip_name=cc).values('id'))[0]['id']
        ff = json.loads(request.body)['name']
        content = json.loads(request.body)['content']
        sss = {
            'content': content,
            'userid': ff,
            'content_tips_id_id': id,
            'reviewer_id': decoded['user_id']
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





# 分页
def limit(request):
    return HttpResponse('tips limit')
# 点赞
def approve(request):
    return HttpResponse('tips approve')
