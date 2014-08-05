#Using the Python language, have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is
#a prime number, otherwise return the string false. The range will be between 1 and 2^16. 


def primeTime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True


print (primeTime(int(input())))
