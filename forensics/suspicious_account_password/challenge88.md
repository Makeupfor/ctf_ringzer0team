# Suspicious Account Password - Challenge 88

Let's dig into that file with volatility, it's probably a memory dump.

```
root@kali:~# volatility imageinfo -f 5bd2510a83e82d271b7bf7fa4e0970d1
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86
                     AS Layer1 : IA32PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/root/5bd2510a83e82d271b7bf7fa4e0970d1)
                      PAE type : No PAE
                           DTB : 0x185000L
                          KDBG : 0x82920be8L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x82921c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2014-03-09 20:57:55 UTC+0000
     Image local date and time : 2014-03-09 13:57:55 -0700
```

Ok good, let's keep digging for more useful stuff

```
root@kali:~# volatility hivelist --profile=Win7SP1x86 -f 5bd2510a83e82d271b7bf7fa4e0970d1
Volatility Foundation Volatility Framework 2.6
Virtual    Physical   Name
---------- ---------- ----
0x879d0008 0x0c824008 \Device\HarddiskVolume1\Boot\BCD
0x87bd88d8 0x0c0958d8 \SystemRoot\System32\Config\SOFTWARE
0x93d47008 0x03bf3008 \??\C:\Users\flag\ntuser.dat
0x93d4f580 0x01970580 \??\C:\Users\flag\AppData\Local\Microsoft\Windows\UsrClass.dat
0x82090450 0x06491450 \SystemRoot\System32\Config\SAM
0x820984a0 0x06bab4a0 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0x820a0558 0x05c85558 \SystemRoot\System32\Config\SECURITY
0x8210e0d0 0x063e80d0 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0x8780c008 0x0029b008 [no name]
0x87819938 0x00122938 \REGISTRY\MACHINE\SYSTEM
0x878419d0 0x0008c9d0 \REGISTRY\MACHINE\HARDWARE
0x878c5008 0x0b6b7008 \SystemRoot\System32\Config\DEFAULT

root@kali:~# volatility hashdump --profile=Win7SP1x86 -f 5bd2510a83e82d271b7bf7fa4e0970d1
Volatility Foundation Volatility Framework 2.6
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
flag:1000:aad3b435b51404eeaad3b435b51404ee:3008c87294511142799dca1191e69a0f:::
```

Sweet, the flag hash is probably what we are looking for so let's look it up on https://crackstation.net/

`3008c87294511142799dca1191e69a0f	NTLM	admin123`

Success!
