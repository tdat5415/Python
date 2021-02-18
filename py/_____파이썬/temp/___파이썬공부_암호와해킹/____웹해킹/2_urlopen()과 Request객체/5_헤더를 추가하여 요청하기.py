from urllib.request import urlopen, Request


user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
url = 'http://www.google.com'
req = Request(url)
req.add_header('User-Agent', user_agent)
with urlopen(req) as h:
    print(h.read(100))


'''
User-Ahent 헤더는 요청하는 웹 브라우저의 종류를 지정합니다.

urllib 모듈은 디폴트User-Agent로 'Python-urllib/3.x'와 같은 문자열을 사용합니다.

그런데 일부 웹 사이트에서 User-Agent를 체크하여 통용되는 웹 브라우저에서

보내온 요청이 아니면 응답을 막아 놓은 경우가 있습니다.

위 예는 모질라 파이어폭스의 User-Agent를 실제 웹 브라우저인 것으로 변경하면

정상적으로 요청되어 응답 받을 수 있습니다.

위 예는 모질라 파이어폭스의 User-Agent 문자열을 이용하여 헤더를 구성한후

요청하는 예 입니다.
'''
