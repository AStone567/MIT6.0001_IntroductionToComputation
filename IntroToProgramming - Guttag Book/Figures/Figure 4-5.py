#Figure 4.5 - Iterative and recursive implementations of factorial

#Iterative
def facI(n):
    """Assumes n is an int > 0
    Returns n!"""
    result = 1
    while n > 1:
        result = result * n
        n -=1
    return result
print(facI(5))

#Recrusive
def facR(n):
    """Assumes n is an int >0
    Returns n!"""
    if n == 1:
        return n
    else:
        return n*facR(n-1)
print(facR(5))