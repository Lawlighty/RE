import re

phone = "1*5*1*1*0*3*3*6*4*9*1 #美女发来的电话号码"
patt = '\D'

mat = re.sub(patt, '',phone)
print(mat)