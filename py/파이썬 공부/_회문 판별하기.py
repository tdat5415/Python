_list =["level", "SOS", "rotator", "nursesrun","apple"]

for s in _list:
    is_palindrome =True
    for i in range(len(s)//2):
        if(s[i] != s[-1 -i]):
            is_palindrome =False
            break
    print(is_palindrome)
