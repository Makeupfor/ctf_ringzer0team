#!/usr/bin/env python

# 2nd variant of Bacon's Cipher
# https://en.wikipedia.org/wiki/Bacon%27s_cipher
bacon = {
    'aaaaa': 'a',
    'aaaab': 'b',
    'aaaba': 'c',
    'aaabb': 'd',
    'aabaa': 'e',
    'aabab': 'f',
    'aabba': 'g',
    'aabbb': 'h',
    'abaaa': 'i',
    'abaab': 'j',
    'ababa': 'k',
    'ababb': 'l',
    'abbaa': 'm',
    'abbab': 'n',
    'abbba': 'o',
    'abbbb': 'p',
    'baaaa': 'q',
    'baaab': 'q',
    'baaab': 'r',
    'baaba': 's',
    'baabb': 't',
    'babaa': 'u',
    'babab': 'v',
    'babba': 'w',
    'babbb': 'x',
    'bbaaa': 'y',
    'bbaab': 'z',
}

def main():
    message = "VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!"
    c1 = '' # Ciphertext: Uppercase letters are A, Lowercase letters are B
    c2 = '' # Ciphertext: Uppercase letters are B, Lowercase letters are A
    p1 = '' # Plaintext of message c1
    p2 = '' # Plaintext of message c2

    for letter in message:
        if letter.isupper():
            c1 = c1 + 'a'
            c2 = c2 + 'b'
        if letter.islower():
            c1 = c1 + 'b'
            c2 = c2 + 'a'    

    # Decipher message 1
    for i in range(0, len(c1) - 5, 5):
        try:
            p1 = p1 + bacon[c1[i:i+5]]
        except KeyError:
            p1 = p1 + "#"

    # Decipher message 2
    for i in range(0, len(c2) - 5, 5):
        try:
            p2 = p2 + bacon[c2[i:i+5]]
        except KeyError:            
            p2 = p2 + "#"

    print('Ciphertext 1: %s\nLen: %d\nPlaintext: %s\n' % (c1, len(c1), p1))
    print('Ciphertext 2: %s\nLen: %d\nPlaintext: %s\n' % (c2, len(c2), p2))

if __name__ == '__main__':
    main()