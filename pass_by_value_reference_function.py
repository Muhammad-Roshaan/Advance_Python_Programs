# -=-=-=-=-==-=28-March-2024 (Thursday)-=-=-=-=-=-=-=-
# -=-=-=-=-=Pass by value / pass by Reference Global and local scopes Class Tasks

# -=-=-=Q1
# Write a Python function that takes an integer as input and doubles its value inside the
# function. Call this function with an integer variable as an argument and print the original and
# updated values of the variable before and after the function call.
def double_value(num):
    return num*2

user_input = int(input("enter any integer number:"))

print(f"Before calling function with value: {user_input}\n ")
print("When calling function the value is:", double_value(user_input))
print(f"\nAfter calling function with value: {user_input}\n")

# -=-=-=Q2
# Write a Python function that takes a list as input and appends an element to the list inside the
# function. Call this function with a list variable as an argument and print the original and
# updated values of the list before and after the function call.
my_list = []
for i in range(3):
    my_list.append(int(input("Enter any integer:")))


def append_element(lst, elem):
    lst.append(elem)
    return lst


element = int(input("Enter any element for add in list:"))
print("\n Before calling function with list: ",
      my_list, "\n and Element is:", element)
print("When calling function the list is:",
      append_element(my_list, element), "\n")
print("After calling function with list: \n", my_list)

# -=-=-=Q3
# Write a Python program that demonstrates the difference between pass by value and pass by
# reference. This could involve creating a function that modifies a variable passed by value and
# another function that modifies a variable passed by reference. Call both functions with
# appropriate variables and observe the changes.
# Function Pass By Value


def change_val(a):
    a += 5


x = 7
change_val(x)
print('Value of x outside the function:', x)

# Function Pass By Reference


def change_ref(b):
    b.append(10)


y = [1, 2, 3]
change_ref(y)
print('\nValue of y outside the function:', y)

# -=-=-=Q4
#  Write a Python program that declares a variable outside a function and another variable
# inside the function with the same name. Inside the function, modify the variable. Print both
# variables before and after the function call to understand how variable scope affects pass by
# value and pass by reference.
# Declare a variable outside the function
x = 5


def modify_variable():
    global x  # Access the global variable inside the function
    print("Inside modify_variable function - Before modification:", x)
    x += 10
    print("Inside modify_variable function - After modification:", x)


print("Before calling modify_variable function:", x)

modify_variable()
print("After calling modify_variable function:", x)

# -=-=-=Q5
#  Write a Python program that declares a variable in the global scope and another variable with
# the same name inside a function. Attempt to access both variables from within the function.
# Print the values of both variables before and after the function call to observe the scope
# # differences.
# method 1


def func():
    var1 = "I am local"
    try:
        print("var1 (local) : ", var1)
        print("var2 (global) : ", var2)
    except NameError as e:
        print("Caught an exception!")
        print("The error is: %s" % e)


var2 = "I am global"
func()

# method 2
# Declare a variable in the global scope
x = 5


def access_variable():
    x = 10
    print("Inside access_variable function - Local x:", x)
    try:
        print("Inside access_variable function - Global x:",
              globals()['x'])  # Access the global variable x
    except KeyError:
        print("Global variable x is not accessible inside the function.")


# Print the value of the global variable x before calling the function
print("Before calling access_variable function - Global x:", x)

# Call the function to observe variable scope differences
access_variable()

# Print the value of the global variable x after calling the function
print("After calling access_variable function - Global x:", x)

# -=-=-=Q6
# Define a function `outer_function` that declares a variable `x` and another function
# `inner_function` inside it. The inner function should access the variable `x` from the enclosing
# scope and print its value. Call `outer_function` and then call `inner_function` to observe how
# the inner function can access variables from the enclosing scope.


def outer_function():
    x = 7

    def inner_function():
        print(f"Value of x from outer_function: {x}")
    return inner_function


func = outer_function()
func()

# -=-=-=Q7
# Write a Python program that defines a function `change_global_variable` which attempts to
# modify a global variable `count`. Declare the `count` variable outside the function. Inside the
# function, use the `global` keyword to modify the value of `count`. Print the value of `count`
# before and after calling the function to see the effect of the `global` keyword.


def change_global_variable():
    global count
    count += 5


count = 3
print("Before calling change_global_variable function - Global count: ", count)
change_global_variable()
print("After calling change_global_variable function - Global count: ", count)

# -=-=-=Q8
#  Define a function `outer_function` that declares a variable `x` and defines another function
# `inner_function` inside it. The inner function should modify the variable `x` from the enclosing
# scope using the `nonlocal` keyword. Print the value of `x` before and after calling the inner
# function to observe the effect of the `nonlocal` keyword .


def outer_function():
    x = 5  # Variable x in the outer function's scope

    def inner_function():
        nonlocal x  # Use the nonlocal keyword to modify x from the outer scope
        x += 10  # Modify x from the enclosing scope

    # Print x before calling inner_function
    print("Before calling inner_function - x:", x)
    inner_function()  # Call inner_function to modify x
    # Print x after calling inner_function
    print("After calling inner_function - x:", x)


# Call outer_function to observe the effect of nonlocal keyword
outer_function()
