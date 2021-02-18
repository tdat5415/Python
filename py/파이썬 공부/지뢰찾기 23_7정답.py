col, row = map(int,input().split(' ')) # 행 열 
matrix = []
for i in range(row): # 열
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            cnt = 0
            for r in [y for y in range(i-1,i+2) if 0 <= y < row] :
                for c in [x for x in range(j-1,j+2) if 0 <= x < col] :
                    if matrix[r][c] == '*' : cnt+=1
            matrix[i][j] = cnt
for i in matrix:
    for j in i:
        print(j,end='')
    print()
    
