import ccrypt


def findPass(passhash, dictfile):
    salt = passhash[3:5]
    with open(dictfile, 'r') as dfile:
        for word in dfile.readlines():
            word = word.strip('\n')
            cryptwd = ccrypt.crypt(word, salt) #사전에 있던 단어와 salt 넣기
            if cryptwd == passhash[3:]:# 해쉬된 값이 해쉬비번과 일치하는지
                return word
    return ''


def main():
    dictfile = 'dictionary.txt'
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():#줄줄이 리스트
            data = line.split(':')
            user = data[0].strip()#공백제거
            passwd = data[1].strip()
            word = findPass(passwd, dictfile) # 한 비번에 사전공격
            if word:
                print('FOUND Password: \tID[%s] \tPassword [%s]' %(user, word))
            else:
                print('Password Not Found of \tID[%s]' %(user))

if __name__ == '__main__':
    main()
            
