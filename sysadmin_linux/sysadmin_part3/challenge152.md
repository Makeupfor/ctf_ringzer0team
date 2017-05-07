# Sysadmin part 3 - Challenge 152

Dig for flag.

We'll search for all files owned by the architect.

```
architect@forensics:/$ find / -user architect 2>&1 | egrep -v "Permission denied|proc"
/var/tmp/.swl
/var/mail/architect
/var/www/index.php
/dev/pts/5
/dev/pts/0
/home/architect
/home/architect/.profile
/home/architect/.bash_logout
/home/architect/.vimrc
/home/architect/.bashrc
```

/var/www/index.php contains some juicy bits:

```
$mysqlDatabaseName ="arch";
$mysqlUserName ="arch";
$mysqlPassword ="asdftgTst5sdf6309sdsdff9lsdftz";
```

Let's connect to the database and see what's going on there:

```
architect@forensics:/$ mysql -u arch -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 555
Server version: 5.5.52-0+deb7u1 (Debian)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use arch;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_arch |
+----------------+
| arch           |
| flag           |
+----------------+
2 rows in set (0.00 sec)

mysql> select * from flag;
+---------------------------------+
| flag                            |
+---------------------------------+
| FLAG-0I68UrLA758G5G30806w637a4k |
+---------------------------------+
1 row in set (0.00 sec)
```
