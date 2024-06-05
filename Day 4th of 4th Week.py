# Day 1 Was Quiz
# Day 2 Was Revision
# Day 3 Was Tuple Revision

#                Advance Python Programming & Application
#                               Tuple programs
#                                  Practices

#     *************** Tuple Manipulation***************

# Q1. Write a function to create a tuple from user input.
# def input_Tuple():
#     user_input = input("Enter A Tuple: ")
#     return tuple(user_input.split())
#
# print(input_Tuple())
# ******** End ********

# Q2. Write a function to add an element to an existing tuple and return the new tuple.
# x=("Apple", "Banana","Peach","Mango")
# def input_Tuple2():
#     user_input2 = input("Enter A Fruit: ").split()
#     return (x+tuple(user_input2))
#
# print(input_Tuple2())
# ******** End ********

# Q3. Write a function to remove an element from a tuple and return the new tuple.

# x= (1,2,3,4)
# print('Old Tuple',x)
# def rmv_tup():
#     e_t_r = x[:3]
#     return e_t_r
# print('New Tuple',rmv_tup())
# ******** End ********

# Q4. Write a function to concatenate two tuples and return the result.
# con=input('\nEnter 1st Tuple:' ).split()
# catenate=input('\nEnter 2nd Tuple:' ).split()
# def concatenate():
#     con_contenate =tuple(con)+tuple(catenate)
#     return con_contenate
# print(concatenate())
# ******** End ********

# Q5. Write a function to find the length of a tuple.
# Tup_Length=input('\nEnter Tuple to check length:' ).split()
# def tuple_length():
#     Length=len(Tup_Length)
#     return Length
# print(tuple_length())
# ******** End ********

#     *************** Tuple Operations ***************

# Q1. Write a function to find the maximum and minimum elements of a tuple.
# Tup_Max_Min=input('\nEnter Tuple to check Max And Min:' ).split()
# def tuple_Max_Min():
#     Max_Min=max(Tup_Max_Min) , min(Tup_Max_Min)
#     return Max_Min
# print(tuple_Max_Min())
# ******** End ********

# Q2. Write a function to check if an element exists in a tuple.

# original_tuple = tuple(input('\nEnter Tuple: ').split())
# def element_exists_in_tuple(tup, element):
#     return element in tup
# element_to_check = input('\nEnter Element To Check If it Exists In Tuple: ')
# if element_exists_in_tuple(original_tuple, element_to_check):
#     print("\nThe element exists in the tuple.")
# else:
#     print("\nThe element does not exist in the tuple.")
# ******** End ********

# Q3. Write a function to count the occurrences of an element in a tuple.

og_tuple = tuple(input('\nEnter Tuple: ').split())
def count_occurrences_in_tuple(tup, element):
    return tup.count(element)

ele_to_cnt = input("\nInput to check occurrence: ")
occurrences = count_occurrences_in_tuple(og_tuple, ele_to_cnt)
print(f"\nThe element {ele_to_cnt} occurs {occurrences} times in the tuple.")

print(type(og_tuple))
# ******** End ********

# Q4. Write a function to reverse a tuple.
# def rev_tuple():
#     re_tuple = tuple(input('\nEnter Tuple: ').split())
#     re_tuple2 = tuple(reversed(re_tuple))
#     return re_tuple2
#
# print(rev_tuple())
# ******** End ********

# Q5. Write a function to sort a tuple.
# def sort_tuple():
#     sor_tuple = tuple(input('\nEnter Tuple: ').split())
#     sor_tuple2 = tuple(sorted(sor_tuple))
#     return sor_tuple2
# print(sort_tuple())
# ******** End ********

# ************  Tuple Unpacking  ***********

# Q1. Write a function to unpack a tuple into individual variables.
# def unpack_tuple(tup):
#     return tup
# my_tuple = tuple(input('Enter any 3 Var: ').split())
# var1, var2, var3 = unpack_tuple(my_tuple)
# print("Variable 1st:", var1)
# print("Variable 2nd:", var2)
# print("Variable 3rd:", var3)
# ******** End ********

# Q2. Write a function to zip two tuples and return a list of tuples.
# def zip_tuple():
#     st_tup = tuple(input('\nEnter 1st Tuple: ').split())
#     nd_tup = tuple(input('\nEnter 2nd Tuple: ').split())
#     x = zip(st_tup, nd_tup)
#     return x
# print(list(zip_tuple()))
# ******** End ********

# ************* Tuple Slicing **************
# Q1. - Write a function to slice a tuple based on start and end indices.
# def slice_tuple(tup, first, last):
#     return tup[first:last]
# original_tuple = (1, 2, 3, 4, 5)
# start_index = 1
# end_index = 4
# sliced_tuple = slice_tuple(original_tuple, start_index, end_index)
# print("Sliced Tuple:", sliced_tuple)
# ******** End ********

# Q2. Write a function to return the first n elements of a tuple.
# def fst_n_elements(tup, n):
#     return tup[:n]
#
# original_tuple = (1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15)
# n = int(input('\nEnter A Value to Return: '))
# result = fst_n_elements(original_tuple, n)
# print("\nFirst", n, "elements of the tuple:", result)
# ******** End ********

# ***********  Tuple Iteration  ***********

# Q1. Write a function to iterate over a tuple and print its elements.
# def pnt_tuple_ele(tup):
#     for element in tup:
#         print(element)
# original_tuple = (50, 30, 83, 44, 777)
# print("\nPrinting all the elements:")
# pnt_tuple_ele(original_tuple)

# ******** End ********
# Q2. Write a function to find the index of a specific element in a tuple.
# def fnd_ele_index(tuple, element):
#     return tuple.index(element)
# original_tuple = (50, 30, 83, 44, 777)
# ele_to_find = 777
# try:
#     index = fnd_ele_index(original_tuple, ele_to_find)
#     print(f"\nThe index is: {index}")
# except ValueError:
#     print(f"\nThe element is not found in the tuple.")
# ******** End ********

# *********** Tuple Packing/Unpacking ***********
# Q1. Write a function to pack and return multiple values as a tuple.
# def pk_values():
#     V1 = input("Enter 1st Value: ").split()
#     V2 = input("Enter 2nd Value: ").split()
#     V3 = input("Enter 3rd Value: ").split()
#     return V1, V2, V3
# result = pk_values()
# print("Pack values:", result)
# ******** End ********
# Q2. Write a function to unpack a tuple returned by another function.
# def return_tuple():
#     return 'Apple', 3.14, [781, 48484]
# def unpack_tuple():
#     v1, v2, v3 = return_tuple()
#     print("Unpack values:")
#     print("Value 1:", v1)
#     print("Value 2:", v2)
#     print("Value 3:", v3)
# unpack_tuple()
# ******** End ********

# *************   Tuple Membership Testing   *************

# Q1. Write a function to test if a given tuple is a subset of another tuple.
# def Sub_Set(x, y):
#     x_set = set(x)
#     y_set = set(y)
#     return x_set.issubset(y_set)
# x = input("\nEnter 1st Tuple: ").split()
# y = input("\nEnter 2nd Tuple: ").split()
# print("\nIs 1st Tuple subset of 2nd?", Sub_Set(y, x))
# ******** End ********

# Q2. Write a function to test if all elements of a tuple satisfy a condition.
# def all_condition(tup, condition):
#     for element in tup:
#         if not condition(int(element)):
#             return False
#     return True
# def is_positive(x):
#     return x > 0
# original_tuple = input("\nEnter A Tuple (separated by spaces): ").split()
# print("\nDo all elements satisfy the condition?", all_condition(original_tuple, is_positive))
# ******** End ********
# Tuple Conversion:
# Q1. Write a function to convert a tuple to a list.
# def T_to_L():
#     y=input("\nEnter A Tuple (separated by spaces):").split()
#     x=list(y)
#     return x
# print(T_to_L())
# ******** End ********
# Q2. Write a function to convert a list to a tuple.
# def T_to_L():
#     y=input("\nEnter a list  (separated by spaces): ").split()
#     x=tuple(y)
#     return x
# print(T_to_L())
# ******** End ********