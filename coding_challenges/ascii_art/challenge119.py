from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/119"

    # GET the html page
    html = get(url, cookies=cookies).content

    # Find message in the text
    message = re.search(r"----- BEGIN MESSAGE -----<br />\r\n\s+(.*)", html).group(1)[:-1]
    message = re.sub(r'&nbsp;', ' ', message)
    message = re.sub(r'<br />', '\n', message)
    message = message.split('\n')

    in_number = False
    numbers = []
    i = 0
    number = ""

    # Challenge numbers in ASCII form, without linebreaks
    num1 = ' xx  x x    x    x  xxxxx'
    num2 = ' xxx x   x   xx  x   xxxxx'
    num3 = 'x   x  xx x   x xxx '
    num4 = ' x   xx    x xxxxx     x    x'
    num5 = 'xxxxxx     xxxx    xxxxxx'
    num8 = ' xxx x   x  xx x   x xxx '
    num0 = ' xxx x   xx   xx   x xxx '

    for line in message:
        if in_number:
            if (line and i < 4):
                in_number = True
                number = number + line
                i = i + 1
            elif (line and i == 4):
                numbers.append(number)
                in_number = True
                number = line
                i = 0
            else:
                in_number = False
                i = 0
                numbers.append(number)
                number = ""
        else:
            if (line):
                in_number = True
                i = 0
                number = line

    answer = ""

    for number in numbers:
        if number == num1:
            print('1 - %s' % number)
            answer = answer + '1'
        elif number == num2:
            print('2 - %s' % number)
            answer = answer + '2'
        elif number == num3:
            print('3 - %s' % number)
            answer = answer + '3'
        elif number == num4:
            print('4 - %s' % number)
            answer = answer + '4'
        elif number == num5:
            print('5 - %s' % number)
            answer = answer + '5'
        elif number == num8:
            print('8 - %s' % number)
            answer = answer + '8'
        elif number == num0:
            print('0 - %s' % number)
            answer = answer + '0'
        else:
            print('\'%s\'' % number)

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)


if __name__ == '__main__':
    main()
