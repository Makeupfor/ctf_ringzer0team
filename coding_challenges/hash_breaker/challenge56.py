from hashlib import sha1
from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/56"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN HASH -----<br />\r\n\s+(\w+)<", html).group(1)

    for answer in range(1000, 9999):
        hashed_answer = sha1(str(answer)).hexdigest()
        if hashed_answer == message:
            print("The message is : %s" % message)
            print("The plaintext is : %d" % answer)
            print("The hash plaintext is: %s" % hashed_answer)
            break

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
