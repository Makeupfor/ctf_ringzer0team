from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/32"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN MESSAGE -----<br />\r\n\s+(.+) =", html).group(1)
    param1 = message.split(' ')[0]
    param2 = message.split(' ')[2]
    param3 = message.split(' ')[4]
    print(message)
    print("%d + %d - %d" % (int(param1), int(param2, 16), int(param3, 2)))
    answer = int(param1) + int(param2, 16) - int(param3, 2)

    # Submit the answer
    html = get("%s/%s" % (url, str(answer)), cookies=cookies).content    
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
