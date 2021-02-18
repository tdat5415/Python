f = open('test.txt','w')
for j in range(2,10):
    for i in range(1,10):
        txt = '%d * %d = %d\n' % (j, i, j*i)
        f.write(txt)

f.close()
