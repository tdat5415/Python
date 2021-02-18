from urllib.request import urlopen


url = 'http://www.google.com'
with urlopen(url) as h:
    print(h.geturl())   # 실제로 응답한 URL
    print('+++++++++++')
    print(h.info())     # 헤더 등과 같은 페이지의 메타 정보
    print('+++++++++++')
    print(h.getcode())  # HTTP 응답 코드
