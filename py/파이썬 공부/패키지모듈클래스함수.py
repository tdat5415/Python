from urllib.request import *
# urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져옴
req = Request('http://www.google.co.kr') # Request를 사용하여 req 생성
response = urlopen(req) # urlopen 함수 사용
print(response.status)
'''
참고로 urlopen함수에 URL을 바로 넣어도 되고,
Request('http://www.google.co.kr')와 같이
Request클래스에 URL을 넣은 뒤에 req를 생성해서
urlopen함수에 넣어도 됩니다.
'''
