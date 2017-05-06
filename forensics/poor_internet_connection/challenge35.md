# Poor internet connection - Challenge 35

1. Open the file in Wireshark

2. Check how many conversations there are (there's 3 TCP streams)

3. Let's do a search for interesting stuff (CTRL+F, then do a search for String -> password)

4. The .zip password is in that 2nd TCP stream

5. Follow both TCP stream #1 and #3, show data as raw then save the raw bytes to a file.

6. Try to repair both file with WinRar or 7zip, the flag is in our first file that we just repaired and decrypted with the password
