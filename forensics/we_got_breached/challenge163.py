#/usr/bin/env python

import re

def main():
    data = {}

    '''
    Read the file we saved with tshark, it should have the following format:
    Source GeoIP: Unknown,Destination GeoIP: Unknown,No-Operation (NOP),No-Operation (NOP),Timestamps: TSval 455551, TSecr 455551,HTTP/1.1 200 OK\r\n,\r\n,Content-encoded entity body (gzip): 135 bytes -> 124 bytes,User id:1 AND ORD(MID((SELECT IFNULL(CAST(flag AS CHAR),0x20) FROM chart_db.flag ORDER BY flag LIMIT 0,1),4,1))>64 was found
    Source GeoIP: Unknown,Destination GeoIP: Unknown,No-Operation (NOP),No-Operation (NOP),Timestamps: TSval 455551, TSecr 455551,HTTP/1.1 200 OK\r\n,\r\n,Content-encoded entity body (gzip): 135 bytes -> 124 bytes,User id:1 AND ORD(MID((SELECT IFNULL(CAST(flag AS CHAR),0x20) FROM chart_db.flag ORDER BY flag LIMIT 0,1),1,1))>64 was found
    Source GeoIP: Unknown,Destination GeoIP: Unknown,No-Operation (NOP),No-Operation (NOP),Timestamps: TSval 455551, TSecr 455551,HTTP/1.1 200 OK\r\n,\r\n,Content-encoded entity body (gzip): 135 bytes -> 124 bytes,User id:1 AND ORD(MID((SELECT IFNULL(CAST(flag AS CHAR),0x20) FROM chart_db.flag ORDER BY flag LIMIT 0,1),3,1))>64 was found
    '''
    with open('flag_boolean_sql.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
        m = re.search(r'ORDER BY flag LIMIT 0,1\),(\d+),1\)\)>(\d+) was (.*)', line)
        m_pos = int(m.group(1))     # character position we polled with our SQLi
        m_chr = int(m.group(2))     # decimal ascii value return by SQLi
        m_hit = m.group(3)          # found / not found returned by SQLi
        # We already have that character in our dictionnary
        if m_pos in data:
            # Increase minimum decimal ASCII value to current match + 1
            if m_hit == 'found':
                data[m_pos]['char'] = m_chr + 1
        # Process first response for character position
        else:
            data[m_pos] = {}
            data[m_pos]['char'] = m_chr + 1

    # Print out the flag value
    answer = ''
    for i in range(1, len(data) + 1):
        answer = answer + chr(data[i]['char'])
    print answer

if __name__ == '__main__':
    main()
