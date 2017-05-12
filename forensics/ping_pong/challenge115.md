# Ping pong - Challenge 115

The interesting part in those ICMP packets is the payload, something's probably hidden in there.

We'll extract the data field using:

`tshark -r 1d807df224db41d7c3808e76c49d4b7a.pcap -T fields -e data 'icmpv6.type==128 && frame.len > 62' > icmp.txt`

Then do the following:
1. Remove the newlines
2. Convert hexdump to binary
3. Base64 decode it
4. Write the output to a new file

`tr -d "\n" < icmp.txt | xxd -r -p | base64 -D > icmp`

That challenge is worth 5 points so we probably won't be able to find the flag easily with strings...

```
root@kali:~# file icmp
icmp: data
root@kali:~# strings icmp | grep -i flag
/Flags 4

root@kali:~# binwalk icmp

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
862           0x35E           Zlib compressed data, default compression
4345          0x10F9          Zlib compressed data, default compression
24966         0x6186          Zlib compressed data, default compression
```

```
root@kali:~# strings icmp
nnot
/Subtype /Link
/Border [0 0 0]
/Rect [72 687.75 180.75 701.25]
/A <</Type /Action
/S /URI
/URI (https://www.google.com/url?q=https%3A%2F%2Fwiki.nsec.io%2Findex.php%2FComrade_Rausczek&sa=D&sntz=1&usg=AFQjCNHQpEkyInDvn0K8HWCQVEKxuW8LyA)
>> <</Type /Annot
/Subtype /Link
/Border [0 0 0]
/Rect [380.25 664.5 531 680.25]
/A <</Type /Action
/S /URI
/URI (https://www.google.com/url?q=https%3A%2F%2Fwiki.nsec.io%2Findex.php%2FDemokratik_Republik_of_Auskev&sa=D&sntz=1&usg=AFQjCNHJ3P3fF0ZXaHOHSsKWONo8B4k0_g)
>> <</Type /Annot
/Subtype /Link
/Border [0 0 0]
/Rect [72 645.75 114 659.25]
/A <</Type /Action
/S /URI
/URI (https://www.google.com/url?q=https%3A%2F%2Fwiki.nsec.io%2Findex.php%2FDemokratik_Republik_of_Auskev&sa=D&sntz=1&usg=AFQjCNHJ3P3fF0ZXaHOHSsKWONo8B4k0_g)
/Contents 6 0 R
endobj
6 0 obj
<</Filter /FlateDecode
/Length 2271
```

I tried the URLs above but the webpage is protected.

Then I used peepdf to dig into the PDF:

`peepdf -i -f /root/icmp.pdf`

```
peepdf -i -f /root/icmp.pdf
Warning: PyV8 is not installed!!

File: icmp.pdf
MD5: 1f0f41595011d546e0d3a49ceae963a5
SHA1: 97d996706a9e7b679e95cf2952e1d478340c0f3c
Size: 25653 bytes
Version:
Binary: False
Linearized: False
Encrypted: False
Updates: 0
Objects: 8
Streams: 3
Comments: 0
Errors: 2

Version 0:
	Catalog: 2
	Info: No
	Objects (8): [1, 4, 5, 6, 7, 8, 9, 10]
	Streams (3): [6, 10, 8]
		Encoded (3): [6, 10, 8]
```

After googling how PDF work (http://www.adobe.com/content/dam/Adobe/en/devnet/acrobat/pdfs/pdf_reference_1-7.pdf), I was able to determine that stream 6 contains the text we are probably looking for:

```
PPDF> stream 6
<...>
/F0 16 Tf
1 0 0 -1 96 112 Tm
<0059> Tj
1 0 0 -1 106.1875 112 Tm
<0059> Tj
1 0 0 -1 116.375 112 Tm
<0059> Tj
1 0 0 -1 126.5625 112 Tm
<0059> Tj
1 0 0 -1 136.75 112 Tm
<0003> Tj
1 0 0 -1 141.4375 112 Tm
<000E> Tj
1 0 0 -1 150.7031 112 Tm
<001A> Tj
1 0 0 -1 160.5703 112 Tm
<0019> Tj
1 0 0 -1 170.6172 112 Tm
<0011> Tj
1 0 0 -1 180.3047 112 Tm
<...>
```

The hex string preceding the Tj command is the character that's rendered by the PDF. Unfortunately to make this more complicated for us, there is a ToUnicode cmap in there. We'll need to take our Tj commands and translate the string to get the unicode value that'll hopefully will reveal the flag.

```
PPDF> stream 8

/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo
<<  /Registry (Adobe)
/Ordering (UCS)
/Supplement 0
>> def
/CMapName /Adobe-Identity-UCS def
/CMapType 2 def
1 begincodespacerange
<0000> <FFFF>
endcodespacerange
10 beginbfchar
<0003> <0020>
<000C> <0041>
<0014> <0049>
<0017> <004C>
<001D> <0052>
<001F> <0054>
<0056> <003A>
<0059> <003D>
<016F> <002C>
<0170> <002E>
endbfchar
6 beginbfrange
<0005> <0007> <0033>
<000E> <0011> <0043>
<0019> <001A> <004E>
<0026> <0035> <0061>
<0037> <003C> <0072>
<003E> <003F> <0079>
endbfrange
endcmap
CMapName currentdict /CMap defineresource pop
end
end
```

The cmap is divided in two parts, the beginbfchar translate values directly, while beginbfrange as the name implies translates a range. For example 000E -> 0043, 000F -> 0044, etc. At first I didn't translate correctly, I translated the whole range to one single value so my output has some valid bits of strings in there but most of it was incorrect.

So now we have all the information we need to write a script:

```
$ python challenge115.py
==== CONFIDENTIAL====Comrade Rausczek, our honorary allies have found the source of the leaks. This person is currently under protection of the Demokratik Republik of Auskev, but we are working diplomatically to resolve the matter.Flag: sasdhbds********redacted*******==== CONFIDENTIAL====
```


[challenge115.py](challenge115.py)
