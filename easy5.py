#Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num.
#For the test cases, the parameter num will be any number from 1 to 1000.

import sys

def simpleAdding(num):
    answer = 0
    if num < 1:
        print ("Number must be 1 or greater")
        sys.exit()
    for i in range(1, num+1):
        answer += i

    print(answer)

simpleAdding(int(input()))
