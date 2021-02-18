a = list(range(0,10))
print(a)
b = list(a) # 간단! # 객체는 다르면서 복사
print(b)
print(a is b)

c = list(range(0,10))
print(c)
d = c[::] # 간단! # 객체는 다르면서 복사
print(d)
print(c is d)
