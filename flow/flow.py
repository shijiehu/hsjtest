import hashlib,json
import urllib ,urllib.parse,urllib.request
#from urllib.parse import urlparse



remote_url='http://120.197.89.173:8081/openapi/router'
SER_KEY = 'b94f8f0aed8217ad6ddf055056464f96'
DATA_FORMAT = 'json'
appKey = 'iujlzfe1c4'
format='json'
userName = ''
v = '2.0'

params = {'appKey':appKey , 'format':format ,'userName':userName , 'v':v}


def flowleft(code,parmms):
    method = 'iot.member.dataplanleft.query'
    params['method']=method
    #params['msisdn']='13428750132'
    params['msisdn']=code
    sign=getSignKey(params)
    print("sing::::"+sign)
    params['sign']=sign
    print(params)
#requrl = urlparse(remote_url)
    postdata=urllib.parse.urlencode(params)   
    print('2222222222222',postdata)
    header_dict={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    req =urllib.request.Request(url=remote_url,data=postdata.encode(encoding="utf-8",errors="ignore"), headers=header_dict,method='POST')
    f = urllib.request.urlopen(req,timeout=120) 
#req = urllib.request.urlopen(remote_url,data=postdata.encode(encoding="utf-8",errors="ignore"))
    r=json.loads(f.read().decode('utf-8'))

    print(type(r)) 
    print(r)
    if( r['resultCode'] == 0):
        return r['giftLeftCount']
    else:
        print(r)

def  getSignKey( params):
    sign = ''	
    keys = params.keys()
    #sorted(keys ,reverse=True)
    #print('keys sort =====',keys)
    #keylist = [k for k in keys]
    keylist = list(keys)
    keylist.sort()

    print('key sort  ====  ',keylist)
    for key  in keylist:
        sign=sign+key+params[key] 
    print('sign=======',SER_KEY+sign+SER_KEY)       
    return hashlib.sha1((SER_KEY+sign+SER_KEY).encode('utf8')).hexdigest().upper()

#flowleft('13428750132',params)
#postdata = urllib.requrl = remote_urlparse.urlencode(params)
print('-----------------------------------------------------------')





