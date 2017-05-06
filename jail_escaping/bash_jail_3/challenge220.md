# Bash jail 3 - Challenge 220

```
RingZer0 Team Online CTF

BASH Jail Level 3:
Current user is uid=1002(level3) gid=1002(level3) groups=1002(level3)

Flag is located at /home/level3/flag.txt

Challenge bash code:
-----------------------------

WARNING: this prompt is launched using ./prompt.sh 2>/dev/null

# CHALLENGE

function check_space {
        if [[ $1 == *[bdksc]* ]]
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
                output=`$input` &>/dev/null
                echo "Command executed"
        fi
done

-----------------------------
Your input:
```

```
eval $(</home/level3/flag.txt) 2>&0
./real.sh: line 39: FLAG-s9wXyc9WKx1X6N9G68fCR0M78sx09D3j: command not found
Command executed
```
