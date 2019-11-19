# Finger Exercise 3.1 - Exhaustive Enumeration:
#Write a program that asks the user to enter an integer and prints two integers
#root and pwr
#such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user
#If no such pair of integres exist, it should print a message to that effect

#incrament the power value by the power up to a value (1,6)
#then if nothing is good, then you move to the next root value

inputInt = int(input('Please enter an integer '))
rootGuess = 0
powerGuess = 0
if inputInt > 0:
    while rootGuess ** powerGuess != inputInt:
        rootGuess += 1
        for guess in range(0,6):
            powerGuess = guess
            if rootGuess ** powerGuess == inputInt:
                break    
    print('Root = ', rootGuess)
    print('Power = ', powerGuess)
elif inputInt < 0:
    while rootGuess ** powerGuess != inputInt:
        rootGuess -= 1
        for guess in range(0,6):
            powerGuess = guess
            if rootGuess ** powerGuess == inputInt:
                break
    print('Root = ', rootGuess)
    print('Power = ', powerGuess)       
else:
    print('The value you entereed was 0, therefore:')
    print('Root = 0 ')
    print('Power = 0')
