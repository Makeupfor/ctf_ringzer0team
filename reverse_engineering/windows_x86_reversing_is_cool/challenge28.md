# Windows x86 reversing is cool - Challenge 28

The program asks for a key and check if its valid. To crack this we'll need to discover how the key validation works.

The first thing the program checks is the length of the key. It has to be exactly 6 characters long.

```
.text:004013FE                 mov     [esp], eax      ; char *
.text:00401401                 call    _strlen
.text:00401406                 cmp     eax, 6
.text:00401409                 jz      short loc_40146F
.text:0040140B                 mov     dword ptr [esp], offset aWrongKey ; "Wrong Key!"
.text:00401412                 call    _printf
.text:00401417                 mov     dword ptr [esp], 1 ; uExitCode
.text:0040141E                 call    _ExitProcess@4
```

Then we have the piece of code that validate each letter of the key

```
.text:00401423 loc_401423:                             ; CODE XREF: _main+E8j
.text:00401423                 mov     eax, [ebp+LetterCounter]
.text:00401426                 mov     edx, [ebp+LetterCounter]
.text:00401429                 mov     dl, [ebp+edx+var_41C]
.text:00401430                 xor     edx, 0FFFFFFD3h
.text:00401433                 mov     [ebp+eax+var_41C], dl
.text:0040143A                 mov     eax, [ebp+LetterCounter]
.text:0040143D                 mov     dl, [ebp+eax+var_41C]
.text:00401444                 mov     eax, [ebp+LetterCounter]
.text:00401447                 mov     al, [ebp+eax+var_423]
.text:0040144E                 cmp     dl, al
.text:00401450                 jz      short loc_40146A
.text:00401452                 mov     dword ptr [esp], offset aWrongKey ; "Wrong Key!"
.text:00401459                 call    _printf
.text:0040145E                 mov     dword ptr [esp], 2 ; uExitCode
.text:00401465                 call    _ExitProcess@4
```

Through a bit of debugging, we find that DL contains the letter of our typed key
 and DL is then XOR'ed with a hardcoded value of D3. The code compares DL against AL, which is set to a byte in var_423.

var_423 is the valid key (97 E0 EB A0 B8 E1):

```
.text:004013BD                 mov     ebx, offset aCriaS ; "ùadá+ß"
```

To find the key we just need to take each char in var_423 and XOR it with D3 and we get the key which is 'D38sk2'

We execute the program and we get the flag:

```
Key:D38sk2
FLAG-PIIXtM36MtKJ8347qh72r7C3
```
