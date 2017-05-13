# PHP jail 3 - Challenge 225

```
RingZer0 Team Online CTF

PHP Jail Level 3:
Current user is uid=1002(level3) gid=1002(level3) groups=1002(level3)

Flag is located at /home/level3/flag.txt

Challenge PHP code:
-----------------------------

WARNING: the PHP interpreter is launched using php -c php.ini jail.php.
The php.ini file contain "disable_functions=exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,readfile,require,require_once,include,include_once,file"

<?php
array_shift($_SERVER['argv']);
$var = implode(" ", $_SERVER['argv']);

if($var == null) die("PHP Jail need an argument\n");

function filter($var) {
        if(preg_match('/(`|\.|\$|\/|a|c|s|require|include)/i', $var)) {
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

-----------------------------
Your input:
```

This time we can't use popen but we can use highlight_file(). However we can't open flag.txt directly because of the filter. We'll use glob with a regex to work our way around the filter:

```
Your input:
highlight_file(glob('fl*')[0]);
<code><span style="color: #000000">
FLAG-D6jg92*************<br /></span>
</code>Command executed
```
