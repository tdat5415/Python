def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
# 양옆 하나씩 줄여 들어간다
# 길이가 0또는1이면 True로 함수를 계속 나간다.return(return(return True)))이런식
# 길이가 2이상인 동안은 양옆 하나씩 검사해 들어간다. False인 순간 계속 나간다.

print(is_palindrome('hello'))
print(is_palindrome('level'))
