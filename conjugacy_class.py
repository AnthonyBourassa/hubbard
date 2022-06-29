e = np.array([[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]])
              
c = np.array([[0,0,0,1],
              [0,0,1,0],
              [0,1,0,0],
              [1,0,0,0]])

od = np.array([[0,1,0,0],
               [1,0,0,0],
               [0,0,0,1],
               [0,0,1,0]])             

of = np.array([[0,0,1,0],
               [0,0,0,1],
               [1,0,0,0],
               [0,1,0,0]])                 
          
    
          
          
          
list1 = np.array([e,c,od,of])

print(list)

def conjugacy_class(list):
    sum = 0
    list2 = []
    list3 = []
    for i in range(len(list)):
        for j in range(len(list)):
            for k in range(len(list)):
                if np.array_equal(list[i], np.dot(list[j],np.dot(list[k],np.linalg.inv(list[j])))):
                    sum += 1
                    print(list[i])
                    print(list[k])
                    print(np.dot(list[k],np.linalg.inv(list[j])))
                    
                    
                    if not np.array_equal(list1[i],np.any(list2)) and np.array_equal(list1[k],np.any(list2)):
                        list2.append([list[i]])
                        list2.append([list[k]])
    return sum,list2,list3 
                
print(conjugacy_class(list1))            
