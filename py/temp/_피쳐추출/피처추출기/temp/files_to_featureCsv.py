import pandas as pd
import os

# workspace ┬ files_to_featureCsv.py
#           └ testfile ┬ test1.hwp
#                       ├ test2.hwp
#                       └ test3.hwp

# workspace에 hwpfeatures.csv 생성

extension_list = ['hwp', 'html', 'scr']

N = 10


def get_file_list(extension):
    if extension not in extension_list:
        raise Exception('가능한 확장자명을 입력하시오.')

    file_list = os.listdir('testfile/%s'%extension)
    file_list = [n for n in file_list if n.find('.%s'%extension)]
        
    return file_list


def features_to_csv(file_list, extension):
    if extension not in extension_list:
        raise Exception('가능한 확장자명을 입력하시오.')
    
    data = []
    for file in file_list:
        with open('testfile/%s/%s'%(extension,file), 'rb') as h:
            s = h.read()

        row_data = []
        row_data.append('%s'%file)
        for i in range(2, N):
            ng_list = n_gram_list(s, i)
            ng_set = set(ng_list)
            row_data.append(len(ng_set))
            
            ng_set_palin = [n for n in list(ng_set) if n == n[::-1]] # 회문만
            row_data.append(len(ng_set_palin))
            
        data.append(row_data)
        print('%s\t피쳐추가'%file)
    
    columns = []
    columns.append('Name')
    for i in range(2, N):
        columns.append('%d-gram'%i)
        columns.append('%d-palin'%i)
        
    
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('./%s_features.csv'%extension)
    print('csv만듦')


def n_gram_list(text, n): # 'text' -> [('t','e'), ('e','x'), ('x','t')]
    ng_list = []

    text_list = []
    for i in range(n):
        text_list.append(text[i:])


    n_gram_zip =zip(*text_list)
    for i in n_gram_zip:
        ng_list.append(i)

    return ng_list


def main():
    file_list = get_file_list('hwp')
    features_to_csv(file_list, 'hwp')
    

if __name__ == '__main__':
    main()
