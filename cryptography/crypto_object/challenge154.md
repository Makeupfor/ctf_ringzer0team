# Crypto object - Challenge 154

The message is: `GMODCDOOKCDBIOYDRMKDPQLDPVWYOIVRVSEOV`

This looks like a Scytale cipher because of the strip of plastic in the picture.

https://en.wikipedia.org/wiki/Scytale

But we don't see all letters of FLAG in the string. It's probably encoded with ROT13 or other rotation count. Let's try all possible rotations, and for each we will try to decode the message using all possible keys for that message length.

```
FLAG letters found in WCETSTEEASTRYEOTHCATFGBTFLMOEYLHLIUEL
        WCETSTEEASTRYEOTHCATFGBTFLMOEYLHLIUEL
        WTCFEGTBSTTFELEMAOSETYRLYHELOITUHECLA
>>>>> WELCOMETOTHESCYTALETHEFLAGISBUTTERFLY <<<<<
        WTTECRFYEYGLTEBHSOTLTTFIEHLUECMEAAOLS
        WAHTLCSCFHETALLTRTMISYFOUTEGEEEOBYLET
```


[challenge154.py](challenge154.py)
