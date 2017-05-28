# Meat loaf - Challenge 140

The recipe in this challenge is actually a program. It uses the Chef programming language, described here: http://www.dangermouse.net/esoteric/chef.html

There are already a few  interpreters available to run the code, I've used this one:
http://search.cpan.org/~wernermp/Acme-Chef-1.03/

``` perl
# Using the module
use Acme::Chef;

open my $fh, '<', "recipe.txt";
read $fh, my $code_string, -s $fh;
close $fh;

my $compiled = Acme::Chef->compile($code_string);
print $compiled->execute();
```

```
$ perl chef.pl
IWouldntEatThat
```
