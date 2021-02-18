from urllib.request import Request, urlopen


url = 'http://www.google.com'
DATA = None

h = urlopen(url, data=DATA)
#또는
h = urlopen(Request(url), data=DATA)


'''
data 인자에 데이터를 지정하게 되면 urlopen()은

HTTP POST 요청메시지를 생성하여 목적지 URL로 요청합니다.

Request()는 URL 요청을 추상화한 클래스이며

목적지 URL로 요청 헤더를 임의로 구성하여 전송할 수 있도록 해줍니다.
'''
