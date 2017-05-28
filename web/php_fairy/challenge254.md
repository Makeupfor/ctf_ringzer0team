# PHP fairy - Challenge 254

Because the script uses a loose comparison operator, we can exploit this one using a PHP type juggling attack.

``` php
if (isset($_GET['pass'])) {
  if(!preg_match('/^[^\W_]+$/', $_GET['pass'])) {
    $output = "Don't hack me please :(";
  } else {

    $pass = md5("admin1674227342");
    if ((((((((($_GET['pass'] == $pass)))) && (((($pass !== $_GET['pass']))))) || ((((($pass == $_GET['pass'])))) && ((($_GET['pass'] !== $pass)))))))) { // Trolling u lisp masta
      if (strlen($pass) == strlen($_GET['pass'])) {
        $output = "<div class='alert alert-success'>FLAG-XXXXXXXXXXXXXXXXXXXXXXX</div>";
      } else {
        $output = "<div class='alert alert-danger'>Wrong password</div>";
      }
    } else {
      $output = "<div class='alert alert-danger'>Wrong password</div>";
    }
  }
}
?>
```

The MD5 hash of `admin1674227342` is `0e463854177790028825434984462555`

We're lucky that the hash begins with 0e. 0e463854177790028825434984462555 is a double but is also 0 if converted to an integer. With the loose comparison we can supply a password of 0 and the logical comparison will be true if 0 == 0. We can't simply use 0 as the password because the code also check the length the password string so we'll just use 00000000000000000000000000000000.
