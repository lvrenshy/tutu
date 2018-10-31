from django.shortcuts import render
# Create your views here.
from datetime import datetime
import json
import math
import jwt
from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect,reverse
from . import models
# Create your views here.
def show(request):
    with open("question/answer.json",encoding='utf-8') as fp:
        data=json.load(fp)
    for i in data:
        print(i)
        models.answer.objects.create(**i)
    return HttpResponse("OK")
    # return HttpResponse('show share')
# 按条件搜索问答详细信息（还未分页）
def search(request):
    len = models.question.objects.count()
    l = math.ceil(len / 3)
    if not request.body:
        bb = []
        a1 = []
        ff = list(models.question.objects.filter(id__in=[1,2,3]).values('question_id'))
        for i in ff:
            # t_name=list(models.question.objects.filter(question_id=i["question_id"]).values('launch_user_id'))[0]
            aa=list(models.question.objects.filter(question_id=i['question_id']).values('content'))[0]
            # print(aa,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            # bb=list(models.answer.objects.filter(question_id_id=i['question_id']).values('answser_user_id'))[0]
            cc=list(models.answer.objects.filter(question_id_id=i['question_id']).values('content'))[0]
            print(cc,'ccccccccccccccccccccccccccccccccccccccc')
            # a1.append(t_name)
            aa['question_content']=aa.pop('content')
            a1.append(aa)
            # a1.append(bb)
            cc['answer_content']=cc.pop('content')
            a1.append(cc)
        ll = {'page': l}

        bb.append(a1)
        print(bb,'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        bb.append(ll)
        print(bb)
        return JsonResponse({"acount": bb})
    else:
        bb = []
        a1 = []
        ff = list(models.question.objects.values('question_id'))
        page = int(json.loads(request.body)['page'])
        for i in range((page - 1) * 3, page * 3):
            aa = list(models.question.objects.filter(question_id=ff[i]['question_id']).values('content'))[0]
            cc = list(models.answer.objects.filter(question_id_id=ff[i]['question_id']).values('content'))[0]
            aa['question_content'] = aa.pop('content')
            a1.append(aa)
            cc['answer_content'] = cc.pop('content')
            a1.append(cc)
        ll = {'page': l}

        bb.append(a1)
        print(bb, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        bb.append(ll)
        print(bb)
        return JsonResponse({"acount": bb})
# 查看问题的详细内容
def questioninfo(request):
    aa=[]
    question=json.loads(request.body)
    question_content=question['content']

    # 查出问题的内容，提出问题的人
    qq=list(models.question.objects.filter(content=question_content).values('content','launch_user_id'))
    for i in qq:
        aa.append(i)
    print(list(qq))
    # 查出问题id
    q_id=models.question.objects.filter(content=question_content).values('id')
    print(list(q_id))
    question_id_id=list(q_id)[0]['id']
    answer_content=list(models.answer.objects.filter(question_id_id=question_id_id).values('content'))
    for i in answer_content:
        aa.append(i)



    return JsonResponse({'code':aa})

#展示最新问题(带分页-------------------------------------------------)
def showQuestion(request):
    bb = []
    a1 = []
    aa=[]
    len = models.question.objects.count()
    # 拿到问题页数。一页显示三个
    l = math.ceil(len / 3)
    # 拿到前三条的问题id
    ff = list(models.question.objects.values('spare1'))
    print(ff)
    # if not request.body:
    #     for i in ff:
    #         a1.append(i['spare1'])
    #     a1.sort()
    #     ll = {'page': l}
    #     a1.reverse()
    #     for i in range(0,3):
    #         vv=list(models.question.objects.filter(spare1=a1[i]).values('content','spare1','launch_user_id'))
    #         # 此处spare1是"2018-10-15 11:13:50.601522"的，如何展示需商榷
    #         bb.append(vv[0])
    #
    #     bb.append(ll)
    #     # print(bb)
    #     return JsonResponse({"acount": bb})
    # else:
    #     # 拿到前台传过来的页码
    page=int(json.loads(request.body)['page'])
    for i in ff:
        a1.append(i['spare1'])
    a1.sort()
    ll = {'page': l}
    a1.reverse()
    print(111111111111111111111111111111)
    for i in range((page-1)*3,page*3):
        # 拿到问题内容
        print(222222222222222222222222222222222222222222222222222222)
        vv=list(models.question.objects.filter(spare1=a1[i]).values('content'))
        # 此处spare1是"2018-10-15 11:13:50.601522"的，如何展示需商榷
        acc = list(models.question.objects.filter(spare1=a1[i]).values('question_id'))
        print(acc,33333333333333333333333333333333333333333333333333333333333333)
        abb=list(models.answer.objects.filter(question_id_id=acc[0]['question_id']).values('content'))
        bb.append({'question_content':vv[0]['content']})
        if abb:

            bb.append({'answer_content':abb[0]['content']})
        else:
            bb.append({'answer_content':''})
    print(33333333333333333333333333333333333333333333333333333333333333)

    aa.append(bb)
    aa.append(ll)
    # print(bb)
    return JsonResponse({"acount": aa})



# 查看未解决问题(带分页------------------)
def waitquestion(request):

    a1 = []
    len = models.question.objects.filter(question_style_id=1).count()
    # 拿到未问题页数。一页显示三个
    l = math.ceil(len / 3)
    # ff是未解决问题和提问人的字典列表
    ff = list(models.question.objects.filter(question_style_id=1).values('content'))
    # if request.body:
    #     page=int(json.loads(request.body)['page'])
    #     if page==1:
    #         bb = []
    #         for i in range(0,3):
    #             a1.append(ff[i])
    #         ll = {'page': l}
    #         bb.append(a1)
    #         # print(bb, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #         bb.append(ll)
    #         # print(bb)
    #         return JsonResponse({"acount": bb})
    #     else:
    #         for i in range((page-1)*3,page*3):
    #             bb = []
    #             a1.append(ff[i])
    #             ll = {'page': l}
    #             bb.append(a1)
    #             # print(bb, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #             bb.append(ll)
    #             # print(bb)
    #             return JsonResponse({"acount": bb})
    # else:

    bb = []
    for i in range(0, 3):
        a1.append({'question_content':ff[i]['content']})
        a1.append({'answer_question':''})
    ll = {'page': l}
    bb.append(a1)
    # print(bb, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    bb.append(ll)
    # print(bb)
    return JsonResponse({"acount": bb})

#查看答案
def showAnswer(request):
    return HttpResponse('show answer')
#问题分页
def queLimit(request):
    return HttpResponse('show question in limit')
#答案分页
def ansLimit(request):
    return HttpResponse('show answer in limit')
#提出问题
def ask(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        ss = json.loads(request.body)
        cc=models.question.objects.count()
        ab = {
            'spare1': datetime.now(),
            'question_style_id':1,
            'content': ss['content'],
            'launch_user_id': decoded['user_id'],
            'question_id':cc+1
        }
        models.question.objects.create(**ab)
        return JsonResponse({'code': '成功哦'})
    else:
        return JsonResponse({'code': 'token过期'})
#回答问题
def answer(request):
    asd = request.META.get("HTTP_TOKEN")
    SECRET_KEY = '123456'
    # 将headers中的token进行解密
    decoded = jwt.decode(asd, SECRET_KEY, audience='webkit', algorithms=['HS256'], options={'verify_exp': True})
    if decoded:
        name=decoded['user_id']
        ss=json.loads(request.body)['content']
        s2=json.loads(request.body)['answercontent']
        check=list(models.question.objects.filter(content=ss).values('question_id'))[0]['question_id']
        aa={
            'content':s2,
            'answser_user_id':name,
            'question_id_id':check
        }
        models.answer.objects.create(**aa)
        return JsonResponse({'code':'成功哦'})
    else:
        return JsonResponse({'code':'token过期'})



# 建表
def jianbiao(request):
    with open("question/answer.json",encoding='utf-8') as fp:
        data=json.load(fp)

    for i in data:
        print(i)
        models.answer.objects.create(**i)
    return HttpResponse("OK")
