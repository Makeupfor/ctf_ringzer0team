# Spy my girl - Challenge 12

Source 2.4.1 is an HP keyboard, that looks interesting...

First we'll extract the payload from the packets

`tshark -r 4c27525e7a3d2e45495c6284386b4d5c.cap -T fields -e usb.capdata 'usb.src == "2.4.1"' > keyboard.txt`

Then we need to check the payload for keydown events (3rd byte contains our key pressed). I used this document to build the dictionary in my Python script.

http://www.usb.org/developers/hidpage/Hut1_12v2.pdf

`<DELETE><DELETE><DELETE>www.google.ca<SPACEBAR><ENTER>litlle<SPACEBAR><DELETE><DELETE><DELETE>ca<DELETE><DELETE><DELETE><DELETE><DELETE><DELETE>litle<SPACEBAR>cat<SPACEBAR>iin<SPACEBAR>thee<SPACEBAR>world<ENTER>gmail/<DELETE>.coom<ENTER>challenge2gmaail.coom<ENTER>flag-11234eteh<ENTER>hhi<SPACEBAR>mom,<ENTER>i<SPACEBAR>lovvee<SPACEBAR>yoou<SPACEBAR><DELETE>.<ENTER>bbyee<SPACEBAR><ENTER>`

[challenge12.py](challenge12.py)
