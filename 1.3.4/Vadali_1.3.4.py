from __future__ import print_function # must be first in file 
import random

"""Procedure"""
#1-4 N/A

"""Part I. Nested if structures and testing"""
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1 a N/A
#  b 
#   i) If the string placed in the parameters is in the list known as citrus and 
#       fruits
#   ii) If the string placed in the parameters in not in the list know as citrus 
#       and fruits
#   iii)If the string is not in the the food list, and is in the starch list, it
#       could execute it.
#   iv) If the string is not in the food list, and is not in the starch list. 
#  c 
#    Since the first if statement is saying that what ever you place in the 
#    parameters is in the fruits list, execute this. If it isn't, do this. Since
#    banana is in the fruits list, it will go under the if statement. 

#2
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)

#3
def f(n):
    ''' Using the n parameter in order to to tell wheiter something is an integer
        , and if so, is it even or odd'''
    if type(n) == int:
        if n%2 != 0:
            print ("odd")
            return "odd"
        elif n%3 == 0 and n%2 == 0:
            print ("The number is a multiple of 6")
            return "The number is a multiple of 6"
        else: 
            print ("even")
            return "even"
    else: 
        print ("It is not an integer")

#4 Its a canapy 

#5 

def f_test():
    '''This is a method to test to see if the f(n) is working amd will return 
    True
if good, return False and prints error if not good'''
    works = True
    if f(3) != "odd":
        works = 'odd is a bug in the code'
    if f(2) != "even":
        works = 'even is a bug in the code'
    
    if works == True:
        print('All good!')
        return True
    else: 
        print(works)
        return False
   
"""Part II: The raw_input() function, type casting, and print() from Python 3"""
#7 The difference is for addition in concatination, you are adding mutiple string
#in order to prinnt a string. However, for a numeric addition, you are adding the
#two valuing to return a new value.
#chungachungachungachungachunga
#8 
def guess_once():
    '''It uses the variables secret and guess, in order to use a raw imput of a 
    function to see if you did a random generate dnumber'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
       if guess < secret:
           print('Too low - My number is', secret, end='!\n')
       else: 
            print('Too high - My number is', secret, end='!\n')
    else:
        print('Right, my number is', guess, end='!\n')
#   a In line 11 there are three arguments: two strings and a keyword=value pair.
# The two strings 'Right, my number is' and 
# guess are joined with a space separator. This is how they are showing the value
# using the variable guess. 
# The end='!\n' argument is adding an ! at the end of the print string. 

# 9

def quiz_decimal(low, high):
    '''Using the function of quiz_dcimal in order to show if a number is in 
    betweeen two values using the a raw imput and a variable called number'''
    print('Type a number between %s and %s' %(low,high))
    number = float(raw_input('Number: '))
    if number > float(high):
        print('No, %s is greater than %s' %(number,high) ) 
    elif number < float(low):
        print('No, %s is less than %s' %(number,low) ) 
    else:
        print('Good! %s < %s < %s' %(low, number,high))
        
'''Conclusion'''

'''1) The glass-box method is places in order to test and see if all the parts of
the code is working. This means that it will look at every corner of the code and
see if it is functional. This method is used in the if-else statemts because of 
the many functions that are places and to see if what the scope is.'''

'''2) In an if-else statement, not all the code will be present. If - else 
statement is like binary to tell if a statement is true, and if so go the function.
This is like an 0 1 to tell if something is a true statement. '''  

'''3) A test suite runs code several times, providing different input or 
arguments, to see if the code is functional and is outputting value it in needed
to output and cases that cover a range of possibilities  a range so that all 
lines of code get tested. '''

'''4) '''
def f_type(n):
    ''' Using the n parameter in order to to tell wheiter something is an 
     integer'''
    if type(n) == int:
         print('It is an integer')
         return int
    else:
        print('It is not an integer')
        return "not int"
def f_odd(n):
    ''' Using the n parameter in order to to tell wheiter something is a even or
    odd number'''
    if n%2 != 0:
        print('It is odd')
        return "odd"
    else:
        print('It is even')
        return "even"
def f_multiple(n):
    ''' Using the n parameter in order to to tell wheiter something is divisble 
    by 6'''
    if n%3 == 0 and n%2 == 0:
        print('It  is divisble by 6')
        return "multiple of 6"
    else:
        print('It is not divivble by 6')
        return 'not a multple of 6'
'''Challenge'''
#1 

def f_challenge(n):
    '''Using the parameter of n in order to output all the possible values when 
    n is equalivalent to a value and the function is being called'''
    if n % 2 != 0:
        return "odd"
    elif n % 3 == 0 and n % 2 == 0:
        return "Multiple of 6"
    else:
        return "even"

        
'''Assignment Check'''
#1 I believed that I did the assignment correctly because of the fact that there
#are no errors and all my code is present. This means taht I did not have any 
#error in my code for the previous answers and also no errors in the challenge.
#harsha ur bad
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
print(f_challenge(1.1))
print(f_challenge(2))
print(f_challenge(3))
print(f_challenge(6))


 