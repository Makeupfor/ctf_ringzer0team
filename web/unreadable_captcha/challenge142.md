# Unreadable CAPTCHA - Challenge 142

In the comments of the HTML, we have a reference to captcha3.txt:

``` html
<input type="submit" />
</form>
<!-- source code? captcha3.txt -->
</body>
</html>
```

Source code for the PHP script:

``` php
<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
	if (isset($_POST['captcha'])){
		if ($_POST['captcha'] == $_SESSION['captcha']){
		echo 'Congrats, the flag is XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' ;  
		} else {
		echo 'You have a wrong captcha. You are not a human. Try again later.';
}
	} else {
   header( 'Location: index.php' ) ;
}

}
else {
   header( 'Location: index.php' ) ;
}
?>
```

The script uses a loose comparison (== operator, instead of === for strict) between the POST and SESSION variables. This is probably something we can exploit to our advantage...

PHP documentation: http://php.net/manual/en/types.comparisons.php

OWASP link: https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf

With a loose comparison, NULL == array() -> TRUE so all need to do is send a POST with an empty value for the 'captcha' parameter.

`Congrats, the flag is FLAG-si*************`
