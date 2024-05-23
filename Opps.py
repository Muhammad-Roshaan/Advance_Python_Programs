# #                                                     Class/Objects:
# Q1.Bank Account Management System:Create a Python class representing a bank account. Include methods for deposit,
#  withdrawal, and displaying the balance.

# ATM System
# class Bank_Account:
#     def __init__(self, password, name, balance=1000):
#         self.password = password
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount Deposited:", amount)

#     def withdrawal(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Amount Withdrawn:", amount)
#         else:
#             print("Insufficient balance!")

#     def display_balance(self):
#         print("Current Balance:", self.balance)

# account = Bank_Account("password123", "John Doe")
# account.deposit(1000)
# account.withdrawal(1200)
# account.display_balance()


# # Q2. Library Catalog:Design a class for a library catalog. Include methods for adding books,
# # searching for books by title or author, and displaying available books.

# class Library_Catalog:
#     def __init__(self):
#         self.books = [
#             ['Hobit'],
#             ['Harry Porter'],
#             ['To Kill a Mockingbird'],
#             ['The Book Thief']
#             ]
    
#     def add_book(self, book_title):
#         self.books.append(book_title)

#     def display_books(self):
#         if self.books:
#             print("Library Books:")
#             for book in self.books:
#                 print(book)
#         else:
#             print("No books in the library catalog.")
# print('')
# library = Library_Catalog()
# library.display_books()
# library.add_book("1984")


# # Q3.Student Management System:Build a class to represent a student. Include attributes such as name, age,
# # and grade. Implement methods for adding/removing courses, calculating GPA, and displaying student information.

# class College_Management:
#     def __init__(self, student_names, age, grade, courses):
#         self.student_names = [student_names] 
#         self.age = age
#         self.grade = grade
#         self.courses = courses
    
#     def display_available_courses(self):
#         course_categories = {
#             "Science": ["Physics", "Chemistry", "Biology"],
#             "Math": ["Algebra", "Calculus", "Geometry"]
#         }
        
#         print("Available courses:")
#         for category, course_list in course_categories.items():
#             print(f"{category}: {', '.join(course_list)}")

# print('')
# college = College_Management("John", 20, "A", ["Math", "Science"])
# college.display_available_courses()

# Q5. Social Media Profile:Design a class for a social media profile. Include attributes like username,
# bio, and followers. Implement methods for posting updates,
# following/unfollowing other users, and displaying profile information.


# class S_Media_Profile:
#     def __init__(self, username, bio, followers=1000):
#         self.username = username
#         self.bio = bio
#         self.followers = followers
#         self.following = []  

#     def post_update(self, update):
#         print(f"{self.username} Posted: {update}")

#     def follow(self, other_user):
#         self.following.append(other_user.username)
#         other_user.followers += 1
#         print(f"{self.username} is now following {other_user.username}")

#     def unfollow(self, other_user):
#         if other_user.username in self.following:
#             self.following.remove(other_user.username)
#             other_user.followers -= 1
#             print(f"{self.username} unfollowed {other_user.username}")
#         else:
#             print(f"{self.username} is not following {other_user.username}")

#     def display_info(self):
#         print(f"Username: {self.username}")
#         print(f"Bio: {self.bio}")
#         print(f"Followers: {self.followers}")
#         print(f"Following: {', '.join(self.following)}")

# user1 = S_Media_Profile("Umer", "I code")
# user2 = S_Media_Profile("Ahmed", "Foodies")

# user1.post_update("Hello world!")
# user2.follow(user1)
# user1.display_info()
# user2.display_info()

# Q6. Vehicle Hierarchy :# Design a class hierarchy for vehicles, with a base class `Vehicle`
# representing common attributes and behaviors such as `make`, `model`,
# `year`, and `fuel_type`. Subclasses `Car`, `Truck`, and `Motorcycle`
# should inherit from `Vehicle` and extend it with specific attributes such as
# `num_doors`, `bed_length`, and `engine_size`. Each subclass should also
# implement methods such as `start_engine`, `stop_engine`, and
# `accelerate` tailored to the vehicle type

class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.engine_running = False
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            print("Engine started.")
        else:
            print("Engine is already running.")
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            print("Engine stopped.")
        else:
            print("Engine is already stopped.")
    
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, num_doors):
        super().__init__(make, model, year, fuel_type)
        self.num_doors = num_doors
    
    def accelerate(self):
        print("Car is accelerating.")


class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type, bed_length):
        super().__init__(make, model, year, fuel_type)
        self.bed_length = bed_length
    
    def accelerate(self):
        print("Truck is accelerating.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_type, engine_size):
        super().__init__(make, model, year, fuel_type)
        self.engine_size = engine_size
    
    def accelerate(self):
        print("Motorcycle is accelerating.")

car = Car("Toyota", "Cam", 2022, "Gas", 4)
car.start_engine()
car.accelerate()
car.stop_engine()

truck = Truck("Mustang", "G-25", 2023, "Diesel", "Fast")
truck.start_engine()
truck.accelerate()
truck.stop_engine()

motorcycle = Motorcycle("Accord", "Reborn", 2021, "Petrole", "1000cc")
motorcycle.start_engine()
motorcycle.accelerate()
motorcycle.stop_engine()



