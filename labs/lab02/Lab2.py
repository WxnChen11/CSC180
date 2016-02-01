'''Tutorial #2 - Tues Sept. 22
http://www.cs.toronto.edu/~guerzhoy/180/labs/lab02.pdf'''

val=0
undo=0

def display_current_value():
    global val
    print("Current Value:",val)

def add(to_add):
    global val, undo
    undo=val
    val=val+to_add

def mult(to_mult):
    global val, undo
    undo=val
    val=val*to_mult
    
def div(to_div):
    global val, undo
    undo=val
    val=val/to_div

def sub(to_sub):
    global val, undo
    undo=val
    val=val-to_sub

def store_mem():
    global mem, val
    mem=val

def recall_mem():
    global mem, val, undo
    undo=val
    val=mem
    
def undo_func():
    global val, undo
    val=undo

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current value: 0")
    add(21)
    display_current_value()
    add(3)
    display_current_value()
    mult(3)
    display_current_value()
    div(5)
    display_current_value()
    sub(20)
    display_current_value()
    store_mem()
    mult(-5)
    display_current_value()
    recall_mem()
    display_current_value()
    undo_func()
    display_current_value()
    add(50)
    display_current_value()
    mult(7)
    display_current_value()
    undo_func()
    display_current_value()
    recall_mem()
    display_current_value()
    undo_func()
    display_current_value()
    
    
