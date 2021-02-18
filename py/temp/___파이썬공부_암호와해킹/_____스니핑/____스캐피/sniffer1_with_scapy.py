from scapy.all import *


def showPacket(packet):
    print(packet.show())


def main(filter):
    sniff(filter = filter, prn = showPacket, count = 1)
    # prn :  캡처한 패킷을 처리하기 위하 함수를 지정


if __name__ == '__main__':
    filter = 'ip'
    main(filter)
