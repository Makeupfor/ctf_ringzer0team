import hashlib
import re

def main():       
    charset_small = range(48,58) + range(97,103)
    charset = range(48,58) + range(97,123)    

    # Open hash files (need to increase ulimit first)
    fs = {}
    for f1 in charset_small:
        for f2 in charset_small:
            for f3 in charset_small:
                for f4 in charset_small:
                    bucket = chr(f1) + chr(f2) + chr(f3) + chr(f4)
                    fs[bucket] = open(bucket, 'w')            

    # Build our list of plaintext to bruteforce
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    for e in charset:
                        for f in charset:
                            p = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f)
                            h = hashlib.sha1(p).hexdigest()                            
                            fs[h[:4]].write('%s,%s\n' % (p,h))
                            
    print('Done.')