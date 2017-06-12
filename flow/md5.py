import hashlib
print('-----------------------------------------------------------')
m = hashlib.md5()   #创建hash对象，md5:(message-Digest Algorithm 5)消息摘要算法,得出一个128位的密文
print( m )             #<md5 HASH object @ 000000000254ADF0>
m.update('BeginMan'.encode('utf8'))#更新哈希对象以字符串参数
print( m.digest().decode )   #返回摘要，作为二进制数据字符串值
print( m.hexdigest() )#返回十六进制数字字符串    0b28251e684dfbd9102f8b6f0281c0c5
print( m.digest_size )#16
print( m.block_size ) #64
a = 'BeginMan国家'
b = a.encode('utf8')
c = b.decode()
print(a.encode('utf8'))
print(b)
print('1111111111'+c)
a = "a test string".encode('utf8')  
print('md5     '+hashlib.md5(a).hexdigest() )
#print( hashlib.sha1(a)   )
print( 'sha1     '+hashlib.sha1(a).hexdigest()   )
print( 'sha224     '+hashlib.sha224(a).hexdigest()  ) 
print( 'sha256     '+hashlib.sha256(a).hexdigest()   )
print( 'sha384     '+hashlib.sha384(a).hexdigest()   )
print( 'sha512     '+hashlib.sha512(a).hexdigest())