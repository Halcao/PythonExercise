#-*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
from PIL import Image
import pytesseract

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

heads = {
    "Host": "e.tju.edu.cn",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8, image/webp,image/*,*/*;q=0.8",
    "Referer": "http://e.tju.edu.cn/Main/toModule.do?prefix=/Main&page=/logon.jsp",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive" #,
    #"Cookie": "sto-id-20480=BCACBDKMFAAA; Hm_lvt_75e8911b43317c26613c85fce12b7cb3=1487666277; JSESSIONID=6Kxfzr0HxXJGPPrsvOWjOg-iMoPcNasuTc3xlSx6h55xAfCHoOH3!1626549902; Hm_lpvt_75e8911b43317c26613c85fce12b7cb3=1487666277"
}

req = urllib2.Request(
    url="http://e.tju.edu.cn",
    headers=heads
)

result = opener.open(req)

sid = str(result.headers['Set-Cookie'])[11:43]

#print sid
print result.headers


sto = ''
for c in cookie:
    if c.name == "sto-id-20480":
        print c.value
        sto = c.value

heads = {
        "Host": "e.tju.edu.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36X-DevTools-Emulate-Network-Conditions-Client-Id: F9D9B2CE-B532-49A2-8676-38481A9C94A5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8, image/webp,image/*,*/*;q=0.8",
        "Referer": "http://e.tju.edu.cn/Main/toModule.do?prefix=/Main&page=/logon.jsp",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control" : "	max-age=0",
        "Connection": "keep-alive",  # ,
        "Cookie": "sto-id-20480=" + sto + "; JSESSIONID=" + sid
}

req = urllib2.Request(
    url="http://e.tju.edu.cn/Main/toModule.do?prefix=/Main&page=/logon.jsp",
    headers=heads
)

result = opener.open(req)
print result.headers
print cookie
str = result.read()
#
print str

def get_file(url):
    try:
        req = urllib2.Request(url, headers=heads)
        operate = opener.open(req)
        data = operate.read()
        #print data
        return data
    except BaseException, e:
        print e


def save_file(path, file_name, data):
    if data == None:
        print "nil data"
        return

    if (not path.endswith("/")):
        path = path + "/"
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()
    file.close()


CAPTCHA_ADDRESS = 'http://e.tju.edu.cn/Kaptcha.jpg'
LOGIN_ADDRESS = 'http://e.tju.edu.cn/Main/logon.do'

path = "./"
#get_file(CAPTCHA_ADDRESS)
filedata = get_file(CAPTCHA_ADDRESS)
save_file(path, "1.jpg", filedata)

# img = Image.open('./123.jpg')
# cap = pytesseract.image_to_string(img)
# print cap
#
# postdata = urllib.urlencode({
#     'uid': '3015204064',
#     'password': 'nyz1500',
#     'captchas': cap
# })
#
# req = urllib2.Request(
#     url=LOGIN_ADDRESS,
#     data=postdata,
#     headers=heads
# )
#
# result = opener.open(req)
# str = result.read()
#
# print str