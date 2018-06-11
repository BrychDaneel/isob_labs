import re

s = open('styles.css').read()

s = s.replace('\n\n', '\n', 4)

s = s.replace('\n\n',
"""\n
.register {
  width: 20px;
  height: 20px;}
  .register a{
    text-decoration: none;
    border-radius: 5px;
    color: rgba(225, 32, 0, 0.8);}\n"""
  , 1
)

s = s.replace('\n\n', '\n', 4)


s = s.replace('\n\n',
"""\n
main .login {
    width: 20px;
    height: 20px;
    background: rgba(224, 134, 124, 0.5);
    color: rgba(200, 62, 255, 0.8);}"""
    , 1
)

open('out.css', 'w').write(s)
