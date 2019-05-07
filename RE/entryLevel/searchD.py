import re
print('Search  匹配')
key = r"<html><body><h1>hello world<h1></body></html>"
p1 = '<body><h1>(.*?)<h1></body>'
mm = re.compile(p1)
matcher1 = re.search(mm,key).group()
print(matcher1)

print('findall  不带()')
key = r"<html><body><h1>hello world<h1></body></html>"
p1 = r"<h1>.*?<h1>"
pattern1 = re.compile(p1)
print (pattern1.findall(key)[0])

print('findall  带()')
key = r"<html><body><h1>hello world<h1></body></html>"
p1 = '<body><h1>.*?<h1></body>'
pattern1 = re.compile(p1)
print (pattern1.findall(key)[0])


