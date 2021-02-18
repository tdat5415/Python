from queue import Queue
from threading import Thread
import time

q = Queue()
q.put(1)
q.put(2)
q.put_nowait(3) # 자리없으면 QueueFull Exception을 발생


print(q.get())
print(q.get())
print(q.get())
print(q.empty())
#print(q.get_nowait()) # 항목없으면 QueueEmpty Exception을 발생
print('what')

#####################################################################
l = []

def tttt(q, i):
    global l
    try:
        while True:
            v = q.get_nowait()
            l.append([v,i])
            time.sleep(0.01)
    except Exception:
        print('%d\n' %i, end='')


for i in range(300):
    q.put(i)

print(q.qsize())

for i in range(10):
    t = Thread(target=tttt, args=(q, i))
    t. start()

time.sleep(3)
print(l)


