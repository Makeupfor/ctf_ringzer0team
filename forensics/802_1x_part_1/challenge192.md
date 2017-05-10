# 802.1 part 1 - Challenge 192

The goal here is to find the RADIUS shared secret.

Because we have Accounting-Request messages in the capture, we can try to bruteforce the RADIUS secret more easily.

According to RFC 2866:

> The NAS and RADIUS accounting server share a secret.  The Request Authenticator field in Accounting-Request packets contains a one-way MD5 hash calculated over a stream of octets consisting of the Code + Identifier + Length + 16 zero octets + request attributes + shared secret (where + indicates concatenation).  The 16 octet MD5 hash value is stored in the Authenticator field of the Accounting-Request packet.

__RequestAuth = MD5(Code + ID + Length + 16 zero octets + Attributes + Secret)__

We have all the required data to beging bruteforcing the shared secret.

First, we need to zero out the authenticator field off that first packet, the data is now:

```
'04c5017400000000000000000000000000000000011341525542414e4554574f524b535c72616f0406c0a80a010506000000003d06000000132c1f41525542414e45543130304241393642363139382d3535363031413133370655601aa532193130304241393642363139382d303030303030303030340806c0a80a9f1f0e3130304241393642363139381e0e303030423836423836313230193a48cd2fc61c604eb0858987ac517fcdf8b90b0000000000005230303030303031332d30312d353535666232646400000000000000000000002906000000001a1b000039e7051552616f206c696b6573203158204d6f766965731a19000039e7061330303a30623a38363a63663a65323a31361a0f000039e70a0964656661756c741a15000039e7010f61757468656e746963617465641a0c000039e70206000000011a0d000039e70c0757696e20372806000000022a06000084db2b060000ab482f060000010e3006000000c331060000000a2e0600000092'
```

Then we just need to concatenate each word off our wordlist to the end of the RADIUS payload, MD5 the whole thing and compare the result against the MD5 present in the original authenticator field.

```
$ python challenge192.py
Authenticator field from the pcap: d936fe3ccbe8e7a79f58a19a6adf26f3
Hash length: 32
RADIUS message to be prefixed to the secret: 04c5017400000000000000000000000000000000011341525542414e4554574f524b535c72616f0406c0a80a010506000000003d06000000132c1f41525542414e45543130304241393642363139382d3535363031413133370655601aa532193130304241393642363139382d303030303030303030340806c0a80a9f1f0e3130304241393642363139381e0e303030423836423836313230193a48cd2fc61c604eb0858987ac517fcdf8b90b0000000000005230303030303031332d30312d353535666232646400000000000000000000002906000000001a1b000039e7051552616f206c696b6573203158204d6f766965731a19000039e7061330303a30623a38363a63663a65323a31361a0f000039e70a0964656661756c741a15000039e7010f61757468656e746963617465641a0c000039e70206000000011a0d000039e70c0757696e20372806000000022a06000084db2b060000ab482f060000010e3006000000c331060000000a2e0600000092
Length of RADIUS message: 372
Cracking using: dictionary_english.dic
Cracking using: dictionary_huge_0.dic
Cracking using: dictionary_huge_1.dic
Cracking using: dictionary_huge_2.dic
Cracking using: dictionary_huge_3.dic
Cracking using: dictionary_huge_4.dic
Cracking using: dictionary_huge_5.dic
Cracking using: dictionary_huge_6.dic
Cracking using: dictionary_huge_7.dic
Cracking using: dictionary_huge_8.dic
Cracking using: dictionary_huge_9.dic
Cracking using: dictionary_huge_a.dic
Cracking using: dictionary_huge_b.dic
Cracking using: dictionary_huge_c.dic
Cracking using: dictionary_huge_d.dic
Cracking using: dictionary_huge_e.dic
Cracking using: dictionary_huge_g.dic
Cracking using: dictionary_huge_h.dic
Cracking using: dictionary_huge_j.dic
Cracking using: dictionary_huge_k.dic
Found it! --> karaoke
```

[challenge192.py](challenge192.py)
