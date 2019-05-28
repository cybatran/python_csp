"""Procedure"""
# 1 - 4

#5 ) int 

#6 ) For the first example, it is two strings connecting to eachother, therefore,
#   making it a string. However, the second example is a string and an integer, 
#   making it have two types, and also you are not able to connect two different 
#   types. 

# 7) The final code will output an 'h' because it is going back from the starting
#   index, to the end. This means that slogan[-2] outputs 's'. Using this, 
#   slogan[-7] should output 'h'. 

#8) slogan[17: ] should output 'best'

#9 In []: "Dublin High School" + slogan[9:]  
#  Out[]: 'Dublin High School is the best'

# 10 a) This would print out 7 because there are 7 characters from the start to 
#       end
# 10 b)  It should pring out 'theat' because of the len being an integer so 
#   len(activity) - 1 is 7 - 1 so it is 6. 

#11) It outputed True the words 'test and 'goo' are in the phrase, meaing that 
#   it is true and is in the phrase.  

#12
def how_eligible(essay):
    count = 0
    if "?" in essay:
        count += 1
    if '"' in essay:
        count += 1
    if ',' in essay:
        count += 1
    if '!' in essay:
        count+= 1
    return count
    
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

#In this assignment, I got a result of 4 and 1. In the line, there are 4 
#puncuation marks on the first one, and 1 on the second phrase. This makes me 
#believe that I successfully did the assignment.  
