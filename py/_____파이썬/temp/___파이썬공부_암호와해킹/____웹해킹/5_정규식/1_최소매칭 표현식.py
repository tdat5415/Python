import re

#pattern = r'href="(.*)"'
pattern = r'href="(.*?)"'

text = '''<a href="help.html">Click Here for Help</a><font size="15">'''
ret = re.search(pattern, text)
print(ret.group())
