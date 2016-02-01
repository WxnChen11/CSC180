#Problem 1
y=0
for i in range(0,100000):
    y+= (-1)**i  / ( 2*i + 1 )

print(y)
print(4*y)

#Problem 2

for z in range(5,1,-1):
    print(z)

def simplify_fraction(n,m):
    '''n and m must be positive'''
    greatest_common=-1;
    for i in range(n, 1, -1 ): #work through n to find factors, greatest to least
        if n%i==0:
            for z in range (m, 1, -1): #once a factor is found in n, compare w/ all factors in m
                if m%z==0:
                    if i==z: #greatest common factor
                        greatest_common=i;
                        if m/greatest_common==1:
                            print (int(n/greatest_common))
                            #return
                        else:
                            print (int(n/greatest_common), "/", int(m/greatest_common)) 
                            #return


simplify_fraction(3,6)
simplify_fraction(4,2)
simplify_fraction(9,3)
simplify_fraction(81,99)
simplify_fraction(162,198)

#Problem 3

import math

def approx_pi(n):
    sum=0
    for i in range(0,1000000000000*n):
        sum+= (-1)**i  / ( 2*i + 1 )
        if (int(4*sum*(10**(n-1))))==(int(math.pi*(10**(n-1)))):
            print(i,"terms were required to approximate pi to", n, "digits. Value of Leibniz Formula times 4:", 4*sum, " Value of pi :", math.pi )
            break
        #print(int(4*sum*(10**(n-1))))
        #print("",int(math.pi*(10**(n-1))))

approx_pi(7)


#print(int(4*sum*(10**(n-1))))
print("",int(math.pi*(10**(5-1))))

#Problem 4

def next_day(y,m,d):
    if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d==31:
        m+=1
        d=1
    elif (m==4 or m==6 or m==9 or m==11) and d==30:
        m+=1
        d=1
    elif m==12 and d==31:
        y+=1
        m=1
        d=1
    elif m==2 and d==28:
        if y%4==0 and y%100==0 and y%400!=0:
            m+=1
            d=1
        elif y%4==0:
            d+=1
        else:
            m+=1
            d=1
    elif m==2 and d==29:
        m+=1
        d=1
    else:
        d+=1
    
    print("Tomorrow's date is: (",y,m,d,")")

next_day(1600,12,31)
next_day(1991,6,5)

def count_days(y,m,d,y2,m2,d2):
    count=0
    y1=y
    m1=m
    d1=d
    
    #checking input
    if y>y2:
        return
    if y==y2 and m>m2:
        return
    if y==y2 and m==m2 and d>d2:
        return
        
    #loop
    while y2!=y or m2!=m or d2!=d:
        if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) and d==31:
            m+=1
            d=1
        elif (m==4 or m==6 or m==9 or m==11) and d==30:
            m+=1
            d=1
        elif m==12 and d==31:
            y+=1
            m=1
            d=1
        elif m==2 and d==28:
            if y%4==0 and y%100==0 and y%400!=0:
                m+=1
                d=1
            elif y%4==0:
                d+=1
            else:
                m+=1
                d=1
        elif m==2 and d==29:
            m+=1
            d=1
        else:
            d+=1
        
        print("(",y,m,d,")")
        count+=1
        
    
    print()
    print("There are",count,"days between (",y1,m1,d1,") and (",y2,m2,d2,")")
    #print("There are",count,"days between (",y,m,d,") and (",y2,m2,d2,")")

        
count_days(1996,2,17,1996,3,18)


print(int(8/3))

def euclid_algo(a,b):
    ao=a
    bo=b
    y=a%b
    
    while y!=0:
        a=b
        b=y
        y=a%b
        
    print("The GCF of", ao, "and", bo, "is", b)

euclid_algo(2322,654)
euclid_algo(45984,1248)
euclid_algo(636,1221)
euclid_algo(2323543542,6543687)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    