from requests import get
import re

from PIL import Image
import pytesseract

def main():
    cookies = dict(PHPSESSID = "xxxxxxxxxxxxxxxxxxxxxxxxx")
    url = "https://ringzer0team.com/challenges/17"

    # GET the html page
    html = get(url, cookies=cookies).content

    # Extract image from base64 encoded text
    img = re.search(r'data:image/png;base64,(\S+)"', html).group(1)
    f = open("challenge17.png", "wb")
    f.write(img.decode('base64'))
    f.close()

    # Manipulate our image to make it OCR friendly
    n = Image.open('challenge17.png')
    m = n.load()
    # Get x,y size
    s = n.size
    # Iterate through x and y (every pixel)
    for x in xrange(s[0]):
        for y in xrange(s[1]):
            r,g,b = m[x,y]
            if (r != 255 or g != 255 or b != 255):
                m[x,y] = 0,0,0

    # Save the doctored image
    n.save('new_challenge17.jpg', "JPEG")

    # OCR the image *** Not always reliable, try multiple times ***
    answer = pytesseract.image_to_string(Image.open('new_challenge17.jpg'))

    # Submit the answer
    html = get("%s/%s" % (url, answer), cookies=cookies).content
    flag = re.search(r"(FLAG-\w+)<", html).group(1)
    print("FLAG is: %s" % flag)


if __name__ == '__main__':
    main()
