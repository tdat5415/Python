import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import math

# workspace ┬ files_to_featureCsv.py
#           └ testfile ┬ test1.hwp
#                       ├ test2.hwp
#                       └ test3.hwp

# workspace에 hwpfeatures.csv 생성

extension_list = ['hwp', 'html', 'scr']



def get_file_list(extension):
    #if extension not in extension_list:
    #    raise Exception('가능한 확장자명을 입력하시오.')

    file_list = os.listdir('testfile/%s'%extension)
    file_list = [n for n in file_list if n.find('.%s'%extension)]
        
    return file_list


def features_to_csv(file_list, extension):
    #if extension not in extension_list:
    #    raise Exception('가능한 확장자명을 입력하시오.')
    
    data = []
    for file in file_list:
        with open('testfile/%s/%s'%(extension,file), 'rb') as h:
            s = h.read()

        row_data = []
        row_data.append('%s'%file)
    
        ng_list = n_gram_list(s, 2)#n-gram뽑기
        two_grams = count_two_gram(ng_list) # shape(256,256)

        
        two_grams = min_max_scaling(two_grams, 2)###0~1사이 값으로 바꾸기

        for i in range(0, 256):
            for j in range(0, 256):
                row_data.append(two_grams[i][j])
            
            
        data.append(row_data)
        print('%s\t피쳐추가'%file)
        #plt.imshow(two_grams, cmap='Greys', interpolation='nearest')
        #plt.show()

    
    columns = []
    columns.append('Name')
    for i in range(0, 256):
        for j in range(0, 256):
            columns.append('%#x %#x'%(i, j))
        
    
    #df = pd.DataFrame(data, columns=columns)
    #df.to_csv('./%s_features3.csv'%extension)
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


def count_two_gram(two_gram_list):
    num_two_gram = [[0]*256 for i in range(256)]
    num_two_gram = np.array(num_two_gram)

    for i,j in two_gram_list:
        num_two_gram[i][j] += 1

    return num_two_gram


def min_max_scaling(grams, n):
    np_arr = np.array(grams)
    np_arr = np_arr.reshape(256**n)
    new_np_arr = np.array([0.0]*(256**n))

    base = 500000
    new_np_arr = np.log(new_np_arr + 1) #/ np.log(base)
    
    minx = min(np_arr)
    maxx = max(np_arr)

    #값이 크신분들 
    np_arr[0] = minx
    np_arr[-1] = minx

    minx = min(np_arr)
    maxx = max(np_arr)

    
    for i in range(len(np_arr)):
        new_np_arr[i] = (np_arr[i] - minx) / (maxx - minx)

    #s = list(new_np_arr)
    #s.sort(reverse=True)
    #print(s[:50])

    new_np_arr = new_np_arr.reshape(256, 256)
    
    pooling(new_np_arr, 6)

    return new_np_arr


def pooling(grams, n):
    arr = grams

    for k in range(n):#3번 압축
        arrlen = len(arr)//2
        arr2 = np.array([0.0]*arrlen*arrlen)
        arr2 = arr2.reshape(arrlen, arrlen)
        
        for i in range(arrlen):
            for j in range(arrlen):
                arr2[i][j] = max(arr[2*i][2*j], arr[2*i][2*j+1], \
                                 arr[2*i+1][2*j], arr[2*i+1][2*j+1])
        arr = arr2
    
    plt.imshow(arr, cmap='Greys', interpolation='nearest')
    plt.show()
    print(arr)
    

def main():
    extension = 'hwp'
    file_list = get_file_list(extension)
    features_to_csv(file_list, extension)

    
    

if __name__ == '__main__':
    main()
