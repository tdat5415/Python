x = input().split('\n')
key = x[0].split() # 한 줄 받고
x = input().split('\n') # 버퍼에 남아있는 한줄을 가져오나봄
val = list(map(float,x[0].split()))
dic = {}
for i in range(0,len(key)):
    dic[key[i]] = val[i] # for문으로 하나씩 넣어주기

print(dic)

'''두줄 드래그해서 넣을 것
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
'''
