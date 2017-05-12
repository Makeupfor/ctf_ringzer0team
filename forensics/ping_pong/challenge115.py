#!/usr/bin/env python

import re

'''
The following cmap is from the following font info in the .pdf file
PPDF> stream 8

/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo
<<  /Registry (Adobe)
/Ordering (UCS)
/Supplement 0
>> def
/CMapName /Adobe-Identity-UCS def
/CMapType 2 def
1 begincodespacerange
<0000> <FFFF>
endcodespacerange
10 beginbfchar
<0003> <0020>
<000C> <0041>
<0014> <0049>
<0017> <004C>
<001D> <0052>
<001F> <0054>
<0056> <003A>
<0059> <003D>
<016F> <002C>
<0170> <002E>
endbfchar
6 beginbfrange
<0005> <0007> <0033>
<000E> <0011> <0043>
<0019> <001A> <004E>
<0026> <0035> <0061>
<0037> <003C> <0072>
<003E> <003F> <0079>
endbfrange
endcmap
CMapName currentdict /CMap defineresource pop
end
end
'''

cmap = {
'0003':'0020',
'000C':'0041',
'0014':'0049',
'0017':'004C',
'001D':'0052',
'001F':'0054',
'0056':'003A',
'0059':'003D',
'016F':'002C',
'0170':'002E',
'0005':'0033',
'0006':'0034',
'0007':'0035',
'000E':'0043',
'000F':'0044',
'0010':'0045',
'0011':'0046',
'0019':'004E',
'001A':'004F',
'0026':'0061',
'0027':'0062',
'0028':'0063',
'0029':'0064',
'002A':'0065',
'002B':'0066',
'002C':'0067',
'002D':'0068',
'002E':'0069',
'002F':'006A',
'0030':'006B',
'0031':'006C',
'0032':'006D',
'0033':'006E',
'0034':'006F',
'0035':'0070',
'0037':'0072',
'0038':'0073',
'0039':'0074',
'003A':'0075',
'003B':'0076',
'003C':'0077',
'003E':'0079',
'003F':'007A',
}

def main():
    with open('pdf.txt') as f:
        lines = f.read()
    m = re.findall('<(....)>', lines)

    msg = ''
    for c in m:
        try:
            if cmap[c]:
                msg = msg + unichr(int(cmap[c], 16))
            else:
                msg = msg + unichr(int(c, 16))
        except KeyError:
            msg = msg + unichr(int(c, 16))

    print msg


if __name__ == '__main__':
    main()
