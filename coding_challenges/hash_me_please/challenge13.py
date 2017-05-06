from hashlib import sha512
from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/13"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN MESSAGE -----<br />\s+(\w+)<", html).group(1)
    message_hash = sha512(message).hexdigest()
    print("Hash is: %s" % message_hash)

    # Submit the answer
    html = get("%s/%s" % (url, message_hash), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
