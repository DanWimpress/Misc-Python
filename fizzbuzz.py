#Fizzbuzz lulz
#Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print (str(i) + " fizzbuzz")
        elif i % 3 == 0:
            print (str(i) + " fizz")
        elif i % 5 == 0:
            print (str(i) + " buzz")
        else:
            print (str(i))

fizzbuzz()
