text = 'hello'

two_gram =zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')


text = 'this is python script'
words = text.split()
two_gram =zip(words, words[1:])
for i in two_gram:
    print(i[0], i[1])
