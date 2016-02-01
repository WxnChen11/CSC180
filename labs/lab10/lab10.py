def power(x, n):
    
    if n == 0:
        return 1
    
    if n == 1:
        return x
    
    return x * power(x, n-1)
    
print(power(3,3))

def interleave(L1, L2):
    
    if len(L1) == 1:
        return [L1[0]] + [L2[0]]
    
    return [L1[0]] + [L2[0]] + interleave(L1[1:],L2[1:])
    
print(interleave([1,3,5,7],[2,4,6,8]))

def reverse_rec(L):
    
    if len(L) == 1:
        return [L[0]]
    
    return [L[len(L)-1]] + reverse_rec(L[:len(L)-1])
    
print(reverse_rec([1,2,3,4,5]))


def zigzag1(L):
    
    if len(L) == 1:
        return [L[0]]
        
    return zigzag1(L[1:len(L)-1]) + [L[0]]  + [L[len(L)-1]]
    
# def zigzag1(L):
#     
#     if len(L) == 1:
#         print (L[0])
#         return [L[0]]
#     
#     
#     return zigzag1(L[1:len(L)-1])
    
    
def is_balanced(s):
    
    s = "".join(sorted(s))

    if len(s) == 1:
        print("b")
        return not "(" in s and not ")" in s
        
    if len(s) == 2:
        print("a")
        return ("()" in s)
        
    if s[0] == "(" and s[-1] == ")":
        return is_balanced(s[1:len(s)-1])
        
    # if s[0] == "(" and s[-1] == "(":
    #     return is_balanced(s[1:len(s)-1])

    if s[0] == "(":
        return is_balanced(s[:len(s)-1])
    
    if s[0] == ")" and s[-1] == "(":
        return is_balanced(s[1:len(s)-1])
        
    # if s[0] == ")" and s[-1] == ")":
    #     return is_balanced(s[1:len(s)-1])   
        
    if s[0] == ")":
        return is_balanced(s[:len(s)-1])
    
    return is_balanced(s[1:])
    


print(zigzag1([1,2,3,4,5,6,7]))

print(is_balanced("()()()"))

print(is_balanced("()()())"))

print(is_balanced("(well (I think), recursion works like that (as far as I know)"))

print(is_balanced("()()())"))












