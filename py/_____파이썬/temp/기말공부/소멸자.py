class cla:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __del__(self):
        print('__del__실행')

def main():
    a = cla()
    a.__del__()#객체를 없애는 함수가 아님
    print('asfd')
    

if __name__ == '__main__':
    main()
