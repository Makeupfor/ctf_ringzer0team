# Hangovers and more bacon - Challenge 114

The cipher used here is the Bacon's cipher:
https://en.wikipedia.org/wiki/Bacon%27s_cipher

With the Bacon's cipher, each letter of the plaintext is substituted with a matching 5 letter "binary code". In this challenge, the "A" values in the code correspond to lowercase letters of the message and 'B' values are the uppercase ones.

I wrote a script that tries both possible variations (ie. upper=A vs. upper=B). We can see that the 2nd message contains our key:

```
python .\challenge114.py
Ciphertext 1: abbaabbaaabbabbbbabababaabbbbbbbaabbabbbabbabbbbbabbbbbbbbabbaaabbaababbbbbbaababbbaababbabbbbbbbbabbababb
bbaabbbbbbaabababbbbbabbbabaaabbabbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
Len: 215
Plaintext: my##u#zxn###rs#s#w##v##sx#un##############

Ciphertext 2: baabbaabbbaabaaaababababbaaaaaaabbaabaaabaabaaaaabaaaaaaaabaabbbaabbabaaaaaabbabaaabbabaabaaaaaaaabaababaa
aabbaaaaaabbababaaaaabaaababbbaabaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Len: 215
Plaintext: theflagisbaconandjackdanielsacaaaaaaaaaaaa
```

[challenge114.py](challenge114.py)