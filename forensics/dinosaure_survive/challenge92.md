# Dinosaure survive - Challenge 92

Nothing found with a simple grep...

```
root@kali:~# grep -i flag 0b02119984a7cee0ba83d55425b9491f.E01

```

.E01 is an Encase file, let's use binwalk to see what's in it.

```
root@kali:~# binwalk 0b02119984a7cee0ba83d55425b9491f.E01

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
89            0x59            Zlib compressed data, default compression
259           0x103           Zlib compressed data, default compression
1557          0x615           Zlib compressed data, default compression
22241         0x56E1          Zlib compressed data, default compression
51869         0xCA9D          Zlib compressed data, default compression
81513         0x13E69         Zlib compressed data, default compression
111259        0x1B29B         Zlib compressed data, default compression
133333        0x208D5         Zlib compressed data, default compression
143974        0x23266         Zlib compressed data, default compression
144620        0x234EC         Zlib compressed data, default compression
145400        0x237F8         Zlib compressed data, default compression
157615        0x267AF         PDF document, version: "1.2"
190387        0x2E7B3         Zlib compressed data, default compression
```

Then look for flags in the extracted files:

```
root@kali:~# cd _0b02119984a7cee0ba83d55425b9491f.E01.extracted/
root@kali:~/_0b02119984a7cee0ba83d55425b9491f.E01.extracted# grep -i flag *
Binary file 601FD matches
Binary file DB405 matches
Binary file DD3F1 matches
```

DB405 contains what we're looking for:

```
root@kali:~/_0b02119984a7cee0ba83d55425b9491f.E01.extracted# xxd DB405
...
00000e10: 6600 6c00 6100 6700 2e00 7400 7800 7400  f.l.a.g...t.x.t.
00000e20: 666c 6167 2d36 6239 3665 3231 3262 3366  flag-6b96e212b3f
00000e30: 3835 3936 3864 6236 3534 6637 3839 3266  85968db654f7892f
00000e40: 3036 3132 3200 0000 ffff ffff 8279 4711  06122........yG.
```
