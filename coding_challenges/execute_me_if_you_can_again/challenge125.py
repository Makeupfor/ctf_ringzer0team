import binascii
import hashlib
from requests import get
import re
import subprocess

wrapper = '''
char shellcode[] = "{}";

int main(int argc, char **argv) {{
    void (*fp) (void);
    fp = (void *) shellcode;
    fp();
    return 0;
}}
'''
fname = '/tmp/125'

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/125"
    html = get(url, cookies=cookies).content
    shellcode = re.search(r"----- BEGIN SHELLCODE -----<br />\r\n\s+(.+)\n", html).group(1)
    new_shellcode = shellcode[0:248] + shellcode[260:]
    print('Original shellcode:\n%s\n\n' % shellcode)
    print('New shellcode:\n%s\n\n' % new_shellcode)
    with open(fname + '.c', 'wb') as f:
        f.write(wrapper.format(new_shellcode.decode('string_escape')))
    subprocess.call(['gcc', '-z', 'execstack', fname + '.c', '-o', fname])
    out = subprocess.check_output('{} 0>&1'.format(fname), shell=True)

    html = get("%s/%s" % (url, out), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
