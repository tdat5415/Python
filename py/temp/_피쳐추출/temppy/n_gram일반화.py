with open('testfile/test3.hwp', 'rb') as h:
    s = h.read()

def n_gram_list(text, n):
    ng_list = []

    text_list = []
    for i in range(n):
        text_list.append(text[i:])


    n_gram_zip =zip(*text_list)
    for i in n_gram_zip:
        ng_list.append(i)

    return ng_list


for i in range(2,10):
    ng_list = n_gram_list(s, i)
    ng_set = set(ng_list)
    print('%d-gram 세트:\t'%i, len(ng_set))
    ng_set_pd = [n for n in list(ng_set) if n == n[::-1]]
    print('%d-gram 회문세트:\t'%i, len(ng_set_pd))

