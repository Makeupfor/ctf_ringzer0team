# Dr Pouce - Challenge 103

The answer is in the GPS coordinate of the .jpg file.

```
root@kali:~# exiftool DR_Pouce.jpg | grep GPS
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Img Direction Ref           : Magnetic North
GPS Img Direction               : 237
GPS Latitude                    : 44 deg 38' 46.43" N
GPS Longitude                   : 63 deg 34' 23.83" W
GPS Position                    : 44 deg 38' 46.43" N, 63 deg 34' 23.83" W
```

That's Halifax.

The PDF properties reveal the author:

```
root@kali:~# exiftool DR_Pouce.pdf | grep Author
Author                          : Steve Finger
```
