# # import random

# # def get_choice():
# #     options = ["rock", "paper", "scissors"]
# #     player_choice = input("Enter (rock, paper, or scissors): ").lower()
# #     while player_choice not in options:
# #         print("Invalid choice. Please try again.")
# #         player_choice = input("Enter (rock, paper, or scissors): ").lower()
# #     computer_choice = random.choice(options)
# #     choice = {"player": player_choice, "computer": computer_choice};return choice

# # def check_win(player, computer):
# #     print(f"You chose {player}, Computer chose {computer}")
# #     if player == computer:
# #         return "It's a tie!"
# #     elif player == "paper":
# #         if computer == "rock":
# #             return "Paper covers rock! You win"
# #         else:
# #             return "Scissors cut paper! You lose."
# #     elif player == "rock":
# #         if computer == "scissors":
# #             return "Rock smashes scissors! You win"
# #         else:
# #             return "Paper covers rock! You lose."
# #     elif player == "scissors":
# #         if computer == "paper":
# #             return "Scissors cut paper! You win"
# #         else:
# #             return "Rock smashes scissors! You lose"

# # choices = get_choice()
# # result = check_win(choices["player"], choices["computer"])
# # print(result)


# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # name= 1.;print(isinstance(name,float))

# # input_age=input("\nEnter Your Age: ");age=int(input_age);print(f"\nYou are {age} years old.")
# # birth_year=2024-age;print(f'\nYou were born in {birth_year}')
# # age+=age;print(f'\nYou will be {age} years old in 2048.')


# # Ternary Operator

# def is_adult(age):
#     return "\nAdult\n" if age >= 18 else "\nNot an Adult\n"

# age = int(input("Enter your age: "));result = is_adult(age);print(result)


# # ----------------------------------------------------------------------------------------
# # Books in library
# book1,book2 = "To Kill a Mockingbird","1984"

# library = [book1, book2];

# read = all([book1 in library, book2 in library]);print(read)

# # ----------------------------------------------------------------------------------------
# # Books to check
# book1 = "To Kill a Mockingbird"
# book2 = "1984"

# book3 = "Moby Dick" 
# book4 = "The Great Gatsby"

# library = [book1, book2]

# books_to_check = [book1,book2,book3, book4]

# not_in_library = [book for book in books_to_check if book not in library];print(not_in_library) 

# # ________________________________________________________________________________
# num=complex(2,3)
# print(num)
# print(type(num))

# from enum import Enum

# class State(Enum):
#     INACTIVE='Hi,There'
#     ACTIVE=1

# print(list(State))

# # Star Pattern
# condition = True
# x = ""
# while condition == True:
#     x+="*"
#     if len(x) >4:
#         condition = False
#     print(x)

# x = ""
# while len(x) < 10:
#     print(x)
#     x += '*'

# # inverted stars_____________
# x = ["*"] * 10 
# while x:
#     print("".join(x)) 
#     x.pop() 

# #Table of x________________________________________________________
# # condition = True  # Define the condition

# x = 0  # Initialize x

# while condition:
#     x += 1  # Increment x
#     print(f"{x}")  # Print the current value of x
    
#     # Termination condition to prevent an infinite loop (for example, stop after 10 iterations)
#     if x >= 10:
#         condition = False
 
# #  Classes__________________________________________________________
# class Animal:
#     def pets(self):
#         return "Woof!"

# class Dog(Animal):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         return print("Woof!")

# roger = Dog("Roger",4)
# print(roger.name)
# print(roger.age)

# roger.bark()
# print(roger.pets())

import sys 

# List all attributes and methods of the sys module
attributes = dir(sys)
print(attributes)









