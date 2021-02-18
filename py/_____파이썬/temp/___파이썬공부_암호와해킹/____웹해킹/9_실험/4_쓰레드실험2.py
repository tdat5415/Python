from threading import Thread
from threading import Lock
import time

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()


def run_threads(func, args, num=5):
    threads = []
    for i in range(num):
        t = Thread(target=func, args=args)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def sss(s):
    global lock1, lock2, lock3

    lock1.acquire() # 마리오의 ON/OFF 장애물같음
    print('1\n', end='')
    time.sleep(s)
    lock1.release()
    
    lock2.acquire()
    print('2\n', end='')
    time.sleep(s)
    lock2.release()
    
    lock3.acquire()
    print('3\n', end='')
    time.sleep(s)
    lock3.release()

#def ss():
#    time.sleep(3)
#    print('waked up')

print('start')
#t = Thread(target=ss, args=())
#t.start()
run_threads(sss, (1,))
print('end')
