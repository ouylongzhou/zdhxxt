#coding=utf-8
import base64
import hashlib
import http.client
import requests
import uuid
import time
import json

timestamp = int(time.time())
u1 = uuid.uuid1()
u2 = uuid.uuid1()


def json_md5_base64(timeQuotaJsonList, params1):
    d = dict()
    signKEY = "db290a1b871a4eb589df2a185b21c3d7"
    dataKey = "yu1qoj8kyu1qoj8k"
    timeQuotaJsonList["signkey"] = signKEY
    args1 = json.dumps(timeQuotaJsonList)  # 将dict对象 转换成 string对象
    params = json.dumps(params1)
    m = hashlib.sha256()    # 创建对象
    m.update(args1.encode('utf-8'))  # 生成加密串
    # m.update(params.encode('utf-8'))
    # m.update(signKEY.encode('utf-8'))
    psw1 = m.hexdigest()   # 获取加密串
    s = hashlib.md5()  # md5加密
    s.update(psw1.encode('utf-8'))
    psw = s.hexdigest()
    args2 = base64.b64encode(args1.encode('utf-8'), dataKey.encode('utf-8'))   # base64加密
    d["data"] = args2
    d["sign"] = psw

    print(d)
    return json.dumps(d).encode(encoding='utf-8')


def qingqiu():
    url = "https://tpt.jchl.com"
    headers = {'Content-Type': 'application/json'}
    timeQuotaJsonList = {
            "version": "1", "cusType": "0",
            "cusName": "ouy支付客户", "userId": "8d35e31397254822a39ecd4d781c0e25",
            "taxIdentification": "18899990000", "businessOrderNo": "2018061310091219",
            "channel": "4", "payAmount": "88",
            "goodsSkuId": "25205542045684835", "payRetUrl": "http://www.runoob.com/",
            "payNotifyUrl": "http://www.runoob.com/"}

    params1 = {"appId": "000106", "sessionId": str(u1), "requestId": str(u2), "timestamp": timestamp}
    data = json_md5_base64(timeQuotaJsonList, params1)
    params = {"appId": "000106", "sessionId": u1, "requestId": u2, "timestamp": timestamp, "sign": data["sign"]}

    r = requests.post("POST", "/gateway/ordercenter/outter/orderService/createRewardOrder", json=data["data"], headers=headers, params=params)
    response = r.getresponse()
    result = response.read()
    print(result)


if __name__ == '__main__':

    qingqiu()