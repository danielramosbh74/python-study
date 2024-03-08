# Basic structures

# Function easiest model
def sum(a, b):
    return a + b
    OR
    # c = a + b
    # return c

# Test values running the program easiest model
# Very useful to test step by step nested functions, if sentences, for and while loops

a_argument = int(input('Type "a": '))
b_argument = int(input('Type "b": '))

print("Sum of a and b = ", sum (a_argument, b_argument))

# OR just simulating fixed arguments direct:

print ( "Sum of 2 and 3 = ", sum (2, 3) )



for i in range (0,2):
    print (i)
print()
print(i)

print()

for i in [0, 1, 2]:
    print (i)
print()
print(i)

print()

x = ['123', '456', '789']
values = []
for val in x:
    values.append(int(val))
    print(values)

print()

i = 0
while i < 3:
    print(i)
    i = i + 1
print()
print(i)


age = int(input("Type age: "))
# age = 50

if (age < 50):
    print ("Age < 50: ", age)
elif (age > 50):
    print ("age > 50: ", age)
else:
    print ("age = 50: ", age)
