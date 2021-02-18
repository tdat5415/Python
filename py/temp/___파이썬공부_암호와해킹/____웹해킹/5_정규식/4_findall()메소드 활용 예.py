import re


html_page = \
          '''
</head>
<body><center>
<div>
<h3>PICTURE</h3><br>
<img src="/static/images/2015-08-25_234806.jpg"/>
<img src="/static/images/2015-08-25_234836.jpg"/>
<img src="/static/images/2015-08-25_234910.jpg"/>'''

text = 'href=abbr_view.php?opt=search&m_first_letter=1&m_search=O asdf>O</a>'

#pattern = r'src=\S+"' # 화이트 스페이스가 아닌문자 1회이상반복
pattern = r'src=([\S]+)"' # 화이트 스페이스가 아닌문자 1회이상반복
#pattern = r'src=[^\s]+"' # 화이트 스페이스가 아닌문자 1회이상반복
#pattern = r'src="(.*?)"'
pattern = r'href=(\S+?)>'

p = re.compile(pattern)
ret = p.findall(html_page)
ret = p.findall(text)


print(ret)
if ret:
    for r in ret:
        print(r)


# findall()메소드를 이용해 웹 페이지에서 모든 이미지 링크 URL을 추출하기위한 코드
