var CryptoJS = require("crypto-js");
var c = "ob1xQz5ms9hRkPTx+ZHbVg==";
var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
var p = CryptoJS.AES.decrypt(c, CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) })
console.log(p.toString(CryptoJS.enc.Utf8));
