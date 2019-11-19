#Finger excercise 3.5 - Newton-Raphson:

# Add some code to the implementation of Newton-raphson that keeps track of 
# the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of Newton-Raphson and bisection search.

#Newton-Raphson for square root
#Find x such that x**2 - 24 s within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
guessnum = 1
while abs(guess*guess-k) >= epsilon:
    print(guess)
    guess = guess - (((guess**2) - k)/(2*guess))
    guessnum += 1
print('Square root of ', k, 'is about', guess)
print('Number of guesses: ', guessnum)

