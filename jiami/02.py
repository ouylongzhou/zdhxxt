import requests
import hashlib

def login():
    url = 'https://smini.leyaoyao.com/customer/login'
    a = '84424368'
    s = hashlib.md5()  # md5加密
    s.update(a.encode('utf-8'))
    passw = s.hexdigest()
    print(passw)
    payload = {'username': 'orTHPwjv2pf4n1yINS8FPOHuHeD4', 'password': passw,'equipmentId':'12200412'}

    r = requests.get(url=url,params=payload)

    print(r.text)

login()
