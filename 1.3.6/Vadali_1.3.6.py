import random
'''Introduction'''
# 1 - 3
'''Part I: Tuples, Syntax'''
#4  
a = (1,3,4)

#5 In python, we have a specific template to use in order to create out 
# docstrings. Our teacher told us what the docstring needs to consist of and how 
# we need to turn it in. However, we have no conventions when creating and naming
# new variables, unless he specifically explains to name it a certain variable.

#6
some_values = ('a', 'b', 3)
#a) some_value[1] will output 'b' because it is the second tuple and the first 
# for the indexer. 

#b) some_values[0:2] will output 'a' and 'b' because it is the first and second 
# value in the tuple, or the 0 and 1 in the indexer. 

#7) 
a = 10
b = (9, a, 11)
#a) For the first value, it will output True. It is true because of the code, 
# 'b[1] == 10' is asking if the seond value in the tuple is 10. since a = 10 and
# a is the second value, b[1] == 10 is true.
#b) This will output 10. Since a = 10, 10 will substitude with a in the tuple, 
#   and will make b[1] output 10. This is the reason why, because a = 10. 
'''Part II: Lists '''
#8) The code values[1:] will output ['b', 3] because it is the second value to 
# the last value, making it 'b' and 3 where be s a string and 3 is an integer. 

#9) The code will output False because of the types being different. Using the 
# code, 'values[2] = '3'', you are assigning value[2] to '3'. However, that is a
# string and 3 is an integer, making it False.

#10)
#   a) This code, 'values = values + [4, 5]' will append the values to the end of
# the list. Since, you are adding two list together, they will append to the end
# of the list you are adding it to 

#   b) 'values.append([6, 7])' will append the list, including the square brackets
#   to the end. This is because you are appending the list and the brackets to the
#   end of the list. 

#11) This will not work because you are not able to add and integer to a list. 
# This is impossible because a list can consist of strings, integers, and floats.
# However, an integer will not be able to add ot all thet types, and 'can only 
# concatenate list (not "int") to list'.

#12) If 'a = 6 ' and if you short hand the multiplication, it would be the same 
# as doing a = a * 3. Both ways will come out to the same answer of 18. 
'''Part III: Lists and the random module '''
#13) N/A

#14) 
def roll_two_dice():
    """Using the imported random code, I am cerated a random generater, 
    impersanation 2 die. this will give a value in between 2 and 12, since they 
    are the least and greatest value you can roll for two die"""
    return random.randrange(2,12)
     
"""Conclusion"""

#1) The variable a is a string, and 'a[3]' will output 'd'. The variable b is 
#bound to the tuple because it is explained that b is a variable that is equal 
#to a tuple. Finally, c is the name of the list. However, all the three 'a[3'  
#'b[3]', and 'c[3]' will output 'd'. 

#2) Many coding languages have different variable roles and variable types 
# because they have numerous syntax differences. There are many different 
# commands and that created many different variable types. Like how an integer 
# and float may exsist in python, only a int will exsist in java. This shows how
# we have a variety in variable types. However, not everything can be an integer.
# Like in the average verbal language of english, a number is not a letter. 
# There are many methods to turn it into a word by spelling it out. Relating this
# back to python, not all data types are integers, and can not work with integers.
# This will create a sintax error, and like in english, you addeding '5 + blue',
# it is impossible.

#3) Throughout 1.3.2 to 1.3.6, we discussed the basis of python. We talked about
#how to create a list, integer vs float, importing code, printing using python 3,
#and finally, list, tuples. This is the basis of coding python because if you 
#have no knowledge on this information, it is hard to create data sets that you 
#are able to use to calculate a price value with a tip, organize your computer 
#data, or do any raw imputs. We learned many needed topics and understand how to
#create for loops and work on docstrings and other types of code in order to best
#shape our coding skills. 

"""Assignment Check"""
#1.3.6 Function Test
print(roll_two_dice())

#1) I believe that my code works. Since it is randoming generating a value from 
# 2 - 12, it is showing that I successfully coded my part. In order to see if my
# code is functional, I tested it multiple times, seening that a new number is 
# coming each time. This means taht I successfully did the assignment. 