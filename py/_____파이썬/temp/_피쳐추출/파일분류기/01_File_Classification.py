#!/usr/bin/env python
# coding: utf-8

# In[2]:


# by Kyoung-Seok kim

import csv
import os
import pandas as pd
import pefile
import shutil
import sys

from openpyxl import load_workbook

####################################################################################################
# 파일 시그니쳐 목록
signatures = {
    'PE'   : [0x4D, 0x5A],
    'HWP'  : [0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1],
    'HTML' : [0x3C, 0x21, 0x64, 0x6F, 0x63, 0x74, 0x79, 0x70],
    'DOCX' : [0x50, 0x4B, 0x03, 0x04]
    }

####################################################################################################
# 데이터셋 경로 설정
path_dataset            = 'Dataset' + os.sep
path_dataset_2018_train = path_dataset + '01. 2018_TrainSet' + os.sep
path_dataset_2018_qual1 = path_dataset + '02. 2018_예선_1차' + os.sep
path_dataset_2018_qual2 = path_dataset + '03. 2018_예선_2차' + os.sep
path_dataset_2019_train = path_dataset + 'KISA-challenge2019-Malware_trainset' + os.sep + 'KISA-challenge2019-Malware_trainset' + os.sep + 'trainSet' + os.sep

####################################################################################################
# 정답지 경로 설정
path_answer = path_dataset + '대용량_정상,악성파일Ⅲ_정답지모음' + os.sep

# 본 python 파일이 실행되면 2018 train 파일은 xlsx => csv 파일로 재생성 및 경로 변경
path_answer_2018_train = path_answer + '01. 2018_TrainSet_정답.xlsx'
path_answer_2018_qual1 = path_answer + '02. 2018_예선_1차_정답.csv'
path_answer_2018_qual2 = path_answer + '03. 2018_예선_2차_정답.csv'

# 본 python 파일이 실행되면 2019 train 파일은 top rows에 'file', 'mal/bin(1/0)' 추가되어 재생성 및 경로 변경
path_answer_2019_train = path_dataset + 'KISA-challenge2019-Malware_trainset' + os.sep + 'KISA-challenge2019-Malware_trainset' + os.sep + 'trainSet.csv'

####################################################################################################
# PE 파일 경로 설정
path_pe = path_dataset + 'PE' + os.sep

path_pe_pe16     = path_pe + 'PE16' + os.sep
path_pe_pe16_ben = path_pe_pe16 + 'ben' + os.sep
path_pe_pe16_mal = path_pe_pe16 + 'mal' + os.sep

path_pe_pe32     = path_pe + 'PE32' + os.sep
path_pe_pe32_ben = path_pe_pe32 + 'ben' + os.sep
path_pe_pe32_mal = path_pe_pe32 + 'mal' + os.sep

path_pe_pe64     = path_pe + 'PE64' + os.sep
path_pe_pe64_ben = path_pe_pe64 + 'ben' + os.sep
path_pe_pe64_mal = path_pe_pe64 + 'mal' + os.sep

####################################################################################################
# NonPE 파일 경로 설정
path_nonpe = path_dataset + 'NonPE' + os.sep

path_nonpe_hwp     = path_nonpe + 'HWP' + os.sep
path_nonpe_hwp_ben = path_nonpe_hwp + 'ben' + os.sep
path_nonpe_hwp_mal = path_nonpe_hwp + 'mal' + os.sep

path_nonpe_html     = path_nonpe + 'HTML' + os.sep
path_nonpe_html_ben = path_nonpe_html + 'ben' + os.sep
path_nonpe_html_mal = path_nonpe_html + 'mal' + os.sep

path_nonpe_docx     = path_nonpe + 'DOCX' + os.sep
path_nonpe_docx_ben = path_nonpe_docx + 'ben' + os.sep
path_nonpe_docx_mal = path_nonpe_docx + 'mal' + os.sep

path_nonpe_rest     = path_nonpe + 'REST' + os.sep
path_nonpe_rest_ben = path_nonpe_rest + 'ben' + os.sep
path_nonpe_rest_mal = path_nonpe_rest + 'mal' + os.sep

####################################################################################################
# 데이터셋 존재 확인
def Dataset_Check():
    if not(os.path.isdir(path_dataset_2018_train)) or not(os.path.isdir(path_dataset_2018_qual1)) or not(os.path.isdir(path_dataset_2018_qual2)) or not(os.path.isdir(path_dataset_2019_train)) or not(os.path.isfile(path_answer_2018_train)) or not(os.path.isfile(path_answer_2018_qual1)) or not(os.path.isfile(path_answer_2018_qual2)) or not(os.path.isfile(path_answer_2019_train)):
        print('폴더 또는 파일 일부가 없습니다. 폴더와 파일이 모두 있는지 확인하세요.\n')
        
        print('[Dataset 경로]')
        print(path_dataset_2018_train)
        print(path_dataset_2018_qual1)
        print(path_dataset_2018_qual2)
        print(path_dataset_2019_train)
        
        print('\n[정답지 경로]')
        print(path_answer_2018_train)
        print(path_answer_2018_qual1)
        print(path_answer_2018_qual2)
        print(path_answer_2019_train)
        
        sys.exit(1)

####################################################################################################
# 분류된 파일이 위치할 폴더 생성
def Make_Folder():
    try:
        os.makedirs(os.path.join(path_pe))
        
        os.makedirs(os.path.join(path_pe_pe16))
        os.makedirs(os.path.join(path_pe_pe16_ben))
        os.makedirs(os.path.join(path_pe_pe16_mal))
        
        os.makedirs(os.path.join(path_pe_pe32))
        os.makedirs(os.path.join(path_pe_pe32_ben))
        os.makedirs(os.path.join(path_pe_pe32_mal))
        
        os.makedirs(os.path.join(path_pe_pe64))
        os.makedirs(os.path.join(path_pe_pe64_ben))
        os.makedirs(os.path.join(path_pe_pe64_mal))
        
        os.makedirs(os.path.join(path_nonpe))
        
        os.makedirs(os.path.join(path_nonpe_hwp))
        os.makedirs(os.path.join(path_nonpe_hwp_ben))
        os.makedirs(os.path.join(path_nonpe_hwp_mal))
        
        os.makedirs(os.path.join(path_nonpe_html))
        os.makedirs(os.path.join(path_nonpe_html_ben))
        os.makedirs(os.path.join(path_nonpe_html_mal))
        
        os.makedirs(os.path.join(path_nonpe_docx))
        os.makedirs(os.path.join(path_nonpe_docx_ben))
        os.makedirs(os.path.join(path_nonpe_docx_mal))
        
        os.makedirs(os.path.join(path_nonpe_rest))
        os.makedirs(os.path.join(path_nonpe_rest_ben))
        os.makedirs(os.path.join(path_nonpe_rest_mal))
        
    except FileExistsError as e:
        print('폴더가 이미 존재합니다. 아래 폴더를 모두 지워주세요.')
        
        print(path_pe)
        print(path_nonpe + '\n')
        
        Exception_Function(e)
        
    except Exception as e: Exception_Function(e)

####################################################################################################
# 2018 Train 정답지 파일 변환
def Xlsx_To_Csv():
    try:
        global path_answer_2018_train

        new_path_answer_2018_train = path_answer + '01. 2018_TrainSet_정답.csv'
        xlsx_wr = open(new_path_answer_2018_train, 'a', encoding = 'latin1', newline = '')
        csv_xlsx_wr = csv.writer(xlsx_wr)

        header = ['file', 'mal/ben(1/0)']
        csv_xlsx_wr.writerows([header])

        load_wb = load_workbook(path_answer_2018_train, data_only=True)
        load_ws = load_wb['TrainSet']

        for index in range(1, 10001):
            rows = [load_ws['A' + repr(index)].value, load_ws['B' + repr(index)].value]
            csv_xlsx_wr.writerows([rows])

        xlsx_wr.close()

        path_answer_2018_train = new_path_answer_2018_train
        
    except Exception as e: Exception_Function(e)

####################################################################################################
# 2019 Train 정답지 파일 변환
def Csv_To_Csv():
    try:
        global path_answer_2019_train

        new_path_answer_2019_train = path_answer + '04. 2019_TrainSet_정답.csv'
        csv_wr = open(new_path_answer_2019_train, 'a', encoding = 'latin1', newline = '')
        csv_csv_wr = csv.writer(csv_wr)

        header = ['file', 'mal/ben(1/0)']
        csv_csv_wr.writerows([header])

        csv_rd = open(path_answer_2019_train, 'r', encoding = 'latin1')
        rows = csv_rd.readlines()
        csv_csv_wr.writerow([rows[0][3:39], rows[0][40:41]])

        for index in range(1, 10000):
            csv_csv_wr.writerow([rows[index][:36], rows[index][37:38]])

        csv_rd.close()
        csv_wr.close()

        path_answer_2019_train = new_path_answer_2019_train
        

    except Exception as e: Exception_Function(e)

####################################################################################################
# 파일 분류
def File_Classification(count, path, answer):
    csv_data = pd.read_csv(answer)
    for index in range(0, csv_data.shape[0]):
        try:
            temp = open(path + csv_data['file'][index], 'rb')
            signature = list(temp.read(32))
            temp.close()
            
            if signature[:2] == signatures['PE']: PE_Classification(path, csv_data['file'][index], csv_data['mal/ben(1/0)'][index])
            else: NonPE_Classification(path, csv_data['file'][index], csv_data['mal/ben(1/0)'][index], signature)
            
            print('[%02d][%05d/%d] Extraction Success...' %(count, index + 1, 10000))
            
        except Exception as e:
            print(csv_data['file'][index])
            Exception_Function(e)

####################################################################################################
# 16bit, 32bit, 64bit 파일 분류
def PE_Classification(path, filename, answer):
    try:
        pe = pefile.PE(path + filename)
        Machine = pe.FILE_HEADER.Machine
        pe.close()
        
        if Machine == 0x14C:
            if answer == 0: shutil.move(path + filename, path_pe_pe32_ben + filename)
            else: shutil.move(path + filename, path_pe_pe32_mal + filename)
        
        elif Machine == 0x8664:
            if answer == 0: shutil.move(path + filename, path_pe_pe64_ben + filename)
            else: shutil.move(path + filename, path_pe_pe64_mal + filename)
    
    except pefile.PEFormatError:
        if answer == 0: shutil.move(path + filename, path_pe_pe16_ben + filename)
        else: shutil.move(path + filename, path_pe_pe16_mal + filename)
    
    except Exception as e:
        print(path + filename)
        Exception_Function(e)

####################################################################################################
# hwp, html, docx, rest 파일 분류
def NonPE_Classification(path, filename, answer, signature):
    try:
        if signature[:len(signatures['HWP'])] == signatures['HWP']:
            if answer == 0: shutil.move(path + filename, path_nonpe_hwp_ben + filename)
            else: shutil.move(path + filename, path_nonpe_hwp_mal + filename)

        elif signature[:len(signatures['HTML'])] == signatures['HTML']:
            if answer == 0: shutil.move(path + filename, path_nonpe_html_ben + filename)
            else: shutil.move(path + filename, path_nonpe_html_mal + filename)

        elif signature[:len(signatures['DOCX'])] == signatures['DOCX']:
            if answer == 0: shutil.move(path + filename, path_nonpe_docx_ben + filename)
            else: shutil.move(path + filename, path_nonpe_docx_mal + filename)

        else:
            if answer == 0: shutil.move(path + filename, path_nonpe_rest_ben + filename)
            else: shutil.move(path + filename, path_nonpe_rest_mal + filename)
    
    except Exception as e:
        print(path + filename)
        Exception_Function(e)

####################################################################################################
# 임시
def Signature_Classification(path_src, filename):
    try:
        with open(path_src+filename, 'rb') as data:
            file_header = list(data.read(32))

        # PE, HTML, HWP 파일을 각각의 폴더로 이동
        for key in signatures.keys():
            test_hex = []
            for _byte in signatures[key].strip().split(' '):
                test_hex.append(ord(bytes.fromhex(_byte)))

            if test_hex == file_header[:len(test_hex)]:
                shutil.move(path_src+filename, path_src+key+os.sep+filename)
                return
            else: continue
                
        # PE, HTML, HWP 파일이 아니면 ETC 폴더로 이동
        shutil.move(path_src+filename, path_src+'ETC'+os.sep+filename)
        data.close()
        
    except Exception as e:
        print(e)
        print(filename)
        sys.exit(1)

####################################################################################################
# 예외 처리 함수
def Exception_Function(e):
    print(e)
    sys.exit(1)

####################################################################################################
# main
if __name__ == "__main__":
    Dataset_Check() # 데이터셋 존재 확인
    print('== 데이터셋 폴더 검사 완료 ==')
    
    Make_Folder() # 분류된 파일이 위치할 폴더 생성
    print('== 분류 폴더 생성 완료 ==')
    
    Xlsx_To_Csv() # 2018 Train 정답지 파일 변환
    print('== 2018 train 확장자 xlsx => csv 변환 완료 ==')
    
    Csv_To_Csv() # 2019 Train 정답지 파일 변환
    print('== 2019 train csv header 추가 및 재생성 완료 ==')
    
    # 2018 train, 2018 예선 1차, 2018 예선 2차, 2019 train 파일 분류
    File_Classification(1, path_dataset_2018_train, path_answer_2018_train)
    print('2018 train 분류 완료')
    
    File_Classification(2, path_dataset_2018_qual1, path_answer_2018_qual1)
    print('2018 qual1 분류 완료')
    
    File_Classification(3, path_dataset_2018_qual2, path_answer_2018_qual2)
    print('2018 qual2 분류 완료')
    
    File_Classification(4, path_dataset_2019_train, path_answer_2019_train)
    print('2019 train 분류 완료')
    
    print('모두 완료')


# In[ ]:




