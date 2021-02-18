def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=' : ')

# def custom_print(a, b, *args, **kwargs) 요 순서이다
