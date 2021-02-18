
def n_gram_list(text, n): # 'text' -> [('t','e'), ('e','x'), ('x','t')]
    ng_list = []

    text_list = []
    for i in range(n):
        text_list.append(text[i:])

    n_gram_zip =zip(*text_list)
    for i in n_gram_zip:
        ng_list.append(i)

    return ng_list


if __name__ == '__main__':
    s = n_gram_list(b'text', 2)
    print(s)
