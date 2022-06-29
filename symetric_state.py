import numpy as np 
import sys


Nsites = 2
INT_BITS = 2*Nsites

group_c2 = list(np.arange(0,Nsites))


character_table = [[1,1],
                   [1,-1]]


state = int(sys.argv[1])




def Rotate(state, rot):
 
    return (state >> rot)|(state << (INT_BITS - rot)) & ((4**Nsites)-1)

print(Rotate(10,2))



def symetric_state(state):
    coefficient = 1/len(group_c2)
    list = []
    list2 = []
    for i in range(len(group_c2)):
        for j in range(len(character_table[i])):
            list.append((character_table[i][j])*Rotate(state,j))
            
    return coefficient,list



print(symetric_state(state))



