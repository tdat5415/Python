a =list(range(1, 11))
b =list(filter(lambda x :3<x<8, a))
print(b)

# filter는 함수에 요소를 하나씩 넣어서 True가 나오는 것만 고른다.
