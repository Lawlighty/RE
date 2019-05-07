# 匹配一段文本中的每行的时间字符串，比如：‘1990-07-12’
import re

s = 'asfasf1990-07-12asdfAAAbbbb4342411997-12-28001-032-11-23'
p = '\d{4}-\d{2}-\d{2}'
m = re.findall(p, s)
print(m)