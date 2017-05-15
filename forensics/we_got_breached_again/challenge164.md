# We got breached again - Challenge 164

It looks like the attacker is probing each bit position for each character in the flag selected with the GROUP_CONCAT function.

When the IF statement is TRUE, SLEEP(2) is called. The trick here to determine if a bit position in the character is set to 1 is to check if there's a 2 seconds gap between two entries in the access logs.

In a nutshell, the script does the following:
* Escape characters (%20 -> ' ')
* Remove the comments (/\* 09dnOt \*/)
* Remove lines that don't contain chart_db.flag
* Compare timestamps to determine bitmask for each character in the flag

`FLAG-oz5K5V***************`

[challenge164.py](challenge164.py)
