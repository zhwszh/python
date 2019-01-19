from urllib import request,parse

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false'

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=?labelWords=hot'
}

data = {
    'first':'true',
    'pn':1,
    'kd':'java'

}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST',)
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))