import numpy 
import sys




symmetry_generators = [[0,1,2,3],[1,0,3,2]]
#A = 0b11110101
#x = 10
#C = format(x,"04b")

#binA = bin(A)[2:][::1]

#B = int(''.join(C[i] for i in symmetry_generator1), 2)

#print(C)

#print(B)
#print(format(B,"04b"))





character_table = [[1,1],
                   [1,-1]]










Nsites =2
Nflavor = 2*Nsites




def occupied(state,flavor):
  return (state|(2**flavor)) == state

def count_left(state,flavor):
  count=0
  for ii in range(flavor,Nflavor):
    if occupied(state,ii):
      count +=1 
  return count

def create(state,flavor):
  assert(flavor < Nflavor)

  if occupied(state,flavor):
    return None
  coefficient=(1)**(count_left(state,flavor+1))
  return coefficient*state+(2**flavor)

def annihilate(state,flavor):
  assert(flavor < Nflavor)

  if not occupied(state,flavor):
    return None
  coefficient=(1)**(count_left(state,flavor+1))
  return coefficient*state-(2**flavor)


def count(state):
  sum=0
  x = int((Nflavor)/2)
  for i in range(0,Nflavor):
    if occupied(state,i) and occupied(state,i+x):
      sum +=1 
  return sum 



def hopping(state):
   List = []
   matrix = [[0,1],
            [1,0]]


   for i in range(len(matrix)):
       for j in range(len(matrix)):
           if matrix[i][j] == 0:
               continue
           elif matrix[i][j] != 0:
               c1 = annihilate(state,i)
               coefficient1=(-1)**(count_left(state,i+1))
               if c1 == None:
                   continue
               else:
                   c2 = create(c1, j)
                   if c2 == None:
                       continue
                   else:
                       coefficient2=(-1)**(count_left(state,i+1))
                       List.append(c2)#(coefficient1*coefficient2*c2)
                       List = [i for i in List if i != 0]
   for i in range(len(matrix)):
       for j in range(len(matrix)):
           if matrix[i][j] == 0:
               continue
           elif matrix[i][j] != 0:
               c3 = annihilate(state,Nflavor-1-i)
               coefficient1=(-1)**(count_left(state,i+1))#8
               if c3 == None:
                  continue
               else:
                   c4 = create(c3, Nflavor-1-j)
                   if c4 == None:
                       continue
                   else:
                       coefficient4=(-1)**(count_left(state,i+1))
                       List.append(c4)#(coefficient1*coefficient2*c2)
                       List = [i for i in List if i != 0]

   return List


def hamiltonian():
    list = np.zeros((4**Nsites,4**Nsites))
    for i in range(0,4**Nsites):
        for j in range(0,4**Nsites):
            list[j][j] = count(j)
            for k in range(len(hopping(j))):
                if hopping(j)[k] == 0:
                    continue
                else:
                    list[j][hopping(j)[k]] = 1
    return list





def block_printer4():
    bank = list(range(1, 64))
    result = [[0],]
    test2 = []

    while len(bank) != 0 :

        test = [bank[0]]
        test2 = test.copy()
        bank.remove(bank[0])
        i = 0
        while True:    
          if set(hopping(test2[i])).issubset(test2):
            i +=1
            
          elif not set(hopping(test2[i])).issubset(test2):
             for j in range(len(hopping(test2[i]))):
               test2.append(hopping(test2[i])[j])
             i = 0
             
          if (all(set(hopping(test2[t])).issubset(test2) for t in range(len(test2)))):
            break
            
          
        test2 = list(set(test2))
        test2.sort()
        test2 = list(set(test2))
        test2.sort()
        for k in test2:
            if k in bank:
                bank.remove(k)
        result.append(test2)

    return result



def rotate(state,symmetry_generator):
    A = format(state,"04b")
    B = int(''.join(A[i] for i in symmetry_generator), 2)
    return B

print(rotate(6,[1,0,3,2]))

def symmetric_state(state):
    coefficient = 1/len(symmetry_generators)
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(symmetry_generators)):
        for j in range(len(character_table[i])):
            list1.append((character_table[i][j])*rotate(state,symmetry_generators[j]))
            if j == len(character_table[i])-1:
                test = list1.copy()
                list3.append(test)
                list1 *= 0
           
    for i in range(1):
        for j in range(1,len(character_table[i])):
            list2.append((character_table[i][j])*rotate(state,symmetry_generators[j]))

            
    return coefficient,list2,list3


def inner_product(state1,state2,representation):
    sum = 0
    list = []
    if state1 != state2:
        for i in range(len(symmetric_state(state1)[2][representation])):
            for j in range(len( symmetric_state(state2)[2][representation])):
                if hamiltonian()[symmetric_state(state1)[2][representation][i]][symmetric_state(state2)[2][representation][j]] != 0:
                    sum += 1
                    list.append("-t")
    return sum


print(inner_product(5,6,0))




def symmetric_block(list):
    a = np.zeros((len(list),len(list)))
    list2 = []
    for i in range(len(list)):
        for j in range(len(symmetric_state(list[i])[1])):
            if list[i] and symmetric_state(list[i])[1][j] not in list2:
                list2.append(list[i])
    for i in range(len(list2)):
        for j in range(len(list2)):
            for k in range(len(list2)):
                print(list2[i])
                print(list2[k])
                a[i][k] = inner_product(list2[i],list2[k],j)
                a[i][i] = count(j)
    return a



p = [5,6,9,10]

print(symmetric_block(p))

def symmetric_matrix(block):
    list2 = []
    for i in range(len(block)):
        list2.append(symmetric_block(block[i]))
    return list2



print(symmetric_matrix(block_printer4()))
