#Problem 1

def list1_start_with_list2(list1, list2):
    
    if len(list1) >= len(list2):
        for i in range (len(list2)):
            if list1[i] != list2[i]:
                return False
            
    elif len(list1) < len(list2):
        return False
    
    return True

print(list1_start_with_list2([1, 2, 3, 4, 5],[1, 2])) #True

print(list1_start_with_list2([1, 2, 3, 4, 5],[1, 3])) #False

print(list1_start_with_list2([1, 2, 3, 4, 5],[2,3])) #False 

print(list1_start_with_list2([1, 2, 3, 4, 5],[1, 2, 3, 4, 5])) #True

print(list1_start_with_list2([1, 2, 3, 4, 5],[1, 2, 3, 4, 5, 6])) #False

print("----------Problem 1 Finished-------------")

#Problem 2
def match_pattern(list1, list2):
    
    num_match = 0
    
    for i in range (len(list1)):
        if list1[i] == list2[0]:
            num_match = 0
            for z in range (1, len(list2)):
                if list1[i+z] == list2[z]:
                    num_match += 1
            if num_match == len(list2)-1:
                return True
    return False
                
print(match_pattern([1,2,3,4,5,6],[3,4]))

print(match_pattern([1,2,3,4,5,6],[1,2,3,4]))

print(match_pattern([1,2,3,4,5,6],[1]))

print(match_pattern([1,2,3,4,5,6],[6]))

print(match_pattern([4, 10, 2, 3, 50, 100],[2, 3, 50]))

print(match_pattern([4, 10, 2, 3, 50, 100],[4,2]))

print(match_pattern([4, 10, 2, 3, 50, 100],[10,2,50]))

print(match_pattern([4, 10, 2, 3, 50, 100],[4,10,2,3,50,101]))

print(len([2,3,4]))

print("----------Problem 2 Finished-------------")

#Problem 3
def duplicates(list0):
    
    for i in range (len(list0)-1):
        if list0[i] == list0[i + 1]:
            return True
    
    return False

print(duplicates([1,2,3,4,5,6])) #False
print(duplicates([1,1,2,3,4,5])) #True
print(duplicates([1,2,3,4,6,6])) #True
print(duplicates([6,5,6,5,6,5,6])) #False

print("----------Problem 3 Finished-------------")


#Problem 4 Part A

def print_matrix_dim(M):
    
    try:
        print ( len(M), "x", len(M[0]) )

    except TypeError:
        print ( 1, "x", len(M) )
        
    # else:
    #     print ( len(M), "x", len(M[0]) )

print_matrix_dim([[1,2],[3,4],[5,6]])

print_matrix_dim([[1],[3],[5]])

print_matrix_dim([1,2,3])

print_matrix_dim([1])

print("----------Problem 4 A Finished-------------")

#Problem 4 Part B

def mult_M_v(M,v):
    
   
    try:
        test_1_col = len(M[0])
       
        res=[0]*(len(M))
        
        for i in range (len(M)):
           for z in range(len(M[0])):
                res[i] += M[i][z]*v[z]
           
    except TypeError:
        
        res=[0]
        
        for i in range(len(M)):
           res[0] += M[i]*v[i]
           
    return res
    

print (mult_M_v( [ [1,2] , [3,4], [5,6] ] , [9,9] )) #[27,63,99]

print (mult_M_v( [1,2] , [9,9] )) #27

print ([0]*10)

#Problem 5

#Problem 6

def sum_squares_two_diff(num):
    
    res = []
    count = 0
    skip_value = []
    
    for i in range(1, num):
        
        if i in skip_value:
            continue
        
        for x in range(1, num): 

            if (i**2 + x**2) == num:
                
                skip_value.append(x)
                #skip_value.append(i)
                
                res.append([i,x])
                
                count += 1
                
    if count >= 2:
        return True
        
    return False

print(sum_squares_two_diff(1385))

print(sum_squares_two_diff(1))

print(sum_squares_two_diff(1))

print (sum_squares_two_diff(25))


def square_taxi_count(n):
    
    count = 0
    
    for i in range(n+1):
        
        if (sum_squares_two_diff(i)):
            
            count += 1
            
    return count
        
print(square_taxi_count(200))

print(square_taxi_count(145))


















