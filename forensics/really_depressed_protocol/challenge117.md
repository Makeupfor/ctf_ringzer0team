# Really depressed protocol - Challenge 117

1. First we need to get the password from that PKCS12 file with crackpkcs12 http://crackpkcs12.sourceforge.net/

2. Open the .pcap in Wireshark and setup SSL decryption
> edit-> preferences -> protocols -> SSL

 > Edit RSA keys list

 > 10.153.108.145,3389,data,cert.pfx,secret

3. Follow the SSL stream of the RDP session (hexdump)
4. Look for keydown events
44 04 00 xx , where xx = scancode

5. If you played NES in the 80's you'll understand what the string is all about (up down up down, etc..)
