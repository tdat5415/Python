words =["level", "SOS", "rotator", "nursesrun", "apple"]

for s in words:
    print(s == s[::-1])

'''
>>> word = 'level'
>>> list(word) == list(reversed(word))
True

>>> list(word)
['l', 'e', 'v', 'e', 'l']
>>> list(reversed(word))
['l', 'e', 'v', 'e', 'l']

>>> word = 'level'
>>> word == ''.join(reversed(word))
True

>>> word
'level'
>>> ''.join(reversed(word))
'level'
'''
