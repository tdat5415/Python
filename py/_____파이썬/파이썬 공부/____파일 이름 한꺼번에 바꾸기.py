files = input().split()
print(["{0:0>3}.{1}".format(i.split('.')[0], i.split('.')[1]) for i in files])


files = input().split()
print(list(map(lambda x : "{0:0>3}.{1}".format(x.split('.')[0], x.split('.')[1]), files)))





files = input().split()

name =[i.split('.')[0] for i in files]
extension =[i.split('.')[1] for i in files]

name =["{0:0>3}".format(i) for i in name]

files =["{0}.{1}".format(name[i], extension[i]) for i in range(len(files))]

print(files)


# 1.jpg 10.png 11.png 2.jpg 3.png
