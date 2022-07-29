#import numpy as np
#c = complex([0[, (2*np.pi/3)]])
#w = cmath.exp(c)
#w_conj = cmath.exp(-c)


def group_create(Nsites,group):
    if Nsites == 2 and group == "c2":
        sym_gen = [[1,0]]
        char_table = [[1,1],
                     [1,-1]]
    elif Nsites == 4 and group == "c2":
          sym_gen = [[1,0,3,2]]
          char_table = [[1,1],
                          [1,-1]]
    
    elif Nsites == 3 and group == "c2":
          sym_gen = [[1,0,2]]
          char_table = [[1,1],
                        [1,-1]]
    elif Nsites == 3 and group == "d3":
          sym_gen = [[1,0,2],[2,0,1]]
          char_table = [[1,1,1,1,1,1],
                       [1,-1,1,-1,1,-1],
                       [2,0,-1,0,-1,0]]
   # elif Nsites == 3 and group == "c3":
    #      sym_gen = [[2,0,1]]
     #     char_table = [[1,1,1],
      #                 [1,w,w_conj],
       #                [1,w_conj,w]]

    elif Nsites == 4 and group == "c2":
        sym_gen = [[1,0,3,2]]
        char_table = [[1,1],
                        [1,-1]]
    elif Nsites == 4 and group == "c2v":
        sym_gen = [[3,2,1,0],[1,0,3,2]]
        char_table = [[1,1,1,1],
                        [1,1,-1,-1],
                        [1,-1,1,-1],
                        [1,-1,-1,1]]
    elif Nsites == 5 and group == "c2":
        sym_gen = [[1,0,3,2,4]]
        char_table = [[1,1],
                     [1,-1]]
    return sym_gen,char_table





