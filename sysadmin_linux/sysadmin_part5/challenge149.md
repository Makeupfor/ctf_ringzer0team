# Sysadmin part 5 - Challenge 149

To gain access to the oracle account, we'll login as morpheus then ssh using the oracle's private key from the previous challenge.

Checking all files in oracle's home directory, we find the following shell alias in .bashrc:

`alias reveal="openssl enc -aes-256-cbc -a -d -in encflag.txt.enc -k 'lp6PWgOwDctq5Yx7ntTmBpOISc'"`

```
oracle@forensics:~$ reveal
FLAG-IaFOjjFWazycSg0lbVO3T8ZTvz
```
