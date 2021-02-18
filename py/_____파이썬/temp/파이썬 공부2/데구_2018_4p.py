
def permute(a, s, l):
    if s == l:
        for i in range(0,l):
            x = a[i]
            print(x, end='')
        print()
        return True
    else:
        for i in range(s,l):
            a[i], a[s] = a[s], a[i]
            b = permute(a,s+1,l)
            a[i], a[s] = a[s], a[i]

    return b


l = 4

a = list(range(0,l))

permute(a, 0, l)
print(a)
