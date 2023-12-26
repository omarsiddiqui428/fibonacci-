#without recursion

def fibonacci(x):
    n = x-2
    y = [0,1]
    while n > 0:
        y.append(y[-1] + y[-2])
        n -= 1
    print(y)

fibonacci(25)


#with recursion- this one gives us the x number of the fibonacci sequence counting 0 as the first number of the sequence. Still need to figure out how to make it show the entire sequence
#somehow make a string y and keep adding to the 0 index, and then print the y string at the end. Not sure how to create the y string at first in a way that it doesn't change 
#this whole fuction just gives us the x number in the sequence, I need this whole thing to run for x and every number before it down to 1 and print those outputs 

def fibonacci(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(5))

#used no help until this point, was having an issue figuring out how to print all the numbers UP to the X number in the sequence, so I got help for that online 
#Got the below, but I think we said no loops, so not sure if the i in range (x,x+1) is allowed here

def fibonacci(x):
    def fib(x):
        if x == 1:
            return 0
        if x == 2:
            return 1
        else:
            return fib(x-1) + fib(x-2)
        
    fibonacci_sequence = []
    for i in range (1,x+1):
        fibonacci_sequence.append(fib(i))
        print(fib(i))
    return fibonacci_sequence

fibonacci(20)
