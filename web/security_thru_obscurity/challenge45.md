# Security through obscurity - Challenge 45

There's a cookie called AUTH in this challenge

`Z3Vlc3QsYTgyZDhlM2VhZTExMjk4NCwxNDk0MTA0NDEzLGZhbHNlOjk2ZjhlMDYzODIwYmEzN2EwZTk4NjZhN2VjYmNiMzE3`

When we base64 decode it we get:

`'guest,a82d8e3eae112984,1494104413,false:96f8e063820ba37a0e9866a7ecbcb317'`

Fields:

* guest = username
* a82d8e3eae112984 = password hash? (we don't care about this one)
* 1494104413 = cookie expiry timer
* false = flag is account has admin rights
* 96f8e063820ba37a0e9866a7ecbcb317 = MD5 hash of previous fields

So we just need to change username to admin, set expire > now() and calculate new MD5 hash

Then we just edit our cookie in our browser and refresh the page to get the flag.

[challenge45.py](challenge45.py)
