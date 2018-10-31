#!/usr/bin/python
# -*-coding:utf-8-*-

# 秒嘀短信API实现
# Refer to: http://www.miaodiyun.com/doc/guide.html
import http.client
import urllib.parse, hashlib, datetime, time, json, ssl

ssl._create_default_https_context = ssl._create_unverified_context


# import httplib,  #加载模块


# 发送行业短信
def sendIndustrySms(tos, smsContent):
    # 定义账号和密码，开户之后可以从用户中心得到这两个值
    accountSid = '59c162859bdd4b66aac1529bd01c0803'
    acctKey = '1d2fbfa8cca344a9ada5edb9c0584d59'

    # 定义地址，端口等
    serverHost = "api.miaodiyun.com"
    serverPort = 443
    industryUrl = "/20150822/industrySMS/sendSMS"

    # 格式化时间戳，并计算签名
    timeStamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    rawsig = accountSid + acctKey + timeStamp
    m = hashlib.md5()
    m.update(str(rawsig).encode('utf-8'))
    sig = m.hexdigest()

    # 定义需要进行发送的数据表单
    params = urllib.parse.urlencode({'accountSid': accountSid,
                                     'smsContent': smsContent,
                                     'to': tos,
                                     'timestamp': timeStamp,
                                     'sig': sig})
    # 定义header
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

    # 与构建https连接
    conn = http.client.HTTPSConnection(serverHost, serverPort)

    # Post数据
    conn.request(method="POST", url=industryUrl, body=params, headers=headers)

    # 返回处理后的数据
    response = conn.getresponse()
    # 读取返回数据
    jsondata = response.read().decode('utf-8')

    # 打印完整的返回数据
    print(jsondata)

    # 解析json，获取特定的几个字段
    jsonObj = json.loads(jsondata)
    respCode = jsonObj['respCode']
    print("错误码:", respCode)
    respDesc = jsonObj['respDesc']
    print("错误描述:", respDesc)

    # 关闭连接
    conn.close()