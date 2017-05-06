from hashlib import sha512
from requests import get
import re

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/16"
    html = get(url, cookies=cookies).content
    message_base64 = re.search(r"----- BEGIN CRYPTED MESSAGE -----<br />\r?\n?\s+(\S+)<", html).group(1)
    bigkey = re.search(r"----- BEGIN XOR KEY -----<br />\r?\n?\s+(\S+)<", html).group(1)
    message = message_base64.decode('base64')

    print("base64 encoded message: %s" % message_base64)
    print("key message: %s " % bigkey)

    for i in range (0, len(bigkey) - 9):
        shortkey = bigkey[i:i+10]
        fullkey = shortkey * 3 + shortkey[0:2]
        a = bytearray(message)
        b = bytearray(fullkey)
        c = bytearray(32)

        for j in range(0, 32):
            c[j] = a[j] ^ b[j]

        message_xored = str(c)
        if message_xored.isalnum():
            answer = message_xored
            print("answer is key: %s" % answer)
            break

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
