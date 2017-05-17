# Love letter - Challenge 215

There are two kinds of white spaces in this file: 0x20 and 0xA0

* 0x20 maps to a 0
* 0xA0 maps to a 1

So we just need to write a script that reads all the whitespaces in the file, converting them to binary then we display the resulting ASCII characters.

``` python
def main():
    f = open('LoveLetter.txt')
    txt = f.read()
    bits = ''
    answer = ''
    for c in txt:
        if ord(c) == 0x20:
            bits = bits + '0'
            if len(bits) == 8:
                answer = answer + chr(int(bits, 2))
                bits = ''
        elif ord(c) == 0xA0:
            bits = bits + '1'
            if len(bits) == 8:
                answer = answer + chr(int(bits, 2))
                bits = ''

    print(answer)

if __name__ == '__main__':
    main()

```
