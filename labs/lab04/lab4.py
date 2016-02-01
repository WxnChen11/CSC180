#Problem 1

def list_to_str(lis):
    '''returns list of strings
    Args:
    lis -- list of integers
    '''
    
    res="["
    
    if len(lis) == 0:
        res += "]"
        return res
    
    for i in range(len(lis)):
        if i+1 == len(lis):
            res += (str(lis[i]) + "]")
        else:
            res += (str(lis[i]) + ",")
            
        
    return res

testlist=[4,5,6,7,5,1,3,2,1,3,"bob"]

list_to_str(testlist)

if testlist[2] == 6:
    print("oops")
if testlist[2] == "6":
    print("yay")
    
print(list_to_str(testlist))
print(list_to_str([1]))
print(list_to_str([]))

#Problem 2

def lists_are_the_same(list1, list2):
    
    '''checks if two lists contain the same elements in orderArgs:
    list1 -- list of integers 
    list2 -- list of integers'''
    
    if len(list1) != len(list2):
        return False
    
    for i in range (len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

listone=[2,3,4,5,6]
listtwo=[2,3,4,5,6]

if lists_are_the_same(listone, listtwo):
    print("lists are the same")

listone=[1,2,3,4,5]
listwo=[2,3,1,4,5]

if lists_are_the_same(listone, listtwo)==False:
    print("lists are not the same")
    
listone=[2,2,2,2]
listwo=[2,2,2]

if lists_are_the_same(listone, listtwo)==False:
    print("lists are not the same")

listone=[0]
listtwo=[0]

if lists_are_the_same(listone, listtwo):
    print("lists are the same")