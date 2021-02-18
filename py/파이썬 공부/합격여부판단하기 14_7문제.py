s = list(map(int,input().split()))
for i in s:
    if i<0 or i>100:
        print('잘못된 점수')
        break
else: # for문을 무사통과하면 여기로
    if sum(s)/4 >= 80:
        print('합격')
    else:
        print('불합격')
