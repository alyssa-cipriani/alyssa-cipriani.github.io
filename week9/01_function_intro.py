
# Example Function
def sayHello():
    '''A function that print out "Hello World"'''
    print ("Hello World")
# End of sayHello() function

sayHello()

def sayHelloTo(name : str):
    '''Function that says hello tot he input string '''
    print("Hello %s" % name)

sayHelloTo("Alyssa")
sayHelloTo("Sally")

name = "John"
sayHelloTo("raj")
print(name) # Will not impact the function

def sayHelloGreeting(greeting :str, name: str):
    '''A function that outputs a greeting customized for the name.'''
    print("%s %s!" % (greeting,name))

# use the function
sayHelloGreeting("Good Morning", "John")
sayHelloGreeting("Good Afternoon", "Class")

# example 4

def addTwoNumbers(num1,num2):
    '''A function that adds two numbers together.'''
    return num1 + num2 


x = 4 
y = 5 
sum = addTwoNumbers(x,y)
print (" %i + %i = %i" % (x,y,sum))

# example 5 - Passing Parameters by Value

def calculateNewSalary(salary: float, percentageRaise: float):
    '''A function yo calculator an employees new salary with the given percentage
    raise'''
    NewSalary = salary * (1 + percentageRaise)
    salary = 0 
    return NewSalary

# call the function 
mySalary = 50000.0
myRaise = 0.05 

print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
newAmount = calculateNewSalar(mySalary,myRaise)
print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
print("My new salary is: $%.2f" % newAmount)

# example of returning MORE THAN 1 THING 
# python only 

def addAndSubtract(a: int, b: int):
    '''Function that returns both the sum and the difference between 2 numbers.'''
    add = a + b 
    subtract = a - b 
    return add, subtract 

# calling the function 
sum,diff = addAndSubtract(10,5)
print("Sum: %d, Diff: %d" % (sum,diff))