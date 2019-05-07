#匹配重复出现字符    abcxxxxabc
import re

s = 'allochirallyyanticovenantingbarbary'
p = '((\w{3}).*\\2)'
m = re.findall(p, s)

list = []
for i in m:
    word = i[0]
    list.append(word)

print(list)