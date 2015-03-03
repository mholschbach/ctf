#!/usr/bin/python

import sys
from PIL import Image

im = Image.open(sys.argv[1])
pix = im.load()

#print im.size # 588,264
#print pix[0,0] # links oben
#print pix[im.size[0]-1,im.size[1]-1] #rechts unten
#print pix[17,28] #12er Reihe ganz links
#print pix[570,28] #12er Reihe ganz rechts
#print pix[17,48] #11er Reihe ganz links
#print pix[17,68] #0er Reihe ganz links
#print pix[17,248] #9er Reihe ganz links
#print pix[570,248] #9er Reige ganz rechts

punchdict = {
    '0-----------':'&',
    '-0----------':'-',
    '--0---------':'0',
    '---0--------':'1',
    '----0-------':'2',
    '-----0------':'3',
    '------0-----':'4',
    '-------0----':'5',
    '--------0---':'6',
    '---------0--':'7',
    '----------0-':'8',
    '-----------0':'9',
    '0--0--------':'a',
    '0---0-------':'b',
    '0----0------':'c',
    '0-----0-----':'d',
    '0------0----':'e',
    '0-------0---':'f',
    '0--------0--':'g',
    '0---------0-':'h',
    '0----------0':'i',
    '-0-0--------':'j',
    '-0--0-------':'k',
    '-0---0------':'l',
    '-0----0-----':'m',
    '-0-----0----':'n',
    '-0------0---':'o',
    '-0-------0--':'p',
    '-0--------0-':'q',
    '-0---------0':'r',
    '--00--------':'/',
    '--0-0-------':'s',
    '--0--0------':'t',
    '--0---0-----':'u',
    '--0----0----':'v',
    '--0-----0---':'w',
    '--0------0--':'x',
    '--0-------0-':'y',
    '--0--------0':'z',
    '----0-----0-':':',
    #'-----0----0-':'#',
    #'------0---0-':'@',
    '-------0--0-':'\'',
    '--------0-0-':'=',
    #'---------00-':'"',
    #'0---0-----0-':'`',
    '0----0----0-':'.',
    '0-----0---0-':'<',
    '0------0--0-':'(',
    #'0-------0-0-':'+',
    #'0--------00-':'|',
    '-0--0-----0-':'!',
    #'-0---0----0-':'$',
    #'-0----0---0-':'*',
    '-0-----0--0-':')',
    #'-0------0-0-':';',
    '-0-------00-':'^',
    #'--0-0-----0-':'~',
    #'--0--0----0-':',',
    #'--0---0---0-':'%',
    #'--0----0--0-':'_',
    #'--0-----0-0-':'>',
    '--0------00-':'?',
    '------------':' '}
    
card=""    
for x in range (1,81):
    punchline=""
    for y in range (1,13):
        if pix[10+x*7,8+y*20][0] < 100 :
            punchline+='0'
        else:
            punchline+='-'

    card = card+punchdict[punchline]
    #print punchline+" "+punchdict[punchline]

print sys.argv[1]+': '+card