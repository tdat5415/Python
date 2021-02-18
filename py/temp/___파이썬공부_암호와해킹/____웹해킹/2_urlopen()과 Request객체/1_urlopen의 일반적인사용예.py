from urllib.request import Request, urlopen


url = 'http://www.google.com'

h = urlopen(url)
#또는
h = urlopen(Request(url))


'''
urlopen()은 HTTP GET 요청 메시지를 자동적으로 생성하고 목적지 url로 요청합니다.

만약 웹 서버로 HTTP 요청을 할때, 로그인 정보와 같이 전송할 데이터가 있을 경우는

urlopen()의 data인자에 데이터를 지정하면 됩니다.
'''
