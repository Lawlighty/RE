# 匹配一段文本中的每行的邮箱
import re
s = '123@qq.comaaa@163.combbb@126.netasdfasfs33333@adf.c'

p = '\w+@\w+\.[com,cn,net]{1,3}'

m = re.findall(p, s)
print(m)

email  = str(input('输入注册邮箱>'))
p = '^\w+@\w+\.[com,cn,net]{1,3}$'
if re.match(p,email):
    print('来了 老弟')
else:
    print('wdnmd  写的啥玩意儿')
