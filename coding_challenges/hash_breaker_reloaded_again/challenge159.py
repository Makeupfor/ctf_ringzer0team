import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/159"
    
    print('Getting hash from challenge webpage...')
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN HASH -----<br />\s+(\w+)<", html).group(1)
    print('Hash is: %s' % message)

    f = open(message[:4])
    lines = f.read().splitlines()
    for line in lines:
        if re.search(message, line):
            answer = line.split(',')[0]    
   
    # Submit the answer
    print('Submitting answer to challenge page...')
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()