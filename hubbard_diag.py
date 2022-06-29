import numpy as np
import sys

Nsites =2
################

Nflavor = 2*Nsites

#for flavor in range(Nflavor):
 #  print( (state|(2**flavor)) == state )


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
  return (coefficient*state+(2**flavor))

def annihilate(state,flavor):
  assert(flavor < Nflavor)

  if not occupied(state,flavor):
    return None
  coefficient=(1)**(count_left(state,flavor+1))
  return (coefficient*state-(2**flavor))


############
#print(create(178,2))
#print(annihilate(178,5))

def count(state):
  sum=0
  x = int((Nflavor)/2)
  for i in range(0,Nflavor):
    if occupied(state,i) and occupied(state,i+x):
      sum +=1
  return sum
#print(count(11))





def hopping(state):
   List = []
   x = int(Nflavor/2)
   for i in range(0,Nflavor-1):
       c1 = annihilate(state,i+1)
       coefficient1=(-1)**(count_left(state,i+1))#8
       if i == x-1:
         continue
       if c1 == None:
           List.append(0) 
       else:
           c2 = create(c1, i)
           if c2 == None:
               continue
           else:
               coefficient2=(-1)**(count_left(state,i+1))
               List.append(c2)#(coefficient1*coefficient2*c2)
               List = [i for i in List if i != 0]
           

   for i in range(1,Nflavor):
       c3 = annihilate(state,i-1)
       coefficient3=(-1)**(count_left(state,i+1))
       if i == x:
         continue
       if c3 == None:
           List.append(0)
       else:
           c4 = create(c3, i)
           if c4 == None:
               continue
           else:
               coefficient4=(-1)**(count_left(state,i+1))
               List.append(c4)
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
                    list[j][hopping(j)[k]]=1
    return list
 



def diagonalisator(list):
    list2=[]
    list3 = np.zeros((4**Nsites,4**Nsites))
    for i in range(0,4**Nsites):
        if i not in list2:
            list2.append(i)
        for j in range(0,4**Nsites):
            if list[i][j] !=0 and j not in list2:
                list2.append(j)
    for i in range(len(list2)):
         list3[list2.index(list2[i])][list2.index(list2[i])] = count(list2[i])
         hopping(list2[i])
         for j in range(len(hopping(list2[i]))):
             if hopping(list2[i])[j] == 0:
                    continue
             else: list3[i][list2.index(hopping(list2[i])[j])] = 1
    return list3


        

np.set_printoptions(linewidth=300)

np.set_printoptions(threshold=sys.maxsize)

def list_contains(List1, List2):
    check = False

    # Iterate in the 1st list
    for m in List1:

        # Iterate in the 2nd list
        for n in List2:

            # if there is a match
            if m == n:
                check = True
                return check

    return check    

def bloc_printer():
    list1 = []
    list2=[]
    list3=[]
    list4=[[0]]
    i = 1
    while i < 4**Nsites:
        list1 = []
        list2 = list(hopping(i))
        list2 = [i for i in list2 if i != 0]
        list3 = []

        while(True):
            if all([ v == 0 for v in list2 ]):
                list4 += list([[i]])
                break

            for j in range(len(list2)):
                if list2[j] != 0:
                    list1.append(list2[j])
            list1.sort()
            list3 = list(hopping(list2[0]))
            list3 = [i for i in list3 if i != 0]

            if list_contains(list1, list2) and list_contains(list1, list3):
                list4 += [list(list1)]
                break
            list3*=0
            list2 = list(hopping(list1[0]))
            list2 = [i for i in list2 if i != 0]

        i+=1
        x = set(tuple(row) for row in list4)
        y = [list(item) for item in x]
    return y,"Nombre de blocs:", len(y)


print(blocprinter())











































































