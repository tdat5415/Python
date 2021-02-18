import numpy as np

B = np.array([3])
A = np.array([1, 2, 2])
B = np.append( B , [A] )

print(B)

B = np.append( B , 7 )#상위호환인듯

print(B)



print()

#############################

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))#왜있는거지
d = np.array([a,b])
print(c)
print(d)
##################################
print()

q = np.array([1,2])
w = np.array([9,8])
e = np.concatenate( (q , w) )#append하위
print(e)
