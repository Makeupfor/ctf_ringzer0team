def main():
    # This is the challenge taken from the .pcap in the ICMP packets 250-265
    # The plaintext is in the data field, the key is in the sequence field
    challenge = [
    'eb11d60a9f10cc59,bf79',
    'c6d1c5c1c784d6cb,b5a4',
    '0a3d0d3f01351032,645b',
    '47e007ac60c067cb,268c',
    '5ef640f14b8842f2,73c2',
    'd8f2ab8bad80e0ad,9ac2',
    'f7d395ae93d0a9e6,c19f',
    '986b986b9817ed03,a85b',
    ]    

    p = ''
    
    for line in challenge:
        c = line.split(',')[0]
        k = line.split(',')[1]        

        # XOR the plaintext with the key
        for i in range(0, 16, 4):
            p = p + chr(ord(c[i:i+2].decode('hex')) ^ ord(k[:2].decode('hex')))
            p = p + chr(ord(c[i+2:i+4].decode('hex')) ^ ord(k[2:4].decode('hex')))

    print p        


if __name__ == '__main__':
    main()