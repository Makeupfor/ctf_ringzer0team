# Sysadmin part 1 - Challenge 89

We need to find trinity's password.

The flag is located in the arguments of a running program.

```
morpheus@forensics:~$ ps aux | grep trinity
morpheus  1284  0.0  0.0   7840   868 pts/3    S+   19:40   0:00 grep trinity
root      3241  0.0  0.0   4188   572 ?        S    Jan14   1:27 /bin/sh /root/backup.sh -u trinity -p Flag-08grILsn3ekqhDK7cKBV6ka8B
```
