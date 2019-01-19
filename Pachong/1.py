from urllib import  request

resp = request.urlopen('https://www.hao123.com')
#print(resp.read())
for i in resp:
    print(i)