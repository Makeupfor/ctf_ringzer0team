def main():
    u = 'administrator'
    p = [176,214,205,246,264,255,227,237,242,244,265,270,283]
    answer = ''
    for i, letter in enumerate(p):
        answer = answer + chr(letter - (10 * i) - ord(u[i]))
    print answer

if __name__ == '__main__':
    main()
