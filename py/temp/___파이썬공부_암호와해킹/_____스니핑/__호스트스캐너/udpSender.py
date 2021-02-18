from socket import *
from netaddr import IPNetwork, IPAddress

def sendMsg(subnet, msg):
    sock = socket(AF_INET, SOCK_DGRAM)
    for ip in IPNetwork(subnet):
        try:
            if '%s' %ip != '192.168.0.2':
                continue
            print('SENDING MESSAGE to [%s]' %ip)
            sock.sendto(msg.encode('utf-8'), ('%s' %ip, 9000))
            #sendto는 udp소켓통신의 함수   # 포트번호 9000
            if '%s' %ip == '192.168.0.2':
                break
        except Exception as e:
            print(e)


def main():
    host = gethostbyname(gethostname())
    subnet = host + '/24'
    msg = 'KNOCK!KNOCK!'
    sendMsg(subnet, msg)


if __name__ == '__main__':
    main()


# 192.168.0.2 -> 192.168.0.2: ICMP: Type[3], Code[1]
# ICMP 타입 3의 하위 코드 값 1은 Destination Host Unreachable을 뜻합니다.
# D.H.U은 게이트웨이 설정이 잘못되었거나
# 라우터에서 목적지로 가는 경로를 찾지 못할 때
# PC자체 또는 라우터에서 생성하는 ICMP메시지입니다.

# sniffer3.py를 약간 수정해서 ICMP타입과 코드값이 각각 3, 3인 경우
# ICMP메시지가 KNOCK KNOCK인지 확인하면된다.
# ICMP 메시지는 ICMP패킷의 맨 마지막 부분입니다.
# 변수data가 ICMP패킷이고 'KMOCK!KMOCK!'의 길이는 12이므로
# data[-12:]의 값을 확인하면 됩니다.
