from django.test import TestCase
import json
from . import models
# Create your tests here.

def loadFont():
    f = open("2.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    family = setting['RECORDS']  #注意多重结构的读取语法
    print(family)
    cc=[]
    for i in family:
        print(i)
        models.user.objects.create(**i)
        cc.append(i)
    print(cc)

    # return family

t = loadFont()

# print(t)
