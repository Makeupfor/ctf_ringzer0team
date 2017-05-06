# Encrypted ZIP - Challenge 29

The legacy zip encryption is vulnerable to a known plaintext attack

Use pkcrack to recover the password from the weird.zip file
https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html

1. Zip weird.txt to weirdP.zip (no password)

2. Extract weirdP.zip to weirdP.txt

3. Extract weirdC.zip to weirdC.txt

4. Execute our knownplain text attack: `pkcrack -c weirdC.txt -p weirdP.txt`

5. Decrypt the flag.zip file: `zipdecrypt 3330b3a9 c403beea a0b3129d flag.zip flagP.zip`
