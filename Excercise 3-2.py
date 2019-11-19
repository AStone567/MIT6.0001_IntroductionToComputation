#Finger Excercise 3.2 - For Loops:
#Let s be a string that contains a sequence of decimal numbers seperated by commas
#e.g. s = '1.23,2.4,3.123'
#Write a program that brings the sum of the number in s


s = '1.23,2.4,3.123'

#First I need a way to identify the numbers

total = 0
charindex = 0 
start = 0
end = 0
length = len(s)

for number in s:
    if number == ",":
        end = charindex
        total += float(s[start:end])
        start = end + 1
    charindex += 1
    if charindex == length:
        end = charindex
        total += float(s[start:end])
print('The Total sum is:')
print(total)

#wafu option 1: Using lambda function
print(sum(map(lambda n: float(n), s.split(','))))

#wafu option 2: using list comprhension
print(sum([float(n) for n in s.split(',')]))

print(sum(map(float, s.split(','))))

#list comprehension but you assign it to a variable 
a = [float(n) for n in s.split(',')]
sum(a)

