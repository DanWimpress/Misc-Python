#Using the Python language, have the function RunLength(str) take the str
#parameter being passed and return a compressed version of the string using
#the Run-length encoding algorithm. This algorithm works by taking the
#occurrence of each repeating character and outputting that number along
#with a single character of the repeating sequence.
#For example: "wwwggopp" would return 3w2g1o2p.
#The string will not contain any numbers, punctuation, or symbols. 

import collections

def runLength(userString):
    counter = 1
    i = 1
    answer = ""
    while i < len(userString):
        i += 1
        if userString[i] == userString[i-1]:
            counter += 1
        else:
            answer = answer + userString[i-1] + str(counter)
            counter = 1
    print (answer + userString[i-1] + str(counter))

    
runLength(input())
    
