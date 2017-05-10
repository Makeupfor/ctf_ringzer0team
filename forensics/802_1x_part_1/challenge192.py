import hashlib
import os
import re

goodhash = 'd936fe3ccbe8e7a79f58a19a6adf26f3'
radius_msg =  '04c5017400000000000000000000000000000000011341525542414e4554574f524b535c72616f0406c0a80a010506000000003d06000000132c1f41525542414e45543130304241393642363139382d3535363031413133370655601aa532193130304241393642363139382d303030303030303030340806c0a80a9f1f0e3130304241393642363139381e0e303030423836423836313230193a48cd2fc61c604eb0858987ac517fcdf8b90b0000000000005230303030303031332d30312d353535666232646400000000000000000000002906000000001a1b000039e7051552616f206c696b6573203158204d6f766965731a19000039e7061330303a30623a38363a63663a65323a31361a0f000039e70a0964656661756c741a15000039e7010f61757468656e746963617465641a0c000039e70206000000011a0d000039e70c0757696e20372806000000022a06000084db2b060000ab482f060000010e3006000000c331060000000a2e0600000092'
msg = radius_msg.decode('hex')

def main():
    print('Authenticator field from the pcap: %s' % goodhash)
    print('Hash length: %d' % len(goodhash))
    print('RADIUS message to be prefixed to the secret: %s' % radius_msg)
    print('Length of RADIUS message: %d' % len(msg))

    for filename in os.listdir('.'):
        if filename.endswith(".dic"):
            with open(filename) as f:
                print('Cracking using: %s' % filename)
                words = f.read().splitlines()
                # Let's try a wordlist
                for w in words:
                    h = hashlib.md5(msg + w).hexdigest()
                    if h == goodhash:
                        print('Found it! --> %s' % w)
                        exit(0)

if __name__ == '__main__':
    main()
