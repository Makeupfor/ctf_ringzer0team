import binascii
import hashlib
from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/57"
    html = get(url, cookies=cookies).content
    msg_hash = re.search(r"----- BEGIN HASH -----<br />\r\n\s+(\w+)<", html).group(1)
    msg_salt = re.search(r"----- BEGIN SALT -----<br />\r\n\s+(\w+)<", html).group(1)
    print("Hash: %s" % msg_hash)
    print("Salt: %s" % msg_salt)

    for i in range(0, 999999):
        salted_password = str(i) + msg_salt
        hashed_salted_password = hashlib.sha1(salted_password).hexdigest()
        if hashed_salted_password == msg_hash:
            answer = i
            break

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
