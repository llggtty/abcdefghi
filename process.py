# abcd/efgh =i， where a-i are numbers from 1-9
import itertools 
import numpy as np

# first find out the range of i
np.floor(9876/1234) # 8
# idea is to iterate the number n1 and n2, where n1>n2 
# depending on i, we can narrow down the first digit
# a1 a2 a3 a4 and b1 b2 b3 b4


def remain(total , used):
    return np.array(list(set(total) - set(used)))

total = np.array(range(1,10))

for i in range(2,8):    
    for a1 in total[total > i]:
        for b1 in list(set([int(np.floor(a1/i)),int(np.ceil(a1/i))]) - set([i])):
            print("i:", i, ", a1:", a1, ", b1:", b1)
            numbers_ab = remain(total, [a1, i , b1])
            
            combos_a = list(itertools.permutations(numbers_ab, 3))            
            for combo in combos_a:
                n1 = 1000*a1 + 100*combo[0] + 10*combo[1] + combo[2]
                numbers_b = remain(numbers_ab, list(combo))
                combos_b = list(itertools.permutations(numbers_b,3))
                for combo in combos_b:
                    n2 = 1000*b1 + 100*combo[0] + 10*combo[1] + combo[2]
                    if n1 == int(n2*i):
                        print("!!!Solved!!!!", "i: ",i, "n1: ",n1, "n2: ", n2)
                        