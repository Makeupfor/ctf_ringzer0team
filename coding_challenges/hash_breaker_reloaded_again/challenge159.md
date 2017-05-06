# Hash breaker reloaded again - Challenge 159

This solution brute forces the hash instead of using the services at https://hashkiller.co.uk

Step 1. Generate our rainbow table. Instead of generating one big multi-gigabyte file, let's generate a bunch of files based on the first 4 characters of the hash.
Need to increase ulimit -n 9999 first otherwise we can't open all the files.

``` python
import hashlib
import re

def main():
    charset_small = range(48,58) + range(97,103)
    charset = range(48,58) + range(97,123)    

    # Open hash files (need to increase ulimit first)
    fs = {}
    for f1 in charset_small:
        for f2 in charset_small:
            for f3 in charset_small:
                for f4 in charset_small:
                    bucket = chr(f1) + chr(f2) + chr(f3) + chr(f4)
                    fs[bucket] = open(bucket, 'w')            

    # Build our list of plaintext to bruteforce
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    for e in charset:
                        for f in charset:
                            p = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f)
                            h = hashlib.sha1(p).hexdigest()                            
                            fs[h[:4]].write('%s,%s\n' % (p,h))

    print('Done.')

if __name__ == '__main__':
    main()
```

[challenge159_makelist.py](challenge159_makelist.py)

Step 2. Then just get the hash and lookup it up in our hash files

``` python
from requests import get

import re

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxx")
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
    ```

[challenge159.py](challenge159.py)
