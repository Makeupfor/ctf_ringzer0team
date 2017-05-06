from pexpect import pxssh
import re
from time import sleep

def main():
    win = 0
    current_val = 5000
    max_val = 10000

    s = pxssh.pxssh()
    s.login('ringzer0team.com', port=12643, username='number', password='Z7IwIMRC2dc764L', terminal_type='vt100', original_prompt='number>', auto_prompt_reset=False)
    s.PROMPT='number>'

    while (win < 10):
        s.sendline(str(current_val))
        s.prompt()
        ret = s.before
        if re.search('too big', ret):
            print 'Too big %d' % current_val
            max_val = current_val
            current_val = current_val / 2
        elif re.search('too small', ret):
            print 'Too small %d' % current_val
            current_val = current_val + ((max_val - current_val) / 2)
        elif re.search('FLAG', ret):
            print ret
            break
        elif re.search('right number', ret):
            print '\n>>>>>>>>> YOU WIN <<<<<<<<<<\n%d' % current_val
            win = win +1
            current_val = 5000
            max_val = 10000

if __name__ == '__main__':
    main()
