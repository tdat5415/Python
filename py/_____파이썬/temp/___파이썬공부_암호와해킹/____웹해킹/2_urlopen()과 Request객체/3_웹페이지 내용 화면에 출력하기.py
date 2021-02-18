from urllib.request import urlopen

url = 'http://www.google.com'
with urlopen(url) as h:
    print(h.read())


#이 코드를 실행하면 구글 홈페이지의 HTML 내용이 화면에 출력됩니다.

    
