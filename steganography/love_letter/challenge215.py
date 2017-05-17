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
