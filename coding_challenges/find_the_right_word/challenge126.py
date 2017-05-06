from requests import get
import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/126"
    html = get(url, cookies=cookies).content
    message = re.search(r"----- BEGIN WORDS -----<br />\r?\n?\s+(\S+)<", html).group(1)
    words = message.split(',')
    words_shuffled = []

    print('Original message: %s' % message)

    # Use a wordlist
    f = open('words0.txt')
    wordlist = f.read().splitlines()

    for word in words:
        try:
            wordlist.index(word)
        except ValueError:
            words_shuffled.append(word)

    for word in words_shuffled:
        word_sorted = ''.join(sorted(word))
        for i in wordlist:
            if word_sorted == ''.join(sorted(i)):
                message = re.sub(word, i, message)
                break

    print('New message: %s' % message)

    # Submit the answer
    html = get("%s/%s" % (url, message), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)

if __name__ == '__main__':
    main()
