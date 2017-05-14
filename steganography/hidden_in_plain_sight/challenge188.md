# Hidden in plain sight - Challenge 188

We can find the original Phrack article at :
http://phrack.org/issues/7/3.html

We'll compare the original file from Phrack against the one provided in the challenge.

1. Take the original file bytes hex values and write them to a file:
> xxd -p original.txt  | fold -w 2 > original`
2. Do the same for the challenge file, we need to get the bytes hex values only, remove spaces and ASCII text to the right:
> cut -c 1-47 new.txt | tr -d ' ' | fold -w 2 > new`
3. Do a diff between the two, don't display identical lines:
> diff -y --suppress-common-lines original new | grep '|'`

```
20							      |	46
69							      |	4c
65							      |	41
69							      |	47
20							      |	2d
2c							      |	4e
20							      |	6f
20							      |	74
20							      |	68
20							      |	69
20							      |	6e
6b							      |	67
74							      |	49
68							      |	73
73							      |	45
62							      |	76
6f							      |	65
68							      |	72
79							      |	57
65							      |	68
68							      |	61
6e							      |	74
77							      |	49
65							      |	74
20							      |	53
72							      |	65
20							      |	65
65							      |	6d
0a							      |	73
```

`464c41472d4e6f7468696e674973457665725768617449745365656d73`

```
python
Python 2.7.10 (default, Feb  6 2017, 23:53:20)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = '464c41472d4e6f7468696e674973457665725768617449745365656d73'
>>> a.decode('hex')
'FLAG-NothingIsEverWhatItSeems'
```
