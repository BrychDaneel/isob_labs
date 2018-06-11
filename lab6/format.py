import re

s = open('out.css').read()

s = re.sub('/\*.*?\*/', '', s)
s = re.sub('\s+', ' ', s)

open('out.css', 'w').write(s)
