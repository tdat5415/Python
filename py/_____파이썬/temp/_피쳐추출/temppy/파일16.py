with open('testfile/test.png', 'rb') as h:
    s = h.read()

#print(s)

s1 = []
s2 = []
s3 = []

text = s

two_gram =zip(text, text[1:])
for i in two_gram:
    s1.append(i)

three_gram =zip(text, text[1:], text[2:])
for i in three_gram:
    s2.append(i)

four_gram =zip(text, text[1:], text[2:], text[3:])
for i in four_gram:
    s3.append(i)


s1 = set(s1)
print('2-gram 세트 :',len(s1))

l1 = [n for n in list(s1) if n == n[::-1]]
print('2-gram 회문세트 :',len(l1))


s2 = set(s2)
print('3-gram 세트 :',len(s2))

l2 = [n for n in list(s2) if n == n[::-1]]
print('3-gram 회문세트 :',len(l2))


s3 = set(s3)
print('4-gram 세트 :',len(s3))

l3 = [n for n in list(s3) if n == n[::-1]]
print('4-gram 회문세트 :',len(l3))
