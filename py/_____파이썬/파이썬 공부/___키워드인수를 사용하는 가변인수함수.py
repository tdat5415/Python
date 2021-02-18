def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ' : ', arg)

personal_info(name ='홍길동', age =30)

x ={'name' :'홍길동', 'age' :30, 'address' :'서울시 용산구 이촌동'}
personal_info(**x)

# **kwargs -> kwargs  는  age =30 -> {age :30}
# x -> **x  는  {age :30} -> age =30 이니까
