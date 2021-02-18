from socket import *
import os
# 스니핑을 한번 한다.

def sniffing(host):
    if os.name == 'nt': #윈도우인경우
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP

    sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    if os.name == 'nt': #윈도우인 경우
        sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
    packet = sniffer.recvfrom(65565)
    print(packet)

    if os.name == 'nt': #윈도우인 경우
        sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)


def main():
    host = gethostbyname(gethostname())
    print('START SNIFFING at [%s]' %host)
    sniffing(host)


if __name__ == '__main__':
    main()
