class Stack(list):
    push = list.append

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.pop())
    print(s.pop())

if __name__ == '__main__':
    main()
