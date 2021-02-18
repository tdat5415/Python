_str ='''anonymously
compatibility
dashboard
experience
photography
spotlight
warehouse'''

with open('words.txt','w') as file:
    file.write(_str)

with open('words.txt','r') as file:
    sss =file.read().split('\n')

#print(sss)
cnt =0
for s in sss:
    if(len(s) <=10): cnt +=1
print(cnt)
