text ='hello'

_N =2

for i in range(len(text) -_N +1):
    for j in range(_N):
        print(text[i +j], end='')
    print()



text ='this is python script'
words =text.split()

_N =2

for i in range(len(words) -_N +1):
    for j in range(_N):
        print(words[i +j], end=' ')
    print()
