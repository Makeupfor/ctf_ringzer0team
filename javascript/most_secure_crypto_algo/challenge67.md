# Most secure crypto algo - Challenge 67

``` js
$(".c_submit").click(function(event) {
	event.preventDefault();
	var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
	var u = $("#cuser").val();
	var p = $("#cpass").val();
	var t = true;

	if(u == "\x68\x34\x78\x30\x72") {
		if(!CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) }) == "ob1xQz5ms9hRkPTx+ZHbVg==") {
			t = false;
		}
	} else {
		$("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
		t = false;
	}
	if(t) {
		if(document.location.href.indexOf("?p=") == -1) {
			document.location = document.location.href + "?p=" + p;
         			}
	}
});
```

Looking at the code above, we already have all we need to solve this challenge:
* We have the username -> "\x68\x34\x78\x30\x72" (h4x0r)
* We have the key -> first 16 bytes of the SHA256 hash
* We have the IV -> last 16 bytes of the SHA256 hash
* We have the ciphertext

``` js
var CryptoJS = require("crypto-js");
var c = "ob1xQz5ms9hRkPTx+ZHbVg==";
var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
var p = CryptoJS.AES.decrypt(c, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) })
console.log(p.toString(CryptoJS.enc.Utf8));
```

```
node challenge67.js
PassW0*********
```

[challenge67.js](challenge67.js)
