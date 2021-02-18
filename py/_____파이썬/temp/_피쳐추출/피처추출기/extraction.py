import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import math


def features_to_csv(directory):
    file_list = os.listdir(directory)
    
    table = []
    for file_name in file_list:
        with open('%s/%s'%(directory, file_name), 'rb') as h:
            data = h.read()

        row = []
        row.append('%s'%file_name)

        features = get_n_gram_features(data, p = 6) # shape(65535)
        row.extend(features)
        
        table.append(row) # 한줄 추가
        print('%s\t피쳐추가'%file_name)
        #plt.imshow(two_grams, cmap='Greys', interpolation='nearest')
        #plt.show()

    
    attributes = []
    attributes.append('Name')
    for i in range(0, 256):
        for j in range(0, 256):
            attributes.append('%#x %#x'%(i, j))
        
    
    df = pd.DataFrame(table, columns=None)
    df.to_csv('./features.csv')
    print('csv만듦')


def get_n_gram_features(data, p = 6): # 6번 압축
    two_gram_list = n_gram_list(data, 2) # n-gram뽑기
    num_two_gram = count_two_gram(two_gram_list) # shape(256,256)
    scaled_num_two_gram = min_max_scaling(num_two_gram) # shape(256,256)
    features = pooling(scaled_num_two_gram, p) # shape(4,4)
    features = features.flatten() # shape(16)
    features = features.round(4) # 소수4번째서 반올림
    
    return features


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


def min_max_scaling(num_two_gram):
    num_two_gram = num_two_gram.flatten()
    num_two_gram = np.log(num_two_gram + 1) # 값차이가 너무커서log사용

    minx = min(num_two_gram)
    maxx = max(num_two_gram)
    #값이 크신분들 작게
    num_two_gram[0] = minx
    num_two_gram[-1] = minx
    minx = min(num_two_gram)
    maxx = max(num_two_gram)
    
    for i in range(len(num_two_gram)): # 0~1 사이 값으로 바꿔줌
        num_two_gram[i] = (num_two_gram[i] - minx) / (maxx - minx)
        
    scaled_num_two_gram = num_two_gram.reshape(256, 256)
   
    return scaled_num_two_gram


def pooling(gram, n):

    for k in range(n): # n번 압축
        gramlen = len(gram) // 2
        new_gram = np.array([0.0]*gramlen*gramlen)
        new_gram = new_gram.reshape(gramlen, gramlen)
        
        for i in range(gramlen):
            for j in range(gramlen):
                new_gram[i][j] = max(gram[2*i][2*j], gram[2*i][2*j+1], \
                                 gram[2*i+1][2*j], gram[2*i+1][2*j+1])
        gram = new_gram
    
    #plt.imshow(gram, cmap='Greys', interpolation='nearest')
    #plt.show()

    return gram
    

def main():
    directory = './testfile'
    features_to_csv(directory)

    
    

if __name__ == '__main__':
    main()
