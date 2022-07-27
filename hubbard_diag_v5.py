import numpy as np
import sys 
from sys import argv
import groups


def bit_count(integer1):
    return bin(integer1).count("1")



Nsites = int(sys.argv[1])
Nflavor = 2*Nsites
group = str(sys.argv[2])
T = -1 

U = 5


if Nsites == 2:
    interaction_matrix = [[0,1],
                          [1,0]]
elif  Nsites == 3:
    interaction_matrix = [[0,1,1],
                          [1,0,1],
                          [1,1,0]]
elif Nsites == 4:
    interaction_matrix = [[0,1,1,1],
                          [1,0,1,1],
                          [1,1,0,1],
                          [1,1,1,0]]








#character_table = [[1,1,1],
#                   [1,1,-1],
#                   [1,-1,-1]]







symmetry_generator = groups.group_create(Nsites,group)[0]

character_table = groups.group_create(Nsites,group)[1]


def main():

  np.set_printoptions(linewidth=300)

  np.set_printoptions(threshold=sys.maxsize)
  
  np.set_printoptions(precision=2)
 # print(hamiltonian())
  print("states orbits:")
  print(orbit_printer())

  print("\n")

  print(electron_number(orbit_printer()))
  


  print("       ",total_spin(orbit_printer()))
  print("\n")
  print("\n")

  print("Block matrix:")
  print("\n")  
  
 

  for i in range(len(orbit_printer())):
      print("Block number:",i)
      
      print(block_matrix(orbit_printer()[i]))
      print("\n")
      
      print("Eigenvalue of the block:",i)
      
      
      print(np.linalg.eigh(block_matrix(orbit_printer()[i]))[0])
      print("\n") 
      
  print("\n")
  print("Block matrix with symmetric state basis:")
  print("\n")
  for i in range(len(orbit_printer())):
      print("Block number:",i)
      
     
      print(symmetric_block(orbit_printer()[i]))
      
      print("\n")
      print("Eigenvalue of the symmetric block:",i)
     
      print(np.linalg.eigh(symmetric_block(orbit_printer()[i]))[0])
      print("\n")
def generator(list1):
    list2 = []
    list3 = []
    list4 = [] 
    group_member = []
    j = 0
    count = 0
    a = np.arange(0,2*Nsites)
    list5 = list(a)
    list6 = [list5]
    list7 = []
    list8 = []
    x = 0
    for i in range(len(list1)):
        while j < 2*Nsites:
            for k in range(len(list1[i])):
                list2.append(list1[i][k]+(count*Nsites))
                j+=1
            count +=1
        j *= 0
        count *=0
        list3 = list2.copy()
        list4.append(list3)
        list2 *= 0

    for z in range(len(list4)):
        while True:
            for y in range(len(list6[x])):
                list7.append(list6[x][list4[z][y]])
            list8 = list7.copy()
            if list7 == list5:
                list7 *= 0
                x *= 0
                break
            else:
                list7 *= 0
                x += 1
            list6.append(list8)



    return list6
















#This function take a state and output its symmetric counterpart for a given symmetry.
#Input:(5,[1,0,3,2])
#output:10
def group_action(state,symmetry):
    A = format(state,"0"+str(2*Nsites)+"b")
    B = int(''.join(A[i] for i in symmetry), 2)
    return B

#This function is equivalent to applying the projector operator on a state to give the symmetric state in the chosen representation.
#THe first output is the coefficient (one over the lenght of the group).
#The second output is the list of other states equivalent to the input state under the relevent symmetry group
#The third output is the list of each group action on the state multiplied by their character in the character table for the chosen representation.
#For Nsites = 2, and group C2
#Input:(5,1)
#Output:1/2,[10],[5,-10]
def symmetric_state(state,representation):
    coefficient = 1/(len((generator(symmetry_generator)))**(1/2))
    list1 = []
    list2 = []
    list3 = []
    sum = 0
    for i in range(len(generator(symmetry_generator))):
        for j in range(len(character_table[i])):
            list1.append((character_table[i][j])*group_action(state,generator(symmetry_generator)[j]))
            if j == len(character_table[i])-1:
                test = list1.copy()
                list3.append(test)
                list1 *= 0
           
    for i in range(1):
        for j in range(1,len(character_table[i])):
            list2.append((character_table[i][j])*group_action(state,generator(symmetry_generator)[j]))
    
    for i in range(len(list3)):
        if list3[0][i] == state:
            sum += 1
    coefficient2 = coefficient**sum
            
    return coefficient2,list2,list3[representation]









#This functioon compute the inner product between two symmetric state in a given representation
#Of course, the product of two state in different representations is zero
#The first two inputs are the states, third one is the representation of the first state, and the last one the representation of the second state
#Input:(5,6,0,0)
#Output:2T
def product(state1,state2,rep1,rep2):
    sum = 0
    for i in range(len(symmetric_state(state1,rep1)[2])):
        for j in range(len( symmetric_state(state2,rep2)[2])):
            if abs(symmetric_state(state2,rep2)[2][j]) in hopping(abs(symmetric_state(state1,rep1)[2][i])):
                if (symmetric_state(state1,rep1)[2][i] < 0 and not symmetric_state(state2,rep2)[2][j] < 0)  or (symmetric_state(state2,rep2)[2][j] < 0 and not symmetric_state(state1,rep1)[2][i] < 0)  :
                    sum -= 1*T
                else:
                    sum += 1*T

            elif abs(symmetric_state(state2,rep2)[2][j])  == abs(symmetric_state(state1,rep1)[2][i]):
                if (symmetric_state(state1,rep1)[2][i] < 0 and not symmetric_state(state2,rep2)[2][j] < 0)  or (symmetric_state(state2,rep2)[2][j] < 0 and not symmetric_state(state1,rep1)[2][i] < 0)  :  
                    sum -= count(abs(symmetric_state(state2,rep2)[2][j]))
                else:
                    sum += count(abs(symmetric_state(state2,rep2)[2][j]))
                
            
            
                
                
    if rep1 != rep2:
        sum = 0 
    return sum*symmetric_state(state1,rep1)[0]*symmetric_state(state2,rep1)[0]

def occupied(state,flavor):
  return (state|(2**flavor)) == state

def count_left(state,flavor):
  count=0
  for ii in range(flavor,Nflavor):
    if occupied(state,ii):
      count +=1 
  return count


#This function create an electron on a chosen electronic site
#Input:(5,1)
#Output:7
def create(state,flavor):
  assert(flavor < Nflavor)

  if occupied(state,flavor):
    return None
  coefficient=(1)**(count_left(state,flavor+1))
  return coefficient*state+(2**flavor)


#This function create an electron on a chosen electronic site
#Input:(5,2)
#Output:1
def annihilate(state,flavor):
  assert(flavor < Nflavor)

  if not occupied(state,flavor):
    return None
  coefficient=(1)**(count_left(state,flavor+1))
  return coefficient*state-(2**flavor)

#Compute the first summation term in the Hubbard Hamiltonien.
#Input(15)
#Output(2U)
def count(state):
  sum=0
  x = int((Nflavor)/2)
  for i in range(0,Nflavor):
    if occupied(state,i) and occupied(state,i+x):
      sum +=1*U 
  return sum

#Compute the second summation term in the Hubbard Hamiltonien.



def hopping(state):
   List = []

   for i in range(len(interaction_matrix)):
       for j in range(len(interaction_matrix)):
           if interaction_matrix[i][j] == 0:
               continue
           elif interaction_matrix[i][j] != 0:
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
   for i in range(len(interaction_matrix)):
       for j in range(len(interaction_matrix)):
           if interaction_matrix[i][j] == 0:
               continue
           elif interaction_matrix[i][j] != 0:
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


#Compute the Hamiltonian matrix without change in thw states order
def hamiltonian():
    list = np.zeros((4**Nsites,4**Nsites))
    for i in range(0,4**Nsites):
        for j in range(0,4**Nsites):
            list[j][j] = count(j)
            for k in range(len(hopping(j))):
                if hopping(j)[k] == 0:
                    continue
                else:
                    list[j][hopping(j)[k]] = 1*T
    return list








#List that contain lists of all states orbits.
#The orbit of a given state is all the states obtainable by successively applying the Hamiltonien on resulting states.
#Ex: for group C2 with Nsites = 2, the orbit of 5 is [5,6,9,10].
def orbit_printer():
    bank = list(range(1, 4**Nsites))
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


def electron_number(list):
    number = []
    for m in list:
        number.append(bit_count(m[0]))
    return "Number of electrons in each block:", number,"Number of blocks:",len(number)






def total_spin(list):
    spin = []
    bucket = []
    for m in list:
        mylist = [i for i in range(m[0].bit_length()) if m[0] & (1<<i)]
        count = 0
        x = 0
        for i in mylist:
            if i < Nsites:
                count -= 1
            else:
                count += 1
        x = count
        spin.append(x)

    return "Total spin for each block:",spin



#Print hamiltonian matrix in block form.
#Each block correpond to the hamiltonian matrix part of a given orbit.
def block_matrix(list):
    matrix = np.zeros((len(list),len(list)))
    for i in range(len(list)):
        for j in range(len(hopping(list[i]))):
            #matrix[j][j] = count(list[j])
            if hopping(list[i])[j] == 0:
                continue
            else:
                matrix[list.index(hopping(list[i])[j])][i] = 1*T
    for i in range(len(list)):
        for j in range(len(list)):
            matrix[j][j] = count(list[j])
                
    return matrix



#Output each block matrix but in the symmetric basis.
#These matrix are have diagonal block correponding to the group irreducable reresentations
def symmetric_block(list):
    sum1 = 0
    sum2 = 0
    list2 = []
    for i in range(len(list)):
        if list[i] not in list2:
            if all(j not in list2 for j in symmetric_state(list[i],0)[1]) :
                list2.append(list[i])
    if len(list)==1:
        list3 = list2
    else:
        list3 = len(character_table)*list2
    a = np.zeros((len(list3),len(list3)))
    for i in range(len(list3)):
        for j in range(len(list3)):
            sum1 = i//len(list2)
            sum2 = j//len(list2)
           
            a[i][j] = product(list3[i],list3[j],sum1,sum2)
    idx = np.argwhere(np.all(a[..., :] == 0, axis=0))
    a2 = np.delete(a, idx, axis=1)
    a3 =a2[~np.all(a2 == 0, axis=1)]

    return a3


#Print the block of a symmetric matrix correponding to an irreducable representation
def irreducable_representation(list,rep):
    sum1 = 0
    sum2 = 0
    list2 = []
    for i in range(len(list)):
        if list[i] not in list2:
            if all(j not in list2 for j in symmetric_state(list[i],0)[1]) :
                list2.append(list[i])

    a = np.zeros((len(list2),len(list2)))
    for i in range(len(list2)):
        for j in range(len(list2)):
            
           
            a[i][j] = product(list2[i],list2[j],rep,rep)
    idx = np.argwhere(np.all(a[..., :] == 0, axis=0))
    a2 = np.delete(a, idx, axis=1)
    a3 =a2[~np.all(a2 == 0, axis=1)]

    return a3



















main()

