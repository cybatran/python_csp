from __future__ import print_function # use Python 3.0 printing 

'''Procedure'''
#1-5 N/A

'''Part 1: Conditionals'''

#6a I believe that it is False
#   my prediction was wrong. Since 3 > 3 is false, not 3 > 3 is true. A true
#   and a true is a true.

#6b I believe that it is True
#       my prediction was correct

#7 x, y = (65,40) 
    # 50 < x and 50 < y and 64 < x

#8 x,y = (90,115)

"""Part II: 
if else 
Structures 
and the print() Function"""

def age_limit_output(age):
    '''This function tells if the age is in the limit and it will need the 
    age parameter in order to tell if it is below or above the limit'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT) 
#9a 
#10 is below the age limit.  Minimum age is  13

# 16 is old enough. Minimum age is  13

def report_grade(percent):
    """This function shows and tells if the percent is a passing or failing 
    grade using the percent parameter"""
    if percent < 80:
        print ("A grade of %s does not indicate mastery" %(percent) )
        print ("Seek extra help!")
    
    else:
        print ("A grade of %s indicates mastery" %(percent) )
        print ("Keep up the good work")
     
#9b       
#   A grade of 79 does not indicate mastery. Seek extra help!
#  A grade of 85 indicates master. Keep up the good work.

'''Part III. The in operator and an introduction to collections'''
#10 True and False

#11
def vowel(letter):
    '''The function looks through and when given a value, tells if it is true 
    or false'''
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False

def letter_in_word(guess, word):
    '''The function of the code is to see if a letter in a word. It imputs true 
    if it is there, and false if it is not'''
    if guess in word: 
        return True
    else:
        return False

#12 

def hint(color, secret):
    '''In MasterMind, one player has a secret sequence of colored pegs. Another 
    player tries to guess the sequence.'''
    if color in secret:
        print ("The color %s IS in the secret sequence of colors" %(color))
    else:
        print ("The color %s IS NOT in the secret sequence of colors" %(color))

'''Conclusion'''

'''1) In the if elif and else, code in the block of indent between it is what we
will run if the value is true. That means that if you want the computer to print 
something if it is true for this value, it will print it in this value. If the 
true value is false, it would go to the elif or else code. If the elif code is
wrong, it would finally go to the else code. The placement of the code is 
importnat, and it will run from if to the last one, in a order list.'''

''' 2)  if-else
        return 
        == 
        != 
        and 
        or 
        not 
        type
        <>
        <==>'''
        
''' 3) Ira (Somewhere): I believe that because yes it may make it faster, it would
not make it much faster. Since each code run in less than a millisecond, it won't
make any difference for the human.
This is why I believe that that it is somewhere close. 

    Jayla (Somewhere): I believe that Jayla's first statement in corrct. The 
        code will run even if the it in at the top or bottom. However, I believe 
        that her second part isnot correct. since there is no reason to change it,
        they don't need to move it. This is why I believe that she is in the 
        middle. 
    
    Kendra (Correct): I believe that she is correct because of the code will work.
    Also, more code will take up more space. This is a good opinion and it is 
    correct. This is the reson why I believe that she is correct. '''
    


#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)
