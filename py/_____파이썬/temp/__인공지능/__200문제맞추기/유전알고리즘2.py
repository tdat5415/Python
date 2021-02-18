import random as rd
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread

#random.sample(pop, k) : pop에서 랜덤으로 k개를 뽑음
#sorted([], reverse=True)
#sorted([][], key=lambda x: x[1], reverse=True)
#random.random() : 0 ~ 1

# 1세대 생성
# 성능측정 - 우수한아이들 선발 - 교배 - 돌연변이





#                       100문제 정답맞추기

NUM_PRO = 200
NUM_KID = 100
NUM_SEL = 5     #n지선다형
MAX_GEN = 200   #최대 세대

BEST_RAT = 5 #아이들중 베스트비율 : 1/n
NUM_BEST = NUM_KID//BEST_RAT

LUC_RAT = 50
NUM_LUC = 0#NUM_KID//LUC_RAT #싫으면 0으로

PAR_RAT = 1
NUM_PAR = NUM_BEST//PAR_RAT #아이의 부모개수 # <= NUM_BEST

MUT_RAT = 100    #변이비율 : 1/n
NUM_MUT = NUM_PRO//MUT_RAT

if NUM_PAR > NUM_BEST or NUM_PAR == 1 or NUM_MUT == 0:
    raise Exception('error')

class child():
    def __init__(self):
        self.score = 0
        self.answers = []

# 답안 생성
correct_answers = []
for i in range(NUM_PRO):
    num = rd.randint(1,NUM_SEL)
    correct_answers.append(num)


# 1세대 생성
kids = []
for i in range(NUM_KID):#100명의 아이들
    kid = child()
    for j in range(NUM_PRO):
        num = rd.randint(1,NUM_SEL)
        kid.answers.append(num)
    kids.append(kid)


# 성능측정함수 (점수채점)
def scoring_kid(kid):
    tot = 0
    for i in range(NUM_PRO):
        if kid.answers[i] == correct_answers[i]:
            tot += 1
    return tot


# 우수한아이들선발 함수
def pick_kids(kids):
    sorted_kids = sorted(kids, key=lambda x:x.score, reverse=True)
    best_kids = sorted_kids[:NUM_BEST]
    lucky_kids = rd.sample(sorted_kids[NUM_BEST:], NUM_LUC)

    return best_kids, lucky_kids


# 교배 함수
def create_kid(best_kids, new_kids):        
    parents = rd.sample(best_kids, NUM_PAR)
    new_kid = make_kid(parents)

    new_kids.append(mutation(new_kid))


# 아이생성 함수
def make_kid(parents):
    kid = child()
    for i in range(NUM_PRO):
        R = rd.randint(0,NUM_PAR-1)
        ans = parents[R].answers[i]
        kid.answers.append(ans)
    return kid


# 변이 함수
def mutation(kid):
    RR = rd.sample(range(NUM_PRO), NUM_MUT)#바꿀 몇문제 뽑
    for i in RR:
        R2 = rd.randint(1,NUM_SEL)#답
        kid.answers[i] = R2
       
    return kid


# print
def show(kids, gen):
    score = []
    flag = 0
    max_score = 0
    for kid in kids:
        if kid.score == NUM_PRO:
            #print('ANSWERS : ', kid.answers)
            #print('CORRECT_ANSWERS : ', correct_answers)
            flag = 1
        if max_score < kid.score:
            max_score = kid.score
        score.append(kid.score)
    print('GEN : %d\tBEST : %d' %(gen+1, max_score))

    return flag, score


def main():
    global kids
    global correct_answers
    scores = []
    
    for i in range(MAX_GEN):
        for kid in kids: # 성능측정
            kid.score = scoring_kid(kid)

        flag, score = show(kids, i) # 출력
        scores.append(score)
        if flag == 1:
            break

        best_kids, lucky_kids = pick_kids(kids) # 우수,운빨 선발
        alive_kids = best_kids + lucky_kids
            
        new_kids = []
        for i in range(NUM_KID - NUM_BEST - NUM_LUC):
            #new_kid = create_kid(best_kids, new_kids) # 아이늘리기
            new_kid = create_kid(alive_kids, new_kids) # 아이늘리기

        kids = best_kids + new_kids + lucky_kids
    
    scores = np.array(scores)
    scores = scores.T
    plt.axis([1,MAX_GEN, 0, NUM_PRO])
    plt.plot(range(1,len(scores[0])+1), scores[-1], 'go')
    plt.plot(range(1,len(scores[0])+1), scores[-2], 'yo')
    plt.plot(range(1,len(scores[0])+1), scores[1], 'bo')
    plt.plot(range(1,len(scores[0])+1), scores[0], 'ro')
    plt.show()
    

if __name__ == '__main__':
    main()









