from threading import Thread
import time


def run_threads(func, args, num=5):
    threads = []
    for i in range(num):
        t = Thread(target=func, args=args)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def sss(s):
    time.sleep(s)

print('start')
run_threads(sss, (2,))
print('end')

'''
#수직(스택)모양 다중쓰레드
def multi_thread(func, n, s):
    if n <= 0:
        return

    t = Thread(target=func, args=(s,n))
    t.start()
    multi_thread(func, n-1, s)
    t.join()
    print('%d is finished\n' %n, end='')


def sss(s,n):
    print('%d is sleeping\n' %n, end='')
    time.sleep(s)


print('start')

t = Thread(target=multi_thread, args=(sss, 10, 3))
t.start()
t.join()

print('end')
'''

'''
#수평모양 다중쓰레드
def multi_thread(func, n, s):
    if n <= 0:
        return
    
    t = Thread(target=multi_thread, args=(func, n-1, s))
    t.start()
    func(s, n)
    print('%d is wakeuped\n' %n, end='')
    t.join()
    print('%d is finished\n' %n, end='')


def sss(s,n):
    print('%d is sleeping\n' %n, end='')
    time.sleep(s)


print('start')

t = Thread(target=multi_thread, args=(sss, 10, 3))
t.start()
t.join()

print('end')
'''



