# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

import string

def conversion_numb(String):
    try:
        if '.' in string:
            return float(string)
        else:
            return int(string)
    except ValueError:
            return False
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m, b, lower_x, upper_x):
    if not (isinstance(lower_x, int) and isinstance(upper_x, int)) or lower_x > upper_x:
        return False
    return [m * x + b for x in range(lower_x, upper_x + 1)]

import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    return x1, x2


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    user_input = input("Enter 'm', 'b', 'lower_x', 'upper_x' separate by space(/ type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    m, b, lower_x, upper_x = user_input.split()

    m = conversion_numb(m)
    b = conversion_numb(b)
    lower_x = conversion_numb(lower_x)
    upper_x = conversion_numb(upper_x)
    
    if m is False or b is False or lower_x is False or upper_x is False:
        print("It's not valid input. Please enter valid numbers.")
        continue
    result = slope_intercept(m, b, lower_x, upper_x)
    print("Results y values:", result)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
while True:
    users_input = input("Enter 'a', 'b', 'c' separate by spaces (/ type 'exit' to quit): ")
    if users_input.lower() == 'exit':
        break
    
    a, b, c = users_input.split()
    a = conversion_numb(a)
    b = conversion_numb(b)
    c = conversion_numb(c)
    
    if a is False or b is False or c is False:
        print("Invalid input. Please enter valid numbers.")
        continue
    
    result = quadratic_formula(a, b, c)
    print("Quadratic formula result:", result)
