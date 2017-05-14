# Look inside the house - Challenge 18

* StegSolver doesn't reveal anything

* binwalk doesn't find anything

* steghide found something:

```
root@kali:~# steghide info 3e634b3b5d0658c903fc8d42b033fa57.jpg
"3e634b3b5d0658c903fc8d42b033fa57.jpg":
  format: jpeg
  capacity: 7.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "flag.txt":
    size: 29.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

Luckily, the file isn't encrypted (empty passphrase)

```
root@kali:~# steghide extract -sf 3e634b3b5d0658c903fc8d42b033fa57.jpg
Enter passphrase:
wrote extracted data to "flag.txt".
root@kali:~# cat flag.txt
FLAG-5jk682************
```
