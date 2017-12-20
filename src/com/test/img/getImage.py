#!/use/bin/python3
#coding=utf-8
import re
import urllib.request
import random
import requests

def __openUrl(url):
    try:
        headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
                ]  
        randdom_header = random.choice(headers)  
        req = urllib.request.Request(url)
        req.add_header("User-Agent",randdom_header)  
        req.add_header("Host","www.umei.cc")  
        req.add_header("Referer","http://www.umei.cc/")
        data = urllib.request.urlopen(req).read()
        return data
    except BaseException as e:
        print(e)
def getHtml(url):
    html = __openUrl(url)
    if len(html) > 0:
        html = html.decode('utf-8')
        reg = r'href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"'
        hrefReg = re.compile(reg)
        hrefList = re.findall(hrefReg, html)
        if len(hrefList) > 0:
            for url in set(hrefList):
                print("url=", url)
                if len(html) > 0:
                    html = __openUrl(url)
                    html = html.decode('utf-8')
                    getImage(html)
                  
def getImage(html):
    try:
        reg = r'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imgUrlList = re.findall(imgre, html)
        if len(imgUrlList) > 0:
            x = 0
            for imageUrl in imgUrlList:
                print('图片%d地址:' % x, imageUrl)
                image_name = 'D:\image\%s.jpg' % hash(imageUrl)
                temp_file = open(image_name, 'wb')
                temp_file.write(requests.get(imageUrl).content)
                temp_file.close()
                x += 1
    except BaseException as e:
        print(e)
getHtml("https://www.umei.cc/")