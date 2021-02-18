a = [1,'a',2,'b',3,'c',4,'d',5,'e']
print(a)
[a.pop(i) for i in reversed(range(len(a))) if type(a[i]) is not int]
print(a)

# b =[1,'a',2,'b',3,'c',4,'d',5,'e']
# print(b)
# [b.pop(i) for i in range(len(b)) if type(b[i]) is not int]
# print(b)

# pop 안은 인덱스

# 앞에서부터 검사하면 len(a)값이 작아져서 (즉 리스트가 줄어들어)
# 처음 넣었던 len(a)에 의해 리스트안을 벗어나 버린다
# 그래서 뒤에서부터 검사하면서  잘라나감 


a = [1,'a',2,'b',3,'c',4,'d',5,'e']
print(a)
a =[i for i in a if type(i) is not str]
print(a)
#왜이리 힘들게 했지
