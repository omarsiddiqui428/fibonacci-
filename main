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

def fibonacci(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(5))
