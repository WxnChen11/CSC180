"""
CSC180 Assignment 1
Prof. Guerzhoy

Wenxin Chen
1002157676

Credit Card Simulator
Last Modified: October 11, 2015
"""

def initialize():
    
    #stores balance accruing interest and interest-free balance
    global cur_balance_owing_intst, cur_balance_owing_recent
    #keeps track of date of most recent operation
    global last_update_day, last_update_month
    #keeps track of last two countries where a transaction occured
    global last_country, last_country2
    #boolean used to indicate a disabled card
    global card_disabled
    #constant value of monthly interest rate
    global MONTHLY_INTEREST_RATE
    
    card_disabled = False
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = 1, 1
    
    last_country = None
    last_country2 = None    
    
    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    
    '''Return true if date1 (day1, month1) is the same as or occurs later than 
    date2(day2, month2). Return False otherwise
    
    day1, month1, and day2, month2 correspond to valid dates in the year 2016
    
    Arguments:
    day1 -- int
    month1 -- int
    day2 -- int
    month2 -- int
    '''
   
    if month1 > month2: #check if month2 occurs after month1
        return True
    elif month1 == month2 and day1 >= day2: #if both dates fall in same month
        return True
    else:
        return False

def all_three_different(c1, c2, c3):
    
    '''return True if values of c1, c2, c3 are all different from each other
    return False otherwise
    
    Arguments:
    c1 -- string
    c2 -- string
    c3 -- string
    '''
    
    if c1 != c2 and c2 != c3 and c1 != c3 and c1 != None and c2 != None and c3\
    != None:
        return True
    else:
        return False

def purchase(amount, day, month, country):
    
    '''simulates purchase of amount (amount), on the date (date, month) in the
    country (country). 
    will return error if an operation has already been completed on a later date
    will return error if the card is disabled or being disabled 
    
    Arguments:
    amount -- int/float > 0 
    day -- int, valid day in 2016
    month -- int, valid month in 2016
    country -- string, valid capitalized country name
    '''
    global last_update_day, last_update_month, last_country, last_country2,\
    cur_balance_owing_recent, card_disabled
    
    if date_same_or_later(day, month,last_update_day, last_update_month)==False\
    or card_disabled:
        return "error"
    if all_three_different(country, last_country, last_country2) == True:
        card_disabled = True
        return "error"
    
    #if month has advanced add recent balance to balance accruing interest
    add_interest(month, last_update_month)
        
    cur_balance_owing_recent += amount
        
    update_date(day, month)
    last_country2 = last_country
    last_country = country

def amount_owed(day, month):
    '''
    return the total amount owed as of the date (day, month)
    return error if an operation has been performed on a date later than 
    (day, month)
    
    Arguments:
    day -- int, valid day in 2016
    month -- int, valid month in 2016
    '''
    
    if date_same_or_later(day, month, last_update_day,last_update_month)==False:
        return "error"
    
    add_interest(month, last_update_month)
    update_date(day, month)
    
    return cur_balance_owing_intst + cur_balance_owing_recent
    
def pay_bill(amount, day, month):
    '''
    deduct (amount) from balance accruing interest first, then remaining amount
    from interest-free balance. return error if an operation has been performed
    on a date later than (day, month)
    
    Arguments:
    amount -- int/float, number > 0
    '''
    
    if date_same_or_later(day, month, last_update_day, last_update_month)==False:
        return "error"
    
    global cur_balance_owing_recent, cur_balance_owing_intst
    
    add_interest(month, last_update_month)
    update_date(day, month)
    
    if amount >= cur_balance_owing_intst:
        cur_balance_owing_recent -= amount - cur_balance_owing_intst
        cur_balance_owing_intst = 0
    
    else:
        cur_balance_owing_intst -= amount
    
    if cur_balance_owing_recent < 0:
        cur_balance_owing_recent = 0

def add_interest(cur_month, prev_month):
    
    '''add the accrued interest between prev_month and cur_month to the current 
    balance owed, and return the new owed balance
    
    Arguments:
    cur_month -- int, valid month in 2016
    prev_month -- int, valid month in 2016
    '''
    global cur_balance_owing_recent, cur_balance_owing_intst, \
    MONTHLY_INTEREST_RATE
    
    #if only one month has passed, add previous month's interest before adding
    #recent balance to balance accruing interest
    if cur_month != prev_month:
        
        cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE)
            
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0
            
        #if multiple months have passed, add interest for those months
        if (cur_month -1) > prev_month:
            
            cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE)**\
            ((cur_month-1) - prev_month)
    else:
        return None

def update_date(new_day, new_month):
    
    '''sets last date and last country to given arguments
    
    Arguments:
    
    new_day -- int, valid day in 2016
    new_month -- int, valid month in 2016
    new_country -- string, valid capitalized country name
    '''
    
    global last_update_day, last_update_month
    
    #updates last_update_[...] with latest date
    last_update_day = new_day
    last_update_month = new_month
    
initialize()		
    
if __name__ == '__main__':
    
    #Testing strategy: check Error cases for every function, while inputting
    #expected values according to assignment specifications

    #testing purchase function
    
    #Error Cases: Operation already completed on later date OR three different
    #countries in a row
    
    initialize()
    
    print("-----0------")
    #Operations completed on later date
    purchase(140, 9, 1, "Canada")
    print(purchase(150, 1, 1, "France")) #Error, operation completed on later
    # date
    print(purchase(150, 2, 1, "Russia")) #Error,operation completed on later 
    #date, card shoul NOT be disabled despite 3 different countries
    purchase(150, 9, 1, "Zimbabwe")
    purchase(150, 9, 1, "Canada")
    print("Now owing:", amount_owed(10, 1)) #Should be 440
    print("-----1------")
    
    initialize()
    
    #Three countries in a row
    purchase(140, 1, 1, "Canada")
    purchase(150, 1, 1, "France")
    purchase(150, 1, 1, "Canada")
    purchase(150, 1, 1, "France") #Should be ok
    print(purchase(150, 1, 1, "Egypt")) #Error - 3 different counries in a row
    print("Now owing:", amount_owed(1, 1)) #should be 590
    print(purchase(150, 1, 1, "France")) #Should always return error-deactivated
    print("Now owing:", amount_owed(1, 1)) #amount should stay at 590
    print("-----2------")
    
    #Three countries but not in a row
    initialize()
    purchase(150, 1, 1, "Egypt")
    purchase(150, 1, 1, "Canada")
    purchase(140, 1, 1, "Canada")
    purchase(150, 1, 1, "France")
    purchase(150, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 1)) #no errors, should be 740
    print("-----3------")

    #testing now_owing and pay_bill for Errors
    
    #Error case: return error only if operation has been completed on a later 
    #date
    
    initialize()
    purchase(140, 1, 1, "Canada")
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2)) #90
    print("Now owing:", amount_owed(2, 3)) #90 * 1.05 = 94.5
    pay_bill(50, 2, 3) # 44.5
    pay_bill(20, 5, 3) #24.5
    print("Now owing:", amount_owed(2, 7)) #24.5 * (1.05)**4 = 29.78
    print(pay_bill(20, 5, 3)) #Error, operation performed on later date
    print(pay_bill(20, 1, 7)) #Error, operation performed on later date
    print("Now owing:", amount_owed(25, 7)) #29.78
    print("Now owing:", amount_owed(18, 7)) #Error, same reason as above
    print("Now owing:", amount_owed(23, 7)) #Error, same reason as above
    print("-----4------")
    
    #test pay_bill
    
    #if amount paid is more than balance, balance should equal zero
    initialize()
    purchase(140, 1, 1, "Canada")
    pay_bill(1440, 2, 1)
    print("Now owing:", amount_owed(2, 6)) #0.0
    purchase(110, 15, 6, "Canada") 
    print("Now owing:", amount_owed(2, 7)) #110
    print("-----5------")
    
    #if amount paid exceeds accuring interest balance
    initialize()
    purchase(140, 1, 1, "Canada")
    print("Now owing:", amount_owed(1, 5)) #140 * (1.05)**3 = 162.07
    purchase(200, 2, 5, "Canada") #Balance accruing interest: 162.07
    #Interest-free balance: 200
    pay_bill(180, 2, 5) #Balance accruing interest:0 Intrst-free balance: 182.07
    print("Balance accruing interest:", cur_balance_owing_intst,\
    " -- Interest Free Balance:",cur_balance_owing_recent) #0 and 182.07
    print("-----6------")
    
    #Testing of typical cases from handout:
    
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      #80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      #30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      #31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      #71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      #41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      #43.65375
    #(=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      #83.65375 
    print(purchase(50, 3, 5, "United States"))  #error    (3 diff. countries in 
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      #83.65375 (no change, purchase
                                                #          declined)
    print(purchase(150, 3, 5, "Canada"))        #error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      #85.8364375 
                                                #(43.65375*1.05+40)