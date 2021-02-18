import re


pattern = r'\w+' # \w : 숫자또는 영문자와 매치, + : 1회 이상반복
p = re.compile(pattern)

#text = '1Ag2d35    '
text = '      1Ag2d35    '

ret1 = p.match(text)
ret2 = p.search(text)

if ret1:
    print('match result:%s' %ret1.group())
if ret2:
    print('search result:%s' %ret2.group())
    

'''
match()는 주어진 문자열의 시작부터 일치하는지 검사하고,

search()는 문자열 내에 일치하는 패턴이 있는지 검사합니다.
'''
