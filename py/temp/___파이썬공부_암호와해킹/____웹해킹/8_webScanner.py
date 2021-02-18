from urllib.request import urlopen, Request, URLError, quote
from queue import Queue
from threading import Thread


user_agent = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; \
rv:11.0) like Gecko'


def webScanner(q, targethost, exts):
    while not q.empty():
        scanlist = []
        try:
            toscan = q.get_nowait() # q.get_nowait()로 바꾸고 예외처리문으로 고쳐야한
        except Exception:
            break
        if '.' in toscan: # FILE
            scanlist.append('%s' %toscan)
            for ext in exts:
                scanlist.append('%s%s' %(toscan, ext))
        else: # DIR
            scanlist.append('%s/' %toscan)

        for toscan in scanlist:
            url = '%s/%s' %(targethost, quote(toscan))
            try:
                req = Request(url)
                req.add_header('User-Agent', user_agent)
                res = urlopen(req)
                if len(res.read()):
                    print('[%d]: %s\n' %(res.code, url), end='')
                res.close()
            except URLError as e:
                pass


def main():
    targethost = 'http://209.202.254.90' #lycos.com
    wordlist = './all.txt'
    exts = ['~', '~1', '.back', '.bak', '.old', '.orig', '_backup']
    q = Queue()

    with open(wordlist, 'rt') as f:
        words = f.readlines()

    for word in words:
        word = word.rstrip()
        q.put(word)

    print('+++[%s] SCANNING START..' %targethost)
    for i in range(50):
        t = Thread(target=webScanner, args=(q, targethost, exts))
        t.start()


if __name__ == '__main__':
    main()
    

'''
all.txt에 있는 43,000여개의 모든 경로 및 팡리에 대해 접속하고, 접속에성공한
경로를 화면에 출력하는 코드입니다.
접속해야 할 사이트가 매우 많기 때문에 50개의 스레드를 구동하여 병렬 처리하도록구현.
네트워크 상황에 따라 스캔을 완료하는데 많은 시간이 소요될수 있음
'''
