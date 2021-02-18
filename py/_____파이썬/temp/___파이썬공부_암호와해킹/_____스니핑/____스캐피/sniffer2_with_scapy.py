from scapy.all import *


protocols = {1:'ICMP', 6:'TCP', 17:'UDP'}


def showPacket(packet):
    src_ip = packet[0][1].src # 또는 packet[IP].src
    dst_ip = packet[0][1].dst # 또는 packet[IP].dst
    proto = packet[0][1].proto # 또는 packet[IP].proto

    if proto in protocols:
        print('PROTOCOL: %s:\t%s\t-> %s' %(protocols[proto], src_ip, dst_ip))
        if proto == 1: # ICMP인가
            print('TYPE:[%d], CODE:[%d]'%(packet[0][2].type, packet[0][2].code))


def main(filter):
    sniff(filter = filter, prn = showPacket, count = 0)


if __name__ == '__main__':
    filter = 'ip'
    main(filter)


# packet : sniff()가 캡처한 패킷입니다. prn인자로 지정된 함수의 인자로 전달합니다.
# packet[0][0] : MAC 주소 계층입니다.
# packet[0][1] : IP 계층입니다. packet[IP]로도 접근 가능합니다.
# packet[0][2] : TCP, UDP, ICMP 계층입니다. 각각 packet[~~~]로 접근 가능합니다.
