# Agent Smith reloaded - Challenge 24

```
root@kali:~# file BK
BK: Linux rev 1.0 ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1c9a80
```

```
root@kali:~# binwalk -e BK

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
218112        0x35400         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
239616        0x3A800         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
270336        0x42000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
277504        0x43C00         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
286720        0x46000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
301056        0x49800         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
307200        0x4B000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
332800        0x51400         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
339968        0x53000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
353280        0x56400         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
368640        0x5A000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
375808        0x5BC00         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
389120        0x5F000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
413696        0x65000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
420864        0x66C00         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
453632        0x6EC00         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
487424        0x77000         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
497664        0x79800         Linux EXT filesystem, rev 1.0, ext3 filesystem data, UUID=ca014691-c6ea-4a5a-8da4-74a1aa1caa1c
1257472       0x133000        Zip archive data, compressed size: 43, uncompressed size: 43, name: mimetype
1257553       0x133051        Zip archive data, at least v2.0 to extract, name: meta.xml
1258056       0x133248        Zip archive data, at least v2.0 to extract, name: settings.xml
1258496       0x133400        Zip archive data, encrypted at least v2.0 to extract, compressed size: 26, uncompressed size: 16, name: secret.txt
1258686       0x1334BE        End of Zip archive
1259520       0x133800        Zip archive data, compressed size: 43, uncompressed size: 43, name: mimetype
1259601       0x133851        Zip archive data, at least v2.0 to extract, name: meta.xml
1260104       0x133A48        Zip archive data, at least v2.0 to extract, name: settings.xml
1261652       0x134054        Zip archive data, at least v2.0 to extract, name: content.xml
1263019       0x1345AB        Zip archive data, at least v2.0 to extract, compressed size: 1462, uncompressed size: 1462, name: Thumbnails/thumbnail.png
1264535       0x134B97        Zip archive data, at least v2.0 to extract, name: Configurations2/images/Bitmaps/
1264596       0x134BD4        Zip archive data, at least v2.0 to extract, name: Configurations2/popupmenu/
1264652       0x134C0C        Zip archive data, at least v2.0 to extract, name: Configurations2/toolpanel/
1264708       0x134C44        Zip archive data, at least v2.0 to extract, name: Configurations2/statusbar/
1264764       0x134C7C        Zip archive data, at least v2.0 to extract, name: Configurations2/progressbar/
1264822       0x134CB6        Zip archive data, at least v2.0 to extract, name: Configurations2/toolbar/
1264876       0x134CEC        Zip archive data, at least v2.0 to extract, name: Configurations2/floater/
1264930       0x134D22        Zip archive data, at least v2.0 to extract, name: Configurations2/menubar/
1264984       0x134D58        Zip archive data, at least v2.0 to extract, name: Configurations2/accelerator/current.xml
1265071       0x134DAF        Zip archive data, at least v2.0 to extract, name: styles.xml
1267605       0x135795        Zip archive data, at least v2.0 to extract, name: META-INF/manifest.xml
1269024       0x135D20        End of Zip archive
1270868       0x136454        Zip archive data, at least v2.0 to extract, name: content.xml
1272235       0x1369AB        Zip archive data, at least v2.0 to extract, compressed size: 1462, uncompressed size: 1462, name: Thumbnails/thumbnail.png
1273751       0x136F97        Zip archive data, at least v2.0 to extract, name: Configurations2/images/Bitmaps/
1273812       0x136FD4        Zip archive data, at least v2.0 to extract, name: Configurations2/popupmenu/
1273868       0x13700C        Zip archive data, at least v2.0 to extract, name: Configurations2/toolpanel/
1273924       0x137044        Zip archive data, at least v2.0 to extract, name: Configurations2/statusbar/
1273980       0x13707C        Zip archive data, at least v2.0 to extract, name: Configurations2/progressbar/
1274038       0x1370B6        Zip archive data, at least v2.0 to extract, name: Configurations2/toolbar/
1274092       0x1370EC        Zip archive data, at least v2.0 to extract, name: Configurations2/floater/
1274146       0x137122        Zip archive data, at least v2.0 to extract, name: Configurations2/menubar/
1274200       0x137158        Zip archive data, at least v2.0 to extract, name: Configurations2/accelerator/current.xml
1274287       0x1371AF        Zip archive data, at least v2.0 to extract, name: styles.xml
1276821       0x137B95        Zip archive data, at least v2.0 to extract, name: META-INF/manifest.xml
1278240       0x138120        End of Zip archive
```

```
root@kali:~/_BK.extracted# cat ext-root/TODO.me
-cryt my password file with Secret Vault Encrypt  
-bring back milk
-buy flower for my love !
-restric my my little brother permission to delete file.
```

There's no file that contains anything useful, but the reference to a deleted file in the TODO.me file gives us a hint.

```
root@kali:~# ext3grep --inode 2 BK
Running ext3grep version 0.10.2
No --ls used; implying --print.

WARNING: I don't know what EXT3_FEATURE_COMPAT_EXT_ATTR is.
Number of groups: 1
Loading group metadata... done
Minimum / maximum journal block: 198 / 1227
Loading journal descriptors... sorting... done
The oldest inode block that is still in the journal, appears to be from 1391736883 = Thu Feb  6 20:34:43 2014
Number of descriptors in journal: 252; min / max sequence numbers: 3 / 47

Hex dump of inode 2:
0000 | ed 41 f4 01 00 04 00 00 55 42 f4 52 1b 42 f4 52 | .A......UB.R.B.R
0010 | 1b 42 f4 52 00 00 00 00 f4 01 05 00 02 00 00 00 | .B.R............
0020 | 00 00 00 00 00 00 00 00 b8 00 00 00 00 00 00 00 | ................
0030 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0040 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0050 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0060 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................
0070 | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................

Inode is Allocated
Group: 0
Generation Id: 0
uid / gid: 500 / 500
mode: drwxr-xr-x
size: 1024
num of links: 5
sectors: 2 (--> 0 indirect blocks).

Inode Times:
Accessed:       1391739477 = Thu Feb  6 21:17:57 2014
File Modified:  1391739419 = Thu Feb  6 21:16:59 2014
Inode Modified: 1391739419 = Thu Feb  6 21:16:59 2014
Deletion time:  0

Direct Blocks: 184
Loading BK.ext3grep.stage2... done
The first block of the directory is 184.
Inode 2 is directory "".
Directory block 184:
          .-- File type in dir_entry (r=regular file, d=directory, l=symlink)
          |          .-- D: Deleted ; R: Reallocated
Indx Next |  Inode   | Deletion time                        Mode        File name
==========+==========+----------------data-from-inode------+-----------+=========
   0    1 d       2                                         drwxr-xr-x  .
   1    2 d       2                                         drwxr-xr-x  ..
   2    3 d      11                                         drwx------  lost+found
   3    5 r      14                                         rrw-r--r--  TODO.me
   4    5 r      12  D 1391739419 Thu Feb  6 21:16:59 2014  rrw-r--r--  secret.sve
   5    6 d      13                                         drwxr-xr-x  .hide
   6  end d      17                                         drwxr-xr-x  .ls
   7  end r      16  D 1391739038 Thu Feb  6 21:10:38 2014  rrw-rw-r--  secret.odg
```

secret.sve and secret.odg were deleted, let's restore all the files:

```
root@kali:~# ext3grep --restore-all BK
Running ext3grep version 0.10.2
WARNING: I don't know what EXT3_FEATURE_COMPAT_EXT_ATTR is.
Number of groups: 1
Minimum / maximum journal block: 198 / 1227
Loading journal descriptors... sorting... done
The oldest inode block that is still in the journal, appears to be from 1391736883 = Thu Feb  6 20:34:43 2014
Number of descriptors in journal: 252; min / max sequence numbers: 3 / 47
Writing output to directory RESTORED_FILES/
Loading BK.ext3grep.stage2... done
Restoring .hide/secret.odg
Restoring TODO.me
Restoring secret.odg
Restoring secret.sve
```

secret.sve is an encrypted zip archive.

```
password incorrect--reenter: root@kali:~/RESTORED_FILES# file secret.sve
secret.sve: Zip archive data, at least v2.0 to extract

root@kali:~/RESTORED_FILES# unzip secret.sve
Archive:  secret.sve
[secret.sve] secret.txt password:
```

I used fcrackzip to bruteforce it but I should have tried a few more common passwords first...

```
root@kali:~/RESTORED_FILES# fcrackzip -b -l 1-8 -c 'aA1' -u secret.sve


PASSWORD FOUND!!!!: pw == 12345
```

The flag is found in the file.
