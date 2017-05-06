# Read me if you can - Challenge 17

We need to read the letter on this image:

![captcha](challenge17.png)

I used PIL and pytesseract to work this challenge.

Since the letters are all white (255,255,255), it's easy to defeat this one.

Take everything that's not white and make it black, then we're left with only the letters that we'll OCR with tesseract.

It doesn't always work on the first try but if we run the script a couple of times we are able to get the flag.


[challenge17.py](challenge17.py)
