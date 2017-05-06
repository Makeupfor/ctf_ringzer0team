import binascii
import hashlib
from requests import get
import re

from ctypes import CDLL, c_char_p, c_void_p, memmove, cast, CFUNCTYPE
# https://github.com/F00ker/ringzer0/blob/master/run_shell.py

def run_shellcode(shellcode):
    libc = CDLL('libc.so.6')
    shellcode = shellcode.replace('\\x', '').decode('hex')
    sc = c_char_p(shellcode)
    size = len(shellcode)
    addr = c_void_p(libc.valloc(size))
    memmove(addr, sc, size)
    libc.mprotect(addr, size, 0x7)
    run = cast(addr, CFUNCTYPE(c_void_p))
    run()

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/121"
    html = get(url, cookies=cookies).content
    shellcode = re.search(r"----- BEGIN SHELLCODE -----<br />\r\n\s+(.+)\n", html).group(1)
    a = run_shellcode(shellcode)
    print a

if __name__ == '__main__':
    main()
