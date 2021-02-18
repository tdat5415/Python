def print_numbers(*args): # (고정인수, 가변인수) 순서
    for arg in args:
        print(arg)

print_numbers(1,2,3,4)

_list =[5,6,7,8]
print_numbers(*_list)
