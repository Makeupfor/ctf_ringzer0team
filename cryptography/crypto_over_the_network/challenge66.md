# Crypto over the network - Challenge 66

The server gives us the time it takes to verify the provided password.

After a few tries, I noticed that the server takes > 0.008 seconds when the provided password is exactly 8 characters long versus about 0.00001 seconds on average.

I wrote a script that goes through a character set for every position in the 8 character password, checking if the computation time differs significantly from 0.008 seconds. After checking the first character, I found out that when I hit the letter G the computation time was less than 0.008 seconds, and did some consistently whenever I ran the script multiple times. So I used this value to check if a character is the right one in the password.

```
python challenge66.py
G0OdPwd!
```
