import flow
remote_url='http://120.197.89.173:8081/openapi/router'
SER_KEY = 'b94f8f0aed8217ad6ddf055056464f96'
DATA_FORMAT = 'json'
appKey = 'iujlzfe1c4'
format='json'
userName = ''
v = '2.0'

params = {'appKey':appKey , 'format':format ,'userName':userName , 'v':v}
print('1111111111',params)

left = flow.flowleft('13428750132', params)
print('2222222222222',params)
print(left)