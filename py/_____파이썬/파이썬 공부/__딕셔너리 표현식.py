keys =['a', 'b', 'c', 'd']
x ={keys : values for keys, values in dict.fromkeys(keys).items()}
print(x)
