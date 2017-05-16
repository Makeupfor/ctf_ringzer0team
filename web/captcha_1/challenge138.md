# Captcha 1 - Challenge 138

The challenge answer is in the javascript code downloaded by our GET request:

``` js
function doIt(){
var A = document.getElementById('captcha-form').value;
if (A == "peduwev"){
document.forms["Form1"].submit();
}
else {
alert("BAD Captcha");
}
}
```

So it's pretty easy, we just have to parse out the challenge answer, issue the POST 1000 times with a script.

[challenge138.py](challenge138.py)
