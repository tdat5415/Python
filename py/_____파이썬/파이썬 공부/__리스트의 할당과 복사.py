a = [0,0,0,0,0]
print('a = ',a)
b = a # 이러면 객체 자체가 같다.
print('b에 a를 할당함')
print('a is b ? ',a is b) # True
print('a == b ? ',a == b) # True
b[2] = 99
print('b[2]에 99를 할당함')
print('a = ',a)
print('b = ',b)

c = [0,0,0,0,0]
print('c = ',c)
d = c.copy() # 이러면 객체는 다르지만 내용은 같다.
print('d에 c를 복사함')
print('c is d ? ',c is d) # True
print('c == d ? ',c == d) # False
d[2] = 99
print('d[2]에 99를 할당함')
print('c = ',c)
print('d = ',d)
