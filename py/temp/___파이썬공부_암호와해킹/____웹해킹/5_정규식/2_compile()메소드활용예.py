import re

p = re.compile(r'href="(.*?)"')

text = '''<a href="help.html">Click Here for Help</a><font size="15">'''
ret = p.search(text)
print(ret.group(0))
