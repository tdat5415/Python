inp =int(input())

for i in range(1, inp +1):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
