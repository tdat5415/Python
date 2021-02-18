from tensorflow.examples.tutorials.mnist import input_data
import math
import numpy as np
import random as rd
import n_net as nn


mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)
#print(len(mnist.test.images))#10000
#print(len(mnist.test.images[0]))#784 = 28x28
#print(len(mnist.test.labels))#10000
#print(len(mnist.test.labels[0]))#10


NUM_KID = 50    # 모델갯수 50개
NUM_BEST = 10   # 선발갯수 10개  베스트 전체가 부모가 된다.
MUT_PER = 0.05  # 변이확률 5%
MAX_GEN = 100
DESIGN = [784, 10]


# 우수한 아이들 선발 함수
def pick_kids(kids):
    sorted_kids = sorted(kids, key=lambda x:x.avg_cost)
    best_kids = sorted_kids[:NUM_BEST]

    return best_kids

# 교배 함수
def create_kid(best_kids):
    new_kid = nn.model(DESIGN)

    for i in range(len(DESIGN)-1):
        for j in range(DESIGN[i+1]):
            for k in range(DESIGN[i]):
                R = rd.randint(0, NUM_BEST-1)
                new_kid.weights[i][j][k] = best_kids[R].weights[i][j][k]
                #[1][10][784]꼴
            R = rd.randint(0, NUM_BEST-1)
            new_kid.biases[i][j] = best_kids[R].biases[i][j]
            #[1][10]꼴
    return new_kid

# 변이 함수
def mutation(kid):
    mut_kid = kid

    for i in range(len(DESIGN)-1):
        for j in range(DESIGN[i+1]):
            for k in range(DESIGN[i]):
                if MUT_PER > rd.random():
                    mut_kid.weights[i][j][k] += 0.1 * np.random.randn()
                    #[1][10][784]꼴
            if MUT_PER > rd.random():
                mut_kid.biases[i][j] += 0.1 * np.random.randn()
                #[1][10]꼴
    return mut_kid

# 출력
def show(kids, gen):
    score = []
    min_cost = 10000
    for kid in kids:
        if min_cost > kid.avg_cost:
            min_cost = kid.avg_cost
        score.append(kid.avg_cost)
    print('GEN : %d\tBEST : %d' %(gen+1, min_cost))

    return fscore


def main():
    #1세대 생성
    kids = [nn.model(DESIGN) for i in range(NUM_KID)]
    
    for i in range(MAX_GEN):
        gen = i
        batch_xs, batch_ys = mnist.train.next_batch(100)
        for kid in kids:
            kid.batch_cel(batch_xs, batch_ys) # 계산
            
        best_kids = pick_kids(kids) # 우수 선발
        print('GEN : %d\tBEST : %lf' %(gen+1, best_kids[0].avg_cost))
        
        new_kids = []
        for i in range(NUM_KID - NUM_BEST):
            new_kid = create_kid(best_kids) # 생성
            new_kid = mutation(new_kid) # 변이
            new_kids.append(new_kid)

        kids = best_kids + new_kids # 세대 교체




    count = 0
    test_xs, test_ys = mnist.test.next_batch(100)
    for i in range(100):
        kids[0].input(mnist.test.images[i])
        kids[0].compute()
        
        ans = None
        _max = -1000
        for j in range(10):
            if _max < kids[0].layers[-1][j]:
                _max = kids[0].layers[-1][j]
                ans = j
        correct = None
        for j in range(10):
            if mnist.test.labels[i][j] == 1:
                correct = j
                break
        print(correct, ans)
        if correct == ans:
            count += 1
    print('정답갯수(100) : %d' %count)

    



if __name__ == '__main__':
    main()


















    
