#Needed for array() and dot()
from numpy import *

#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = array([[1,-2,3],[3,10,1],[1,5,3]])
x = array([75,10,-11])
b = dot(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

#To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

M = array([[5,6,7,8],[0,0,0,1],[0,0,5,2],[0,1,0,0]])

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    
    return len(row)
    
print(get_lead_ind(M[1]))
    
def get_row_to_swap(M,start_i):
    
    toswap=-1
    highest=len(M[0])
    
    for i in range(start_i, len(M)):
            if get_lead_ind(M[i]) < highest:
                highest=get_lead_ind(M[i])
                toswap=i
    
    return toswap
                
print(get_row_to_swap(M, 0))

L=[1,2,3,4]
L2=[1,2,3,4]
L[1]*=2

print(L)

L+=L2

print(L)

def add_rows_coefs(r1, c1, r2, c2):
    
    res=[]
    
    for i in range(len(r1)):
        r1[i]*=c1
    
    for z in range(len(r2)):
        r2[z]*=c2
        
    for r in range(len(r1)):
        res+=[r1[r]+r2[r]]
        
    return res
    
M = array([[5,6,7.0,8],[0,0,0,1],[0,0,5,2],[0,1,0,0]])

    
print(add_rows_coefs(M[0], 2.0, M[2], 1.5))
    
def eliminate(M, row_to_sub, best_lead_ind):
    
    for i in range(row_to_sub+1, len(M)):
        if M[i][best_lead_ind] != 0:
            for z in range(best_lead_ind, len(M[i])):
                M[i][z]-= M[row_to_sub][z]*((M[i][best_lead_ind])/(M[row_to_sub][best_lead_ind]))

M = array([[5,6,7.0,8],[0,0,1,1],[0,0,5,2],[0,0,7,0]])

eliminate(M, 1, 2)

print(M)
    
def normalize_row(r):
    
    denom = 0
    
    for z in r:
        denom += z
    
    for i in range(len(r)):
        r[i] = r[i]/denom
    
normalize_row(M[0])

print(M)

def forward_step(M):
    
    for i in range(len(M)):
        
        swap = get_row_to_swap(M, i)
        print(swap)
        M[i], M[swap] = M[swap], M[i]
        print("Mi", i, M[i])
        print("Mswap", M[swap])
        
        print(array(M), "\n")
        
        eliminate(M, i, get_lead_ind(M[i]))
        
        print(M, "\n")

M = [[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]]

forward_step(M)
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    