import copy
import numpy as np

class lecture:
    def __init__(self, name, times):
        # ex) lecture('강의명', [['월',1],['월',2],['화',1]])
        self.name = name
        
        self.times = times
        
        self.t_index = []
        for time in times:
            temp = [0,0]
            if time[0] == '월':
                temp[0] = 0
            elif time[0] == '화':
                temp[0] = 1
            elif time[0] == '수':
                temp[0] = 2
            elif time[0] == '목':
                temp[0] = 3
            elif time[0] == '금':
                temp[0] = 4
            else:
                raise Exception('요일을 제대로 입력')
            temp[1] = time[1] - 1
            self.t_index.append(temp)

        self.schedule = np.array([np.array([0]*5)]*8)
        for d, t in self.t_index:
            self.schedule[t][d] = 1
        

class sum_sche:
    def __init__(self):
        self.lectures = []
        self.num = 0
        self.schedule = np.array([np.array([0]*5)]*8)
        self.names = []

    def insert(self, lec):
        self.schedule += lec.schedule
        if 2 in self.schedule:
            return None
        elif lec.name in self.names:
            return None
        elif 2 in (self.schedule + np.array([np.array(holiday)]*8)):
            return None
        
        self.lectures.append(lec)
        self.num += 1
        self.names.append(lec.name)
        self.names = sorted(self.names)

        return self

    def show(self):
        print(tuple(sorted([lec.name for lec in self.lectures])))
        print(self.schedule)
        print()

l = []
        
l.append(lecture('현',[['월',5],['월',6],['수',1]]))
l.append(lecture('웹',[['화',5],['화',6],['화',7]]))
l.append(lecture('북',[['수',2],['수',3],['수',4]]))
l.append(lecture('데베',[['월',1],['목',6],['목',7]]))
l.append(lecture('데통',[['금',1],['금',2],['금',3]]))
l.append(lecture('데통',[['수',6],['수',7],['수',8]]))
l.append(lecture('운',[['월',2],['월',3],['월',4]]))
#l.append(lecture('운',[['목',2],['목',3],['목',4]]))
l.append(lecture('운',[['금',6],['금',7],['금',8]]))
l.append(lecture('컴',[['화',1],['화',2],['화',3]]))
l.append(lecture('컴',[['수',6],['수',7],['수',8]]))
l.append(lecture('러',[['화',6],['화',7],['화',8]]))
l.append(lecture('중',[['수',4],['수',5],['수',6]]))
l.append(lecture('피',[['금',2],['금',3],['금',4]]))


# 이름이 겹쳐도 된다.

first_necessary = [ l[0], l[1], l[2] ] # 꼭 들을 강의들(전필등등) # 겹치면 땡

second_necessary = l#[l4, l5] # 2순위 들을 강의들(전선,교양등등)

num_lecture = 7 # 들을 강의 갯수

holiday = [0,0,0,0,1] # 공강할 요일이 들어간다. 

schedules = [] # 가능한 시간표들이 생겨난다.

def make_init_sum_sche():
    init = sum_sche()
    for lec in first_necessary:
        init = init.insert(lec)
        if init == None:
            raise Exception('꼭 들을 강의들이 겹침')

    return init


def solve(init_sche):
    global schedules
    global num_lecture
    num_lecture -= init_sche.num
    
    old_sches = [init_sche]
    old_sches_namess = [init_sche.names]
    old_sches_scheds = [list(init_sche.schedule.flatten())]
    new_sches = []
    new_sches_namess = []
    new_sches_scheds = []
    
    for i in range(num_lecture):
        print(i + init_sche.num, len(old_sches))
        for old_sche in old_sches:
            
            for lec in second_necessary:
                old_copy = copy.deepcopy(old_sche) # 스케줄복사
                
                bigger_sche = old_copy.insert(lec)
                if bigger_sche == None:
                    continue
                if bigger_sche.names in new_sches_namess: # 과목들이 겹치면 
                    if list(bigger_sche.schedule.flatten()) in new_sches_scheds:#시간표확인
                        continue
                new_sches.append(bigger_sche)
                new_sches_namess.append(bigger_sche.names)
                new_sches_scheds.append(list(bigger_sche.schedule.flatten()))

        if len(new_sches) == 0:
            schedules = old_sches
            return
        old_sches = new_sches
        old_sches_namess = new_sches_namess
        old_sches_scheds = new_sches_scheds
        new_sches = []
        new_sches_namess = []
        new_sches_scheds = []
            
    schedules = old_sches
    return


def main():
    global schedules
    init_sche = make_init_sum_sche()
    solve(init_sche)
    #print(schedules)



            
    for sche in schedules:
        sche.show()


if __name__ == '__main__':
    main()


    
















    
