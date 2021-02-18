text ='''apache
decal
did
neep
noon
refer
river'''

with open('words.txt','w') as file:
    file.write(text)

with open('words.txt','r') as file:
    words =file.read().split('\n')

for s in words:
    if(s == s[::-1]):
        print(s)
