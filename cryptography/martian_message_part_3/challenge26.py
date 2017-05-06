def decrypt(c, k):
    ''' Decrypt function, XOR each byte with the key '''
    p = ''
    for i in c:
        p = p + chr(ord(i) ^ k)
    return p

def main():
    # Our encrypted flag
    c = 'EOBD.7igq4;1ikb51ibOO0;:41R'

    # Find the key
    for k in range(0, 255):
        p = chr(ord(c[0]) ^ k) + chr(ord(c[1]) ^ k) + chr(ord(c[2]) ^ k) + chr(ord(c[3]) ^ k)
        if p == 'FLAG':
            # Key has been found
            print('The key is: x%02x' % k)
            print('The flag is: %s' % decrypt(c, k))
            break

if __name__ == '__main__':
     main()
