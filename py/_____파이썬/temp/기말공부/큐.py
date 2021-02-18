class Queue(list):
    put = list.append
    def get(self):
        return self.pop(0)

def main():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q)

if __name__ == '__main__':
    main()
    
