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


def getIP(ipheader): # IP 주소 추출하
    src_ip = inet_ntoa(ipheader[8])
    dest_ip = inet_ntoa(ipheader[9])
    return (src_ip, dest_ip)


def recvData(sock):
    data = ''
    try:
        data = sock.recvfrom(65565)
    except :#timeout:
        print('0')
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
            
            datagramSize = getDatagramSize(ipheader)
            protocol = getProtocol(ipheader)
            src_ip, dest_ip = getIP(ipheader)
            
            print('\nSNIFFERD [%d] ++++++++++' %count)
            print('Datagram Size:\t%s' %str(datagramSize))
            print('Protocol:\t%s' %protocol)
            print('Source IP:\t%s' %src_ip)
            print('Destination IP:\t%s' %dest_ip)
            count += 1
    except KeyboardInterrupt: #Ctrl-C key input
        if os.name == 'nt':
            sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)


def main():
    host = gethostbyname(gethostname())
    print('START SNIFFING at [%s]' %host)
    sniffing(host)


if __name__ == '__main__':
    main()
