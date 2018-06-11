import re
import random

s = open('out.css').read()

s = s.replace('white', '#FFFFFF')
s = s.replace('black', '#000000')
s = s.replace('red', '#FF0000')
s = s.replace('green', '#00FF00')
s = s.replace('blue', '#0000FF')

for st in re.findall('#[0-9a-f]{6}', s):
    r = int(st[1:3], 16)
    g = int(st[3:5], 16)
    b = int(st[5:7], 16)
    s = re.sub(st, 'rgba({},{},{},1)'.format(r,g,b), s)


for st in re.findall(r'([^h.0-9-])(-?\d+)(\.\d+)?(.)', s):
    ss = st[1] + st[2]
    a = float(ss) #* (0.99 + random.random() / 100)
    aa = float(ss) * (0.99 + random.random() / 100)
    if (st[3] == 'e' or st[3] == 'p' or st[3] == '%'):
        repl = '{}{:.7}{}'.format(st[0], aa, st[3])
        s = s.replace(st[0]+ss+st[3], repl)


open('out.css', 'w').write(s)
