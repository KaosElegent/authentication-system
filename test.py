from os import urandom
import base64
import sys

a = urandom(32)
print(a)

a = a.decode('latin1')
print(type(a))
print(a + "|")

b = a.encode('latin1')
print(type(b))
print(b)

while(True):
    a = base64.b64encode(urandom(32))[:32].decode('utf-8')
    print(len(a) , " & " , sys.getsizeof(a))
    print(a)
    print(a.encode('utf-8'))
