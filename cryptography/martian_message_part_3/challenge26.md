# Martian message part 3 - Challenge 26.md

First, let's base64 decode the string:

`'RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'.decode('base64')`

Encrypted flag: `EOBD.7igq4;1ikb51ibOO0;:41R`

The first 4 characters are probably FLAG so let's try to find the key by XORing each byte until we have a match.

The key is 0x3, let's use it to decode the rest of the string.

[challenge26.py](challenge26.py)
