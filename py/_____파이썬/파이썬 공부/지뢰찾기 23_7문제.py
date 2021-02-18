col, row = map(int,input().split(' ')) # 행 열 
matrix = []
for i in range(row): # 열
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            cnt = 0
            if 0<=i+1<row and 0<=j+1<col and matrix[i+1][j+1] == '*': cnt+=1
            if 0<=i+1<row and 0<=j-1<col and matrix[i+1][j-1] == '*': cnt+=1
            if 0<=i+1<row and 0<=j<col and matrix[i+1][j] == '*': cnt+=1
            if 0<=i-1<row and 0<=j+1<col and matrix[i-1][j+1] == '*': cnt+=1
            if 0<=i-1<row and 0<=j-1<col and matrix[i-1][j-1] == '*': cnt+=1
            if 0<=i-1<row and 0<=j<col and matrix[i-1][j] == '*': cnt+=1
            if 0<=i<row and 0<=j+1<col and matrix[i][j+1] == '*': cnt+=1
            if 0<=i<row and 0<=j-1<col and matrix[i][j-1] == '*': cnt+=1
            matrix[i][j] = cnt
for i in matrix:
    for j in i:
        print(j,end='')
    print()
    
