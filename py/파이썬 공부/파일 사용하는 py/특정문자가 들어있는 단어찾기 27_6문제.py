import string
_str ='''Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'''

with open('words.txt','w') as file:
    file.write(_str)

with open('words.txt','r') as file:
    _list =file.read().split()

for s in _list:
    if(s.count('c')):
        print(s.strip(string.punctuation))
