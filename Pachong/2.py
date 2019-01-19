from urllib import request
from urllib import parse
params = {'name':'张三','age':'18','greet':'hello world'}
result = parse.urlencode(params)
print(result)