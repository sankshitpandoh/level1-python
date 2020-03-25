import sys
#collatz conjecture fucntion
def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return(number//2)
    else:
        print(number * 3 + 1)
        return (number * 3 + 1)
print('Enter any number')
try:
    user_number = int(input())
    result = int(collatz(user_number))
    if result == 1:
        sys.exit()
    else:
        while result != 1: #keep callingcollatz untill we get 1
            result = int(collatz(result))  
except ValueError:
    print('You were asked to put in a number -__-')
    sys.exit()  