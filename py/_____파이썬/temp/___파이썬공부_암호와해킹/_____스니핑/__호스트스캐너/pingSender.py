import os
from netaddr import IPNetwork, IPAddress
from socket import *
from threading import Thread


def sendPing(ip):
    try:
        ret = os.system('ping -n 1 %s' %ip) # 핑을 한번 보낸다.
    except Exception as e:
        print(e)


def main():
    host = gethostbyname(gethostname())
    subnet = host + '/24'
    for ip in IPNetwork(subnet):
        t = Thread(target=sendPing, args=(ip,))
        t.start()
        # 꼭 쓰레드 사용할것


if __name__ == '__main__':
    main()


# 다소 비효율적이고 느린 방법이지만 ..
