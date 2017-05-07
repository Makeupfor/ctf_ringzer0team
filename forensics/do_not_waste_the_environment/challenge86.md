# Do not waste the environment - Challenge 86

At first I thought I found something doing a binwalk:

`binwalk 5bd2510a83e82d271b7bf7fa4e0970d1 | grep flag`

```
root@kali:~# binwalk 5bd2510a83e82d271b7bf7fa4e0970d1 | grep flag
37864842      0x241C58A       Unix path: /Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
70637408      0x435D760       Unix path: /Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
77184046      0x499BC2E       Unix path: /Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
90857776      0x56A6130       Unix path: /VirtualBox/GuestInfo/User/flag@flag-PC/UsageState
109416124     0x6858EBC       Unix path: /Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
141426228     0x86DFE34       Unix path: /Users/flag/Desktop/F$L%25A%5EG-5bd2510a83e82d271b7bf7fa4e0970d1.txt
155296650     0x941A38A       Unix path: /Users/flag/Desktop/F$L%25A%5EG-.txt
```

The MD5 hash for `5bd2510a83e82d271b7bf7fa4e0970d1` is : `unautreflag`

I submitted `FLAG-unautreflag` and a couple of variations without any luck.

A simple regex grep was all that was needed:

`strings 5bd2510a83e82d271b7bf7fa4e0970d1 | egrep -i 'f.?l.?a.?g.?-'`

Scrolled through a bunch of pages and found the following:

```
F l a g -=66d7724d872da91af56907aea0f6bfb8
```

Bingo!
