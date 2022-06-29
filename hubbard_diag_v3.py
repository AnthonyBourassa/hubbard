import numpy as np
import sys 
from sys import argv  

Nsites = int(sys.argv[1])
Nflavor = 2*Nsites


def main():

  np.set_printoptions(linewidth=300)

  np.set_printoptions(threshold=sys.maxsize)

  #print(hamiltonian())

  print(block_printer())



  print(electron_number(block_printer()))
  print("      ",total_spin(block_printer()))




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

def count(state):
  sum=0
  x = int((Nflavor)/2)
  for i in range(0,Nflavor):
    if occupied(state,i) and occupied(state,i+x):
      sum +=1
  return sum



def hopping(state):
   List = []

   if Nsites == 2:
       matrix = [[0,1],
               [1,0]]
   elif  Nsites == 3:
       matrix = [[0,1,1],
                [1,0,1],
                [1,1,0]]
   elif Nsites == 4:
       matrix = [[0,1,0,1],
                [1,0,1,0],
                [0,1,0,1],
                [1,0,1,0]]
   else:
       print("Invalide")
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
    list = list = np.array([[" 0"]*(4**Nsites)]*(4**Nsites))
    for i in range(0,4**Nsites):
        for j in range(0,4**Nsites):
          if count(j) != 0:
            list[j][j] = (str(count(j))+"U")
          for k in range(len(hopping(j))):
                if hopping(j)[k] == 0:
                    continue
                else:
                    list[j][hopping(j)[k]] = "-t"
    return list








def block_printer():
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
        number.append(m[0].bit_count())
    return "Nombre d'electron par bloc:", number,"Nombre total de blocs:",len(number)






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

    return "Spin total par bloc:",spin


main()
