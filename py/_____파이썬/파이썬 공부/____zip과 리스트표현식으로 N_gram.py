text = 'hello'

_N =3
_list =[text[i:] for i in range(_N)]
N_gram =zip(*_list)

for i in N_gram:
    for j in i:
        print(j, end='')
    print()
