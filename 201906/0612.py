import re
aaa = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(aaa.findall('123-456-7890, and 098-765-4321'))
bbb = re.compile(r'(Yeet){3,5}')
print(bbb.search('YeetYeetYeetYeet'))