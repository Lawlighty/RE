#转义字符的使用
import re

s = '(abc)def'
#匹配(abc)
m = re.findall('\(.*?\)', s)[0]
print(m)