#Figure 3.4 - Using bisection search to approximate square root

x = 24
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1,0, x)
ans = (high+low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans **2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)

#Finger Excercise:
#What would the code in Figure 3.4 do if the statement x = 25 were replaced by x = -25
#It would keep trying replacing the high with the ans because ans^2 is always greater than the negative value
#Iteration 1 - high = 25
#Iteration 1 - high = 12.5
#Iteration 1 - high = 6.25
#etc..

#the issue is that the low value will never change. Because ans**2 is never less than x
