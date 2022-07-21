



def group_create(Nsites,group):
    if Nsites == 2 and group == "c2":
        sym_gen = [[1,0]]
        char_table = [[1,1],
                     [1,-1]]
    elif Nsites == 3 and group == "c2":
          sym_gen = [[1,0,2]]
          char_table = [[1,1],
                        [1,-1]]
    elif Nsites == 3 and group == "d3":
          sym_gen = [[1,0,2]]
          char_table = [[1,1,1],
                       [1,1,-1],
                       [2,-1,0]]

    elif Nsites == 4 and group == "c2":
        sym_gen = [[1,0,3,2]]
        char_table = [[1,1],
                        [1,-1]]
    elif Nsites == 4 and group == "c2v":
        sym_gen = [[3,2,1,0],[1,0,3,2]]
        char_table = [[1,1,1,1],
                        [1,1,-1-1],
                        [1,-1,1-1],
                        [1,-1,-1,1]]
    return sym_gen,char_table





