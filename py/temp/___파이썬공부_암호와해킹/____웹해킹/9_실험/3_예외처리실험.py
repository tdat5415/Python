def test():
    raise Exception('error')



try:
    print('1')
    try:
        print('2')
        test()
    except Exception:
        pass#print('e2')
except Exception:
    print('e1')


print('3')
