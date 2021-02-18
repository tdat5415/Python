import random


tot =0
for i in range(0,100000):
	x1 =random.randint(0,100000)
	y1 =random.randint(0,100000)
	x2 =random.randint(0,100000)
	y2 =random.randint(0,100000)
	dst =((x1 -x2)**2 +(y1 -y2)**2)**(1/2)
	tot += dst
avg =tot/100000
print(avg/100000)
