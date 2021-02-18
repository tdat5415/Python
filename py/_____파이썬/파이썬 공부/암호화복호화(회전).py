

s = 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
rotation = 13
#atoz = 'abcdefghijklmnopqrstuvwxyz'
#AtoZ = atoz.upper()
#atoZ = atoz + AtoZ

for i in range(rotation):
    table = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz',
        'zabcdefghijklmnopqrstuvwxy')
    s = s.translate(table)
    table = str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'ZABCDEFGHIJKLMNOPQRSTUVWXY')
    s = s.translate(table)
    print(s)

print(s)
