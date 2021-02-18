key = input().split() # 한 줄 받고
val = list(map(float,input().split()))# 버퍼에 남아있는 한줄을 가져오나봄
dic = dict(zip(key,val))
print(dic)

'''두줄 드래그해서 넣을 것
health health_regen mana mana_regen
575.6 1.7 338.8 1.63
'''

'''
>>> z =[[1, 'a'],[2, 'b'],[3, 'c']]
>>> z
[[1, 'a'], [2, 'b'], [3, 'c']]
>>> dic ={}
>>> dic =dict(z)
>>> dic
{1: 'a', 2: 'b', 3: 'c'}
'''
