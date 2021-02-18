a = [[10, 20],[30, 40],[50, 60]]
# 반복문 한번 사용하기
for x, y in a: # 언패킹!
    print(x, y)

# 반복문 두번 사용하기
for i in a:
    for j in i:
        print(j, end=' ')
    print()

# for와 range 사용하기
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

    
