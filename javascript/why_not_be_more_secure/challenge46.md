# Why not be more secure? - Challenge 46

``` js
// Look's like weak JavaScript auth script :)
$(".c_submit").click(function(event) {
	event.preventDefault();
	var u = $("#cpass").val();
	var k = $("#cuser").val();
	var func = "\x2B\x09\x4A\x03\x49\x0F\x0E\x14\x15\x1A\x00\x10\x3F\x1A\x71\x5C\x5B\x5B\x00\x1A\x16\x38\x06\x46\x66\x5A\x55\x30\x0A\x03\x1D\x08\x50\x5F\x51\x15\x6B\x4F\x19\x56\x00\x54\x1B\x50\x58\x21\x1A\x0F\x13\x07\x46\x1D\x58\x58\x21\x0E\x16\x1F\x06\x5C\x1D\x5C\x45\x27\x09\x4C\x1F\x07\x56\x56\x4C\x78\x24\x47\x40\x49\x19\x0F\x11\x1D\x17\x7F\x52\x42\x5B\x58\x1B\x13\x4F\x17\x26\x00\x01\x03\x04\x57\x5D\x40\x19\x2E\x00\x01\x17\x1D\x5B\x5C\x5A\x17\x7F\x4F\x06\x19\x0A\x47\x5E\x51\x59\x36\x41\x0E\x19\x0A\x53\x47\x5D\x58\x2C\x41\x0A\x04\x0C\x54\x13\x1F\x17\x60\x50\x12\x4B\x4B\x12\x18\x14\x42\x79\x4F\x1F\x56\x14\x12\x56\x58\x44\x27\x4F\x19\x56\x49\x16\x1B\x16\x14\x21\x1D\x07\x05\x19\x5D\x5D\x47\x52\x60\x46\x4C\x1E\x1D\x5F\x5F\x1C\x15\x7E\x0B\x0B\x00\x49\x51\x5F\x55\x44\x31\x52\x45\x13\x1B\x40\x5C\x46\x10\x7C\x38\x10\x19\x07\x55\x13\x44\x56\x31\x1C\x15\x19\x1B\x56\x13\x47\x58\x30\x1D\x1B\x58\x55\x1D\x57\x5D\x41\x7C\x4D\x4B\x4D\x49\x4F";
	buf = "";
	if(k.length == 9) {
		for(i = 0, j = 0; i < func.length; i++) {
			c = parseInt(func.charCodeAt(i));
			c = c ^ k.charCodeAt(j);
			if(++j == k.length) {
				j = 0;
			}
			buf += eval('"' + a(x(c)) + '"');
		}
		eval(buf);
	} else {
		$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
	}
});

function a(h) {
	if(h.length != 2) {
		h = "\x30" + h;
	}
	return "\x5c\x78" + h;
}

function x(d) {
	if(d < 0) {
		d = 0xFFFFFFFF + d + 1;
	}
	return d.toString(16).toUpperCase();
}
```

The key length is 9 characters as we can see here: `if(k.length == 9) {`

The cipher text is XORed against the key and because the key is re-used for each block of 9 characters, we can probably perform a known plaintext attack to retrieve the key. We don't know the key but we have the key length and we can guess what some of the plaintext contains.

I wrote a simple script that XORs the string 'document.' against each 9 characters blocks of the ciphertext and saves the resulting key in a list. Then we take each key, XOR the full ciphertext and output the result if it contains 'document.'. 

``` python
import re

def main():
	keys = []
	c = "\x2B\x09\x4A\x03\x49\x0F\x0E\x14\x15\x1A\x00\x10\x3F\x1A\x71\x5C\x5B\x5B\x00\x1A\x16\x38\x06\x46\x66\x5A\x55\x30\x0A\x03\x1D\x08\x50\x5F\x51\x15\x6B\x4F\x19\x56\x00\x54\x1B\x50\x58\x21\x1A\x0F\x13\x07\x46\x1D\x58\x58\x21\x0E\x16\x1F\x06\x5C\x1D\x5C\x45\x27\x09\x4C\x1F\x07\x56\x56\x4C\x78\x24\x47\x40\x49\x19\x0F\x11\x1D\x17\x7F\x52\x42\x5B\x58\x1B\x13\x4F\x17\x26\x00\x01\x03\x04\x57\x5D\x40\x19\x2E\x00\x01\x17\x1D\x5B\x5C\x5A\x17\x7F\x4F\x06\x19\x0A\x47\x5E\x51\x59\x36\x41\x0E\x19\x0A\x53\x47\x5D\x58\x2C\x41\x0A\x04\x0C\x54\x13\x1F\x17\x60\x50\x12\x4B\x4B\x12\x18\x14\x42\x79\x4F\x1F\x56\x14\x12\x56\x58\x44\x27\x4F\x19\x56\x49\x16\x1B\x16\x14\x21\x1D\x07\x05\x19\x5D\x5D\x47\x52\x60\x46\x4C\x1E\x1D\x5F\x5F\x1C\x15\x7E\x0B\x0B\x00\x49\x51\x5F\x55\x44\x31\x52\x45\x13\x1B\x40\x5C\x46\x10\x7C\x38\x10\x19\x07\x55\x13\x44\x56\x31\x1C\x15\x19\x1B\x56\x13\x47\x58\x30\x1D\x1B\x58\x55\x1D\x57\x5D\x41\x7C\x4D\x4B\x4D\x49\x4F"
	
	for i in range(0, len(c) - 9):
		chunk_c = c[i:i+9]		# ciphertext chunk
		chunk_p = "document."	# our known plaintext
		
		# XOR the plaintext with our ciphertext to get the key
		key = ""
		for j in range(0, 9):
			key = key + chr(ord(chunk_c[j]) ^ ord(chunk_p[j]))
		keys.append(key)

	# Try out key against the full ciphertext
	for key in keys:
		message = ""		
		for i in range(0, len(c) - 9):
			message = message + chr(ord(c[i]) ^ ord(key[i % 9]))
		
		# Check if the resulting plaintext is good
		if re.search('document\.', message):
			print('Key: %s\nMessage: %s\n\n' % (key, message))

if __name__ == '__main__':
	main()
```	

We get quite a few hits but one contains the correct plaintext. The key is **Bobvi2347**.

```
Key: @(#<tji9
Message: k!i?=eq},Z(3n#2b@25r,3lp" !|: 8,+g:jt>d9aa2,/s,b1aa&5#r6b5|g!o#s<)%Adocument.?zag,ql&.f("?p=") n("+i1#3.?g%%~-!8`vi-%~984ali)8x>lv. x1w?xg}{9g<j`x)1}gg:j=|d-a5$9m7".k no"i5 u,>#(<=; <}qzf/o*#/)<3%s?l-oq46%o<l.ap58d!w

Key: =!.5~};9
Message: 04k-|qs/,=1/!`b'738al+7"3=."j,pr8x5*fka:'.=28`ca:3713"`g|<4m12(+wA?zag,ql&.document.== -1) { 5= 9(%!a.dr'7?9#j`-|/7?-:fa7|+*9*n$.{m3e~le/{br>x!l+c}<r8x|hf--: &+,# |k{{m0(!"',e6*.|/"n}*od=.>!})g172+no*!47.(n|a+ :v`c

Key: Bobvi2347
Message: if(u == "XorIsCoolButNotUnbreakable") { if(document.location.href.indexOf("?p=") == -1) { document.location = document.location.href + "?p=" + u; } } else {  $("#cresponse").html("<div class='error'>Wrong password sorry.</

Key: Jobbp>2.9
Message: af(a91<:,Por]jOnubJutZvxTtlzeaxnm,! {4pj)~akumqwx/vakat}vb/r|mf.}whdbAn("+i1#3.5= 9(%!a.location document.5 d{zyl`|.l{zmusaf.hf|j!1.*?p);,*:{3 }4d,dv}m {49()8-kregicoik*).|mam2,4dib9om{}{='qk~nh)6Wr{wk!jo{sw{kh!iazry:%#

Key:  elg"0%w
Message: 0)/o.->1b uS}Sl~,:sTadV"+*fqorotbpo|:gv+u/::j`d-}/:.ssa~-y2<))s`tfi?g%%~-!8`dr'7?9#j`= documen5 d{zyl`document.-akumqwx/7aohkv#:`{pw',0(15boz:s0f}3<o|:.4+3c:=bi~mb%{f)rz}o9be+nl.sop3*r |blcgguu`w#a!*<pu|t#b/+=~42?
```

To get the flag, we submit the flag with: **?p=XorIsCoolButNotUnbreakable**