#!/usr/bin/env python

import math
import re

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def main():
    s = "GMODCDOOKCDBIOYDRMKDPQLDPVWYOIVRVSEOV"

    # Let's try rotations
    for i in range(1,26):
        message = rot_alpha(i)(s)
        # Check if we have all 4 letters in the word FLAG somewhere in the message
        if re.search('F', message) and re.search('L', message) and re.search('A', message) and re.search('G', message):
            print("FLAG letters found in %s" %message)
            # Let's try to decode using scytale and all possible keys for the message length
            for key in range(1, int(len(message) / 2)):
                num_col = int(math.ceil(len(message) / float(key)))
                num_rows = key
                num_empty = (num_col*num_rows) - len(message)
                decrypted = [''] * num_col
                col = 0
                row = 0
                for car in message:
                    decrypted[col] += car
                    col += 1
                    if (col == num_col) or (col == num_col - 1 and row >= num_rows - num_empty):
                        col = 0
                        row += 1
                decrypted_message = ''.join(decrypted)
                # We found the message
                if re.search('FLAG', decrypted_message):
                    print(">>>>> %s <<<<<" % decrypted_message)
                else:
                    print("\t%s" % decrypted_message)

if __name__ == '__main__':
    main()
