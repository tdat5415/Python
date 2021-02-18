lines1 =['안녕하세요\n', '반가워요\n', '그럼이만\n']
with open('intro.txt','w') as file:
    file.writelines(lines1)

with open('intro.txt','r') as file:
    lines2 =file.readlines()

print(lines2)
