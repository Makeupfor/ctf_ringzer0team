# Random login form - Challenge 171

We can use an SQL truncation vulnerability to create a new admin account with the password we specify:

In the register form, we submit the following :

`username: admin                                            xxxxxxxxxxxx`

`password: blablabla`

Then we can log in as admin.
