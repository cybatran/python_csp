from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

"""Procedure"""
#1-3

"""Part I: for loops, range(), and help()  """
#4
def days():
    ''' 
    Function packages file that tells the days of a week and tells a day in 
    september in a range of 5 to 8
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
#5

def picks():
    """
    Creates a histogram that shows that shows the value resluts through a random
    code taht chooses between 1, 3, 10
    """
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

#6

def roll_hundred_pair():
    """
    Ceates a histagram that shows the number rolls of two dice for 1 million 
    rolls and will create it using a plt.hist  and plt.savefig in order to crate
    the graph
    """
    rolls = []
    for roll in range(1000000):
        rolls.append(random.randint(1,6) + random.randint(1,6))
    plt.hist(rolls)
    plt.savefig('1.3.7/roll101pair')
    
def dice(n):
    """
    Packages code that tels how many time it would take in order to get a number 
    by rolling a dice through a for loop and a random import
    """
    roll = 0
    for rollz in range(n):
        roll += random.randint(1,6)
    print( "Roll was " + str(roll))
"""Part II: While loops"""
 #7
 

def validate():
    """
    Packaged code that askes for a letter in 'hangman' to demonstrate the use of 
    while loops
    """
    guess = "1"
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

#Line 2 is important because it is making a True statement, letting the while 
# loop working. However, if we comment it out, the while loop will not work and 
#if we change guess toa letter in the answer, it won't work because the loop 
# only works if guess in NOT in answer.

#8 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Packages code that random generates a name from player in order to guess 
    who won the lottery through random and also using a guess number counter
    '''
    winner = random.choice(players) 

    ####
     #This is explaining that it will randomly generate the winner through the 
     #players name
    
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]:
        #This is giving an end due to it being True 
        print(p+', ', end='')
    print(players[len(players)-1])
    #Prints Guess Again if it wasn't the player name

    ####
    # Gives you the option to guess who won without using a raw imput
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
#9
def goguess():
    """
    Packages code that allows you to guess numbers through the a random randint 
    code and tells if the number is too less or too big
    """
    guesses=0
    answer = random.randint(1,20)
    print(answer)
    guess = raw_input("Guess:")
    while guess != answer:
        if int(guess) < int(answer):
            print (guess, 'is too low')
            guess = raw_input("Guess:")
            guesses += 1
        elif int(guess) > int(answer):
            print (guess, 'is too high')
            guess = raw_input("Guess:")
            guesses += 1
        elif int(guess) == int(answer):
            guesses += 1
            print ('Right! My number is', answer, '!', 'You guessed in', guesses,
            'guesses!')
            break
        else:
            print("Please print a number")
            guess = raw_input("Guess:")
#10
# If I change 20 to 6000, I would need 5999 guesses to be 100% right that I would
# get the correct answer because On the 5999 guess I would be 100% sure that I 
#got the next answer correct, due to the fact that the answer could be anything 
# from 1 to 6000.  

"""Part III: Practice"""
#11
    #a
def matches(ticket, winners):
    """
    Packages code that tells how many numbers you have in the ticket and in the 
    winner through a for loop
    """
    amount = 0
    for number in ticket:
        if number in winners:
            amount +=1
        else:
            amount += 0
    return amount
    
    #b
def report(guess, secret):
    """
    Packages code that tells how many are correct from a list of guess and 
    secret for the game 
    """
    right_space = 0
    right_color = 0
    answer = []
    for i in range(len(secret)):
        if secret[i] == guess[i]: 
            right_space += 1 
        if guess[i] in secret[i]:
            right_color += 1
    answer.append(right_space) 
    answer.append(right_color)
    return answer
        
"""Conclusion"""
#1 A benefit is that you have the power to ensure that some code happens for a 
# step times. However, thios leads to the code being very clustered and messy, 
# hard to read and write the code. Also you would have to write the code numerous
# time, while in a loop, you can write it once and put it in a loop. 

#2 Iterations and analysis of a large data set both share to repeating of certain
# processes until a desired result occurs. You also iterate through large data 
# sets such as lists and also dictionaries in order to run code based on the set.
# This means that you will need a large data set in order to iterate through it.
# Therefore, if you desire to iterate, it is dependent on a large data set. 

#3 Both a for and while loop run a body of ciode numerous times. However, unlike
# a for loop, a while loop will run for a certain condition and will stop if the
# condition is not true. While loops are depended on bolean whiile for loop 
# iterate throuhg dictionaries and lists in order to run code and will stop if 
#there is nothing to iterate through.

#4 For this unit, my partner aned I worked effectly with eachother to a certain 
# extent. We would help eachother for the problems which he had issues with. 
# However, this meant taht we woulr be working by ourselves, but discussing 
# what we got as solutions. 

"""Assignment Check"""
print (days())
print(picks())
print(dice(5))
print(validate())
print(guess_winner())
print(goguess())
ticket = [1,3,17,567,22,34,6,54]
winners = [1, 32,44,4,3,17,6]
print(matches(ticket, winners))    
guess= ['black','green','blue','yellow','red']
secret = ['black', 'orange', 'blue','yellow','yellow']
print(report(guess, secret))