url = '"http://www.naver.com/blog/ccc"'

tmp = url.split('/')
parent = '/'.join(tmp[0:-1])


print(parent)



print(url.split('http'))
print(url.strip('"'))
