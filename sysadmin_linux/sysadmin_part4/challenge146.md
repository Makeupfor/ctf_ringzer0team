# Sysadmin part 4 - Challenge 146

Let's try to find oracle's files... nothing too interesting here

```
morpheus@forensics:~$ find / -user oracle 2>&1 | grep -v "Permission denied"
/var/mail/oracle
/run/screen/S-oracle
find: `/proc/2387/task/2387/fd/5': No such file or directory
find: `/proc/2387/task/2387/fdinfo/5': No such file or directory
find: `/proc/2387/fd/5': No such file or directory
find: `/proc/2387/fdinfo/5': No such file or directory
/home/oracle
```

grep reveals something interesting:

```
morpheus@forensics:/var$ grep -iR oracle * 2>&1 | grep -v "Permission denied"
...
tmp/home/oracle/.ssh/authorized_keys:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoEgxjSM+zh29CqzIet5hxwI4gwWsHL56XlN3xM1zylCog02tZJ5/EA17hvQRoBmh+9lsEaseKnIHpf4WC6BdirAHS56bTq5Mach0cBnIdXogT1/+EsKb72dY4l9S880VsxoiLO/MxWE7oZMbLEnzOH8BJBdgEdLPI7GSaoMsHvMW17IkXuG/qzpbbROamOExC04LSZjCfrhkKxWLZ3Vzu0WLDftw661PUt9lpoBQEjB2m8voEWOqk2THPCbXTl4VMO3hZk0o5n2c6ezXwwcEcU5eTxaADELqCq0TaCvtxMFmxvC+Neu17yhO0BYK/dgdIQIf3U3MTcMpWS0LCvVuN oracle@forensics
tmp/home/oracle/.ssh/id_rsa.pub:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoEgxjSM+zh29CqzIet5hxwI4gwWsHL56XlN3xM1zylCog02tZJ5/EA17hvQRoBmh+9lsEaseKnIHpf4WC6BdirAHS56bTq5Mach0cBnIdXogT1/+EsKb72dY4l9S880VsxoiLO/MxWE7oZMbLEnzOH8BJBdgEdLPI7GSaoMsHvMW17IkXuG/qzpbbROamOExC04LSZjCfrhkKxWLZ3Vzu0WLDftw661PUt9lpoBQEjB2m8voEWOqk2THPCbXTl4VMO3hZk0o5n2c6ezXwwcEcU5eTxaADELqCq0TaCvtxMFmxvC+Neu17yhO0BYK/dgdIQIf3U3MTcMpWS0LCvVuN oracle@forensics
```

Let's check that directory:

```
morpheus@forensics:/var$ ls -la tmp/home/oracle/.ssh
total 20
drwx------ 2 morpheus morpheus 4096 Mar 12  2014 .
drwxr-x--- 3 morpheus morpheus 4096 Sep 15  2014 ..
-rw-r----- 1 morpheus morpheus  398 Mar 12  2014 authorized_keys
-rw------- 1 morpheus morpheus 1679 Mar 12  2014 id_rsa
-rw-r----- 1 morpheus morpheus  398 Mar 12  2014 id_rsa.pub
```

Sweet, the oracle left a backup of her private key in there, let's use it to ssh and get access to oracle's account.

```
morpheus@forensics:/var$ ssh -l oracle -i /var/tmp/home/oracle/.ssh/id_rsa 1.3.3.6
Could not create directory '/home/morpheus/.ssh'.
The authenticity of host '1.3.3.6 (1.3.3.6)' can't be established.
ECDSA key fingerprint is 6b:f4:cd:30:7d:04:6a:98:07:4c:6d:e6:85:19:52:59.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/morpheus/.ssh/known_hosts).

You have mail.
Last login: Sun Apr  9 02:54:28 2017 from 47.185.146.234
oracle@forensics:~$
```

```
oracle@forensics:~$ ls
encflag.txt.enc  flag.txt
```

Bingo!
