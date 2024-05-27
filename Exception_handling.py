# -=-=-==-==========-=-=----Exceptional Handling Class Tasks
# -=-=-=-=- 25-March-2024 (Monday)

# -=-=-=-=-Task 1: Division with Error Handling
# Write a function `divide (a, b) ` that takes two numbers as input and returns the
# result of dividing `a` by `b`. Handle any `ZeroDivisionError` exceptions by printing
# a suitable error message.
# a = input("Enter any number:")
# b = input("Enter another number:")


# def divide(a, b):
#     try:
#         return float(a)/float(b)
#     except ZeroDivisionError:
#         print("Error! Cannot divide by zero .")


# result = divide(a, b)
# print("Result is :", result)

# # -=-=-=-=Task 2: Type Conversion with Error Handling
# # Write a function `convert_to_int(string)` that takes a string as input and
# # converts it to an integer. Handle any `ValueError` exceptions that occur during the
# # conversion by printing an appropriate error message.


# def convert_to_int(string):
#     try:
#         return int(string)
#     except ValueError:
#         print("Error! Invalid Input.")


# user_input = input("Please enter a valid number: ")
# number = convert_to_int(user_input)
# print("Number you entered is : ", number)

# # -=-=-=-=Task 3: List Element Access with Error Handling
# # Write a function `get_element(lst, index)` that takes a list `lst` and an index
# # `index` as input and returns the element at the specified index. Handle any
# # `IndexError` exceptions by printing a message indicating that the index is out of
# # # range.


# def get_element(lst, index):
#     try:
#         if index in lst:
#             return lst.index(index)
#         else:
#             raise IndexError
#     except IndexError:
#         print("Index  is Out Of Range!")


# list = []
# for i in range(4):
#     input("enter element for index:")
#     list.append(i)
# print("List elements are: \n", list)
# selected_index = int(input("Enter the index you want to access: "))
# element = get_element(list, selected_index)
# print(element)

# # -==-=-=-Task 4: Dictionary Key Access with Error Handling
# # Write a function `get_value(dictionary, key)` that takes a dictionary `dictionary`
# # and a key `key` as input and returns the value associated with the key. Handle any
# # `KeyError` exceptions by printing a message indicating that the key is not present
# # in the dictionary.


# def get_value(dic, ky):
#     try:
#         return dic[ky]
#     except KeyError:
#         print("The given key is Not Present in the Dictionary!")


# my_dict = {}
# keys = ['name', 'age', 'country']
# values = ['John Doe', 25, 'USA']

# for i in range(len(keys)):
#     my_dict[keys[i]] = values[i]

# print("\nDictionary keys are:\n ", keys)
# print("Dictionary Values are:\n ", values)
# print("\nDictionary Elements:\n", my_dict)

# key = input("Enter the key you want to search: ")
# val = get_value(my_dict, key)
# if val != None:
#     print("Value of the entered key is :\n ", val)

# -=-=-=-=Task 5: Incorrect Function Definition
# Write a program with a function definition that should accept two parameters,
# but mistakenly doesn't. Introduce an `IndentationError` or `SyntaxError` by
# improperly defining the function. Handle this error by printing a message
# indicating the incorrect function definition.


def func_IndentationError_SyntaxError(a,b):
    print("This function has been defined incorrectly.")


try:
    func_IndentationError_SyntaxError()
except IndentationError:
    print("An IndentationError occurred. The function definition may be missing indents.")
except SyntaxError:
    print("A SyntaxError occurred. There may be an issue with the function definition itself.")
else:
    raise SyntaxError
