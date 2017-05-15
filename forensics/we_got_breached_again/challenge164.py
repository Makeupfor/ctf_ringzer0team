#/usr/bin/env python
import re
import time
import urllib

def main():
    with open('access.log') as f:
        buf = f.read().splitlines()

    lines = []

    # Clean up our log
    for line in buf:
        # Escape characters, replace by ASCII equivalent
        line = urllib.unquote(line)
        # Only check lines that contain our flag table
        if re.search('chart_db\.flag', line):
            # Remove comments from SQL query
            line = re.sub('/\*\w+\*/', '', line)
            lines.append(line)

    flag = ''
    bitmask = 0

    for i in range(0, len(lines)):
        # Char position in the flag
        log_charpos = int(re.search('chart_db\.flag\),(\d+),1\)', lines[i]).group(1))
        # Bit position in one character
        log_bitpos = int(re.search('16,2\)\),(\d+),1\)', lines[i]).group(1))

        log_time = lines[i][26:34]
        try:
            log_time_next = lines[i+1][26:34]
        except IndexError:
            pass

        # Reset bitmask if this is a new character
        if not i % 7 and i == 0:
            bitmask = 0
        if not i % 7:
            flag = flag + chr(bitmask)
            bitmask = 0

        # Use log time to check if we have a git on the flag character
        if time.strptime(log_time, '%H:%M:%S') < time.strptime(log_time_next, '%H:%M:%S'):
            print('charpos: %d, bitpos: %d -- MATCH!!!' % (log_charpos, log_bitpos))
            bitmask = bitmask ^ (1 << (log_bitpos - 1))
        else:
            print('charpos: %d, bitpos: %d' % (log_charpos, log_bitpos))

    flag = flag + chr(bitmask)
    print flag

if __name__=='__main__':
    main()
