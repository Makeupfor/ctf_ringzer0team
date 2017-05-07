# Sysadmin part 2 - Challenge 148

We need to find the architect's password.

grep to the rescue!

```
morpheus@forensics:/etc$ grep -s -i architect *
fstab:#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy14QXFXMnlKZzd4UERCV3VlVGdqd05jMW5WWQo="),iocharset=utf8,sec=ntlm  0  0
group:architect:x:1006:
passwd:architect:x:1006:1006::/home/architect:/bin/bash
```

Then just base64 decode the flag.
