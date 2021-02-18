import random as rd

NUM = 23

cnt = 100000
tot = 0
for i in range(cnt):
    people = [rd.randint(1,365) for i in range(NUM)]
    len1 = len(people)
    len2 = len(set(people))
    if len1 != len2: # 생일이 겹친 사람이 있다.
        tot += 1

print('%d명 중 생일이 겹칠 확률 : %0.4lf' %(NUM,tot/cnt))

