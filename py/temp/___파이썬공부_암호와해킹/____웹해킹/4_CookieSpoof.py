from urllib.request import urlopen, Request


user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
cookie = 'NID=1234; expires=Thu, 25-Aug-2016 06:26:36 GMT; path=/; \
domain=.google.co.kr; HttpOnly' # 조작하려는 쿠키 문자열


def cookieSpoof(url):
    req = Request(url)
    req.add_header('User-Agent', user_agent)
    req.add_header('Cookie', cookie)
    with urlopen(req) as h:
        print(h.read())


def main():
    url = 'http://www.google.com'
    cookieSpoof(url)


if __name__ == '__main__':
    main()



'''
쿠키 문자열은 'NID='로 시작하여 'HttpOnly'로 끝납니다.

만약 NID의 값을 '1234'로 조작하여 요청하는 코드를 작성하고 싶다면

위 코드와 비슷한 코드가 됩니다.
'''
