###Section 3- Comparison: equality operator
##  = is an assignment operator, e.g., a = b assigns a with the value of b;
##  == is the question are these values equal? so a == b compares a and b.
var = 0 
print(var == 0)
var = 1 
print(var == 0)
####Inequality: the not equal to operator (!=)
var = 0  
print(var != 0)
var = 1  
print(var != 0)
#Comparison operators: greater than >  less than<  
print(var >= 0)
print(var <= 0)
#Scenario
#Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
#Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.
print('Scenario')
n=55
print(n>=100)
n=99
print(n>=100)
n=100
print(n>=100)
n=101
print(n>=100)
n=-5
print(n>=100)
n=123
print(n>=100)
#3.1.7 Conditions and conditional execution
n=6
if n>=100:
    print('Soy verdadero')
else:
        print('Soy falso')
###nested
        

if n>=100:
    if n==100:
        print('Soy igual que 100')
    else:
        print('Soy mayor que 100 pero no igual')
else:
    if n==99:
        print('Soy falso por que soy 99')
    else:
        print('Soy falso por que soy menor que 99')
###elif keyword
n=100
if n>100:
    print('mayor que 100')
elif n==100:
    print('Soy igual que 100')
else:
    if n==99:
        print('Soy falso por que soy 99')
    else:
        print('Soy falso por que soy menor que 99')
####Inputs and comparison
        # Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)

#refactoriza

numero1= int(input('Dame el primero:'))
numero2= int(input('Dame el segundo:'))
numero3= int(input('Dame el tercero:'))
mayornumero=0
if numero1>numero2: 
    if numero1>numero3: mayornumero=numero1
    else: mayornumero=numero3
elif numero2>numero3: mayornumero=numero2
else: mayornumero=numero3
print(mayornumero)

###otra forma de asignar variables
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)

###strings and intigers
x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")






