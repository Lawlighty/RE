import re
key = r"<head><a>http://www.nsfbuhwe.com and https://www.auhfisna.com</a></head>"
p1 = '(https*://.*\.com)'

matcher = re.findall(p1, key)[0]
print(matcher)