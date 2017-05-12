# We got breached - Challenge 163

There's clearly some form of SQL injection going on in this packet capture.

There's a lot of SQL queries that look like this:

```
User id:1 AND ORD(MID((SELECT IFNULL(CAST(flag AS CHAR),0x20) FROM chart_db.flag ORDER BY flag LIMIT 0,1),2,1))>64 was found
User id:1 AND ORD(MID((SELECT IFNULL(CAST(flag AS CHAR),0x20) FROM chart_db.flag ORDER BY flag LIMIT 0,1),2,1))>96 was not found
```

This looks like a Boolean Based Blind SQL Injection in which we sequentially go through each character and try to find which ASCII value it's set to.

First, we'll use tshark and extract the fields we need:

`tshark -r 93cec4f4aaaa0c8a96d6cd724547d19c.pcap -T fields -e text 'http.response.code==200' > flag_boolean_sql.txt`

Then we'll edit the file and remove all the lines we don't need, keeping only those with 'FROM chart_db.flag' in them. This is most likely the information we need to solve this challenge.

Then it's just a matter of writing a script to extract the ASCII string that was extracted with the SQL injection iteration through the table.

```
$ python challenge163.py
FLAG-NJf3JS*******************
```

[challenge163.md](challenge163.py)
