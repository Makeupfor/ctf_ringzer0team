# File recovery - Challenge 49

Easy one, we have the private key so let's use openssl to decrypt the file:

`openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag.txt`
