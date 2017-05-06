from hashlib import sha512
from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/14"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN MESSAGE -----<br />\r\n\s+(\w+)<", html).group(1)
    hex_message = ''
    for i in xrange(0, len(message) - 1, 8):
        a = chr(int(message[i:i+8], 2))
        hex_message = hex_message + a
    
    message_hash = sha512(hex_message).hexdigest()
    print("Hash is: %s" % message_hash)

    # Submit the answer
    html = get("%s/%s" % (url, message_hash), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
