#Finger Excercise 4.1.1 - Function Definitions

#Write a function 'isin' that accepts two strings as arguments and returns True if either string
#occurs anywhere in the other, and False otherwise. 
#Hint: you might want to use the built-in str operation in

a = 'book'
b= 'bookkeeper'

def isIn(x:str,y:str):
    if len(a) > len(b): #a is the larger string
        if b in a:
            return True
        else:
            return False
    if len(a) < len(b): #b is the larger string
        if  a in b:
            return True
        else:
            return False
    else:
        if a == b: #equal length
            return True
        else:
            return False
    

print(isIn(a,b))

#does this work?