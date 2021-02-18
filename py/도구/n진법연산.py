m = 2**32




a = [0, 2, (2**32)-1, 2, 1]
a_tot = 0
for i in range(len(a)):
    a_tot += (m**i) * a[i]


b = [9, (2**32)-1, 9]
b_tot = 0
for i in range(len(b)):
    b_tot += (m**i) * b[i]


    
print((-a_tot) % b_tot)





c = [816043792, 4252017623, 7]
c_tot = 0
for i in range(len(c)):
    c_tot += (m**i) * c[i]


    
print(c_tot)

