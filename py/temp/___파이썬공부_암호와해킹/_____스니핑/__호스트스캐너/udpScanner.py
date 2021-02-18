from socket import *
import os
import struct


def parse_ipheader(data): # IP헤더에서 필드 데이터 추출하기
    ipheader = struct.unpack('!BBHHHBBH4s4s', data[:20])
    return ipheader


def getDatagramSize(ipheader): # 데이터그램크기 추출하기
    return ipheader[2]


def getProtocol(ipheader): # 프로토콜 추출하
    protocols = {1:'ICMP', 6:'TCP', 17:'UDP'}
    proto = ipheader[6]
    if proto in protocols:
        return protocols[proto]
    else:
        return 'OTHERS'


def getIP(ipheader): # IP 주소 추출하기
    src_ip = inet_ntoa(ipheader[8])
    dest_ip = inet_ntoa(ipheader[9])
    return (src_ip, dest_ip)


def getIPHeaderLen(ipheader):
    ipheaderlen = ipheader[0] & 0x0f
    ipheaderlen *= 4
    return ipheaderlen


def getTypeCode(icmp):
    icmpheader = struct.unpack('!BB', icmp[:2])
    icmp_type = icmpheader[0]
    icmp_code = icmpheader[1]
    return (icmp_type, icmp_code)


def recvData(sock):
    data = ''
    try:
        data = sock.recvfrom(65565)
    except timeout:
        data = ''
    return data[0]


def sniffing(host):
    if os.name == 'nt':
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))

    sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    if os.name == 'nt':
        sniffer.ioctl(SIO_RCVALL, RCVALL_ON)

    count = 1
    try:
        while True:
            data = recvData(sniffer)
            ipheader = parse_ipheader(data[:20])
            ipheaderlen = getIPHeaderLen(ipheader)
            
            
            #datagramSize = getDatagramSize(ipheader)
            protocol = getProtocol(ipheader)
            src_ip, dest_ip = getIP(ipheader)
            if protocol == 'ICMP':
                offset = ipheaderlen
                icmp_type, icmp_code = getTypeCode(data[offset:])
                if icmp_type == 3 and icmp_code == 3:
                    # 타입3 : Destination Unreachable 일단은 목적지 도착못함
                    # 코드3 : Port Unreachable 포트에 도달 못함
                    #                   (호스트에는 왔는데 포트가 닫혀있는?)
                    print('%s -> %s: ICMP: %s'\
                          %(src_ip, dest_ip, data[-12:])) #KNOCK!KNOCK! 길이
                #elif icmp_type == 3 and icmp_code == 1:
                #    print('%s -> %s: ICMP: Destination Host Unreachable'\
                #          %(src_ip, dest_ip))
                
    except KeyboardInterrupt: #Ctrl-C key input
        if os.name == 'nt':
            sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)


def main():
    host = gethostbyname(gethostname())
    print('START SNIFFING at [%s]' %host)
    sniffing(host)


if __name__ == '__main__':
    main()
