def n_gram(text, n):
    ng_list = []

    text_list = []
    for i in range(n):
        text_list.append(text[i:])


    n_gram_zip =zip(*text_list)
    for i in n_gram_zip:
        ng_list.append(i)

    return ng_list



def main():
    sss = n_gram('hello', 2)
    print(sss)

if __name__ == '__main__':
    main()
