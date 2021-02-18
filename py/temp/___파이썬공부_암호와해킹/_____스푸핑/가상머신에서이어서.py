P = 853 # 딜

CP = 0.1 # 치확
CD = 0
.5 # 치피
A = 0.2# 민

A += 0.25
CP += A * 1
CD += 0.45
P *= 1 - 0.63


if CP > 1:
    CP = 1

print('P : %lf' %P)
print('CP : %lf' %CP)
print('CD : %lf' %CD)
print('A : %lf' %A)


res = (1 + (0.25+0.05*6)*CP) * 4 * (1+CP*CD) * P

print(res)
