#-*- coding:utf-8 -*-
import requests, datetime,os
url = "http://epg.stncp.hz.cz/xml2db.php"

try:
    res = requests.get(url,timeout=300)
    res.encoding = 'utf-8'
    print(res.text)
except Exception as e:
    print("出错了")
