import random as rd
import numpy as np
from threading import Thread





class adult():
    NUM_PRO = 200
    NUM_KID = 100
    NUM_SEL = 5     #n지선다형
    MAX_GEN = 200   #최대 세대
    
    def __init__(self):
        self.tot_score = 0 #종합점수
        
        self.BEST_RAT = 10 #아이들중 베스트비율 : 1/n  2= < n <= NUM_KID//10
        self.NUM_BEST = adult.NUM_KID//self.BEST_RAT

        self.LUC_RAT = 50 # 0 < n <= 
        self.NUM_LUC = 0#NUM_KID//LUC_RAT #싫으면 0으로

        self.PAR_RAT = 1 #1/n   1<= n <= (NUM_BEST//2)
        self.NUM_PAR = self.NUM_BEST//self.PAR_RAT #아이의 부모개수 # <= NUM_BEST

        self.MUT_RAT = 100    #변이비율 : 1/n  5 <= n < 무한대
        self.NUM_MUT = adult.NUM_PRO//self.MUT_RAT

        if self.NUM_PAR > self.NUM_BEST or \
           self.NUM_PAR == 1 or \
           self.NUM_MUT == 0:
            raise Exception('error')

        self.correct_answers = []
        self.kids = []
        
    def start(self):
        # 답안 생성
        self.correct_answers = []
        for i in range(adult.NUM_PRO):
            num = rd.randint(1,adult.NUM_SEL)
            self.correct_answers.append(num)

        # 1세대 생성
        self.kids = []
        for i in range(adult.NUM_KID):#100명의 아이들
            kid = child()
            for j in range(adult.NUM_PRO):
                num = rd.randint(1,adult.NUM_SEL)
                kid.answers.append(num)
            self.kids.append(kid)

    # 성능측정함수 (점수채점)
    def scoring_kid(self, kid):
        tot = 0
        for i in range(adult.NUM_PRO):
            if kid.answers[i] == self.correct_answers[i]:
                tot += 1
        return tot


    # 우수한아이들선발 함수
    def pick_kids(self, kids):
        sorted_kids = sorted(kids, key=lambda x:x.score, reverse=True)
        best_kids = sorted_kids[:self.NUM_BEST]
        lucky_kids = rd.sample(sorted_kids[self.NUM_BEST:], self.NUM_LUC)

        return best_kids, lucky_kids


    # 교배 함수
    def create_kid(self, best_kids, new_kids):        
        parents = rd.sample(best_kids, self.NUM_PAR)
        new_kid = self.make_kid(parents)

        new_kids.append(self.mutation(new_kid))


    # 아이생성 함수
    def make_kid(self, parents):
        kid = child()
        for i in range(adult.NUM_PRO):
            R = rd.randint(0,self.NUM_PAR-1)
            ans = parents[R].answers[i]
            kid.answers.append(ans)
        return kid


    # 변이 함수
    def mutation(self, kid):
        RR = rd.sample(range(adult.NUM_PRO), self.NUM_MUT)#바꿀 몇문제 뽑
        for i in RR:
            R2 = rd.randint(1,adult.NUM_SEL)#답
            kid.answers[i] = R2
           
        return kid


    # print
    def show(self, kids, gen):
        score = []
        flag = 0
        max_score = 0
        for kid in kids:
            if kid.score == adult.NUM_PRO:
                #print('ANSWERS : ', kid.answers)
                #print('CORRECT_ANSWERS : ', correct_answers)
                flag = 1
            if max_score < kid.score:
                max_score = kid.score
            score.append(kid.score)
        #print('GEN : %d\tBEST : %d' %(gen+1, max_score))

        return flag, score, max_score


class child():
    def __init__(self):
        self.score = 0
        self.answers = []

##############################################################



# 큰 성능측정
def sub_main(person): 
    gen = 0
    person.start()
    
    for i in range(adult.MAX_GEN):
        gen = i
        #print('%d '%(gen+1), end='')
        for kid in person.kids: # 성능측정
            kid.score = person.scoring_kid(kid)

        flag, score, max_score = person.show(person.kids, gen) # 출력
        if flag == 1:
            break

        best_kids, lucky_kids = person.pick_kids(person.kids) # 우수,운빨 선발
        alive_kids = best_kids + lucky_kids
            
        new_kids = []
        for i in range(adult.NUM_KID - person.NUM_BEST - person.NUM_LUC):
            #new_kid = create_kid(best_kids, new_kids) # 아이늘리기
            new_kid = person.create_kid(alive_kids, new_kids) # 아이늘리기

        person.kids = best_kids + new_kids + lucky_kids

    tot_score = max_score - gen # 이 모델에 대한 점수

    person.tot_score = tot_score
    #return tot_score


#최고사람점수
def show_best(people, gen):
    max_tot_score = -1000
    tot_scores = []
    best_one = None
    for person in people:
        if max_tot_score < person.tot_score:
            max_tot_score = person.tot_score
            best_one = person
        tot_scores.append(person.tot_score)
        
    print('\nGEN : %d\t\tMAX_TOT_SCORE : %d' %(gen, max_tot_score))
    print('BEST_RAT : %d' %best_one.BEST_RAT)
    print('PAR_RAT : %d' %best_one.PAR_RAT)
    print('MUT_RAT : %d' %best_one.MUT_RAT)
            
    return max_tot_score, tot_scores, best_one
                

def main():
    #init
    scores = []

    num_try = 0
    best_one = None
    max_tot_score = -1000
    for i in range(2, adult.NUM_KID//10+1): # 9개
        person = adult()
        person.BEST_RAT = i # 아마 5쯤?
        person.NUM_BEST = adult.NUM_KID//person.BEST_RAT
        for j in range(1, person.NUM_BEST//2+1): # 최대25개 최소 5개
            person.PAR_RAT = j # 아마 1이 최고
            person.NUM_PAR = person.NUM_BEST//person.PAR_RAT

            person.MUT_RAT = 100
            person.NUM_MUT = adult.NUM_PRO//person.MUT_RAT
            
            num_try+=1
            print('Try : %d' %(num_try))
            sub_main(person)
            if max_tot_score < person.tot_score:
                max_tot_score = person.tot_score
                #best_one = person
                print('BEST_RAT : %d\t\tPAR_RAT : %d' %(i,j))
                print('max_tot_score : %d' %(max_tot_score))
                
        


if __name__ == '__main__':
    main()









