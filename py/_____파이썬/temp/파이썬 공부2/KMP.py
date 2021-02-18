def makeTable(pattern):
    table = []
    table.append(0)
    j = 0
    for i in range(1,len(pattern)):
        table.append(0)
        while j>0 and (pattern[i] != pattern[j]):
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1 #그 다음 값을 넣은다 나중에 해당 인덱스 부터 비교
            table[i] = j
    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    j = 0
    for i in range(0,len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1] #j - 1까지는 맞았으니 
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                print("%d번째에서 찾음" %(i - len(pattern) + 2))
                j = table[j]
            else:
                j += 1
    

parent = 'asdfaababaabccafasdf'
pattern = 'ababaabc'

print(makeTable(pattern))
KMP(parent, pattern)



