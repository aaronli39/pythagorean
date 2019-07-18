import math
import random


# checks if parameter a/b make up a triple with c(the third parameter)
def check_triple(a, b, c):
    return ((a ** 2) + (b ** 2) == (c ** 2))

# given a limit, return a random triple
def randTriple(lim):
    # if aaron or sadia return something
    if lim == "aaron": return "bro try harder"
    elif lim == "sadia": return "wow so cool!!!!@*(#&(*!@&#"
    elif type(lim) == type("asdf"): return "input a number pls"
    
    # store temporary random number between 1 and limit
    temp = random.randint(1, lim)

    # check from 1 - temporary random number for triple
    for i in range(1, temp):
        if math.sqrt((i ** 2) + (temp ** 2)).is_integer():
            return temp, i ** 2, (i ** 2) + (temp ** 2)
    # check from temporary random number to limit for triple
    for i in range(temp, lim):
        if math.sqrt((i ** 2) + (temp ** 2)).is_integer(): 
            return temp, i ** 2, (i ** 2) + (temp ** 2)

# finds the missing side given 2 sides
def find(x, y):
    # if the sqrt of the square of the two inputs is an integer,
    # then the answer is just the sqrt of the sum of the squares
    if math.sqrt((x ** 2) + (y ** 2)).is_integer(): 
        return math.sqrt((x ** 2) + (y ** 2))
    else: 
        # otherwise, the answer is the maximum squared - minimum squared
        if math.sqrt((max(x, y) ** 2) - (min(x, y) ** 2)).is_integer():
            return math.sqrt((max(x, y) ** 2) - (min(x, y) ** 2))
        # otherwise, it's not a triple
        return "not a valid triple"
    
# test cases
print(check_triple(123, 1, 123667))
print(check_triple(5, 12, 13))
print(randTriple("aaron"))
print(find(8, 17))
