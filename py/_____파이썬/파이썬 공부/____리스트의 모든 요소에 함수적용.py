a =[1, 2, 3, 4, 5]
print(a)

a[:] =map(lambda x:x**2,a) # a =list(map(lambda x:x**2, a))
print(a)
