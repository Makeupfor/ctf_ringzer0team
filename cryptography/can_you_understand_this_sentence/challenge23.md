# Can you understand this sentence - Challenge 23

xipak-comok-repuk-vanik-dytuk-dimyk-sinyx

Google reveals this looks like Bubble Babble Binary Data Encoding

Documentation: http://wiki.yak.net/589/Bubble_Babble_Encoding.txt

There's already a Python library to encode/decode it:

```
pip install bubblepy

python
>>> from bubblepy import BubbleBabble
>>> bb = BubbleBabble()
>>> bb.decode('xipak-comok-repuk-vanik-dytuk-dimyk-sinyx')
'hackingbubble'
>>>
```
