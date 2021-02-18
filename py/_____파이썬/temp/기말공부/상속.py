class Base:
    a = 10
    def f(self):
        print ('base')

class Derived(Base):
    #파생클래스 : 부모 클래스(속성, 메소드) 상속
    def g(self):
        print('derived')

def main():
    x = Base()
    x.f()
    y = Derived()
    y.f()
    y.g()

if __name__ == '__main__':
    main()
