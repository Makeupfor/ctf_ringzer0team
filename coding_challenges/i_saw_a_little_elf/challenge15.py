from requests import get

import bitstring
import os
import re
import subprocess

def main():
    # Get message
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/15"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN Elf Message -----<br />\r?\n?\s+(\S+)<", html).group(1)
    checksum = re.search(r"----- BEGIN Checksum -----<br />\r?\n?\s+(\S+)<", html).group(1)

    # Base64 decode
    while re.search(r'^[a-zA-Z\d+/=]+$', message):
        message = message.decode('base64')

    # Reverse the content
    payload = ''.join(reversed(message))

    # Write out ELF file
    f = open('challenge15', 'wb')
    f.write(payload)
    f.close()

    # Execute it and capture stdout
    answer = subprocess.check_output('./challenge15', shell=True).strip()
    print answer

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
