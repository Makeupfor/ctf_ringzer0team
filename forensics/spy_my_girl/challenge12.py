hidmap = {4:'a',5:'b',6:'c',7:'d',8:'e',9:'f',10:'g',
11:'h',12:'i',13:'j',14:'k',15:'l',16:'m',17:'n',18:'o',19:'p',20:'q',
21:'r',22:'s',23:'t',24:'u',25:'v',26:'w',27:'x',28:'y',29:'z',30:'1',
31:'2',32:'3',33:'4',34:'5',35:'6',36:'7',37:'8',38:'9',39:'0',40:'<ENTER>',
41:'<ESCAPE>',42:'<DELETE>',43:'<TAB>',44:'<SPACEBAR>',45:'-',46:'=',
47:'[',48:']',49:'\\',50:'#',51:';',52:'\'',53:'`',54:',',55:'.',56:'/',
}

def main():
    a = ''
    with open('keyboard.txt') as f:
        for line in f.read().splitlines():
            coords = line.split(':')
            key1 = int(coords[2], 16)
            try:
                a = a + hidmap[key1]
            except KeyError:
                pass
    print  a

if __name__ == '__main__':
    main()
