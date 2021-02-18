keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))
x ={keys:values for keys, values in x.items() if keys != 'delta' and values != 30}
print(x)
'''
alpha bravo charlie delta echo foxtrot golf
30 40 50 60 70 80 90
'''
