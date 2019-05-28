#code

#Question-1 (Problem 5) It made a histogram that we are able to see and create. It imported files and we were able to create this

def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
    
def hyp(leg1,leg2):
    return (leg1**2 + leg2**2)**0.5

def mean(*args):
    total = 0
    for num in args:
        total += num
    return total/float(len(args))

def perimeter(base,height): # of a rectangle
    if base == height:
        print "It is a square!"
        return base **2
    else:
         return (base * 2 + height * 2)
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)  
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)

