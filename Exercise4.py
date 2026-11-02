# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apples","bananas","pears","grape"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruits)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count  >= 1:
    print(count)
    count -= 1
    

    

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for num in range(1,11):
    square_numbers = num ** 2
    print(square_numbers)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["blue","red","yellow","black","green","pink","orange"]
# TODO: Use a for loop to select and print 3 random colors from the list
random_colours = random.sample(colours, 3)
for colours in random_colours:
    print(colours)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print("Addition:", math_operations.add(5, 3))       # 8
print("Subtract:", math_operations.subtract(5, 3))  # 2
print("multiply:", math_operations.multiply(5, 3))  # 15
print("divide:", math_operations.divide(5, 3))    # 1.666...

# TODO: Use a while loop to create a simple calculator
def calculator():
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error: Division by zero":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input. please try again.")