def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

# 참고로 print 함수에서 사용했던 sep, end도 키워드 인수입니다.
