import zipfile
from threading import Thread


def crackzip(zfile, passwd):
    try:
        zfile.extractall(pwd=passwd)
        print('ZIP file extracted successfully! PASS=[%s]' %passwd.decode())
        return True
    except:
        pass
    return False


def main():
    dictfile = 'dictionary.txt'
    zipfilename = 'locked.zip'
    zfile = zipfile.ZipFile(zipfilename, 'r')
    pfile = open(dictfile, 'r')
    for line in pfile.readlines():
        passwd = line.strip('\n')
        t = Thread(target=crackzip, args=(zfile, passwd.encode('utf-8')))
        t.start()

    

#locked.zip 파일이 없음
