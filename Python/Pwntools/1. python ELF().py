from pwn import *

e = ELF('./파일이름') # ex) e = ELF('stack')

#실행 결과는 checksec과 유사하다.