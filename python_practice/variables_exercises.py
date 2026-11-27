"""
============================================
PYTHON VARIABLES - PRACTICE EXERCISES
============================================
Complete each exercise by filling in the blanks or writing code.
Run this file to check your answers!

Topics Covered:
- Variable creation and assignment
- Naming conventions
- Data types
- Variable scope (local, global)
- Constants

Instructions:
1. Read each exercise carefully
2. Write your code where it says "YOUR CODE HERE"
3. Run the file to check your answers
4. Solutions are at the bottom (don't peek!)

============================================
"""

print("=" * 50)
print("  PYTHON VARIABLES - PRACTICE EXERCISES")
print("=" * 50)
print()

# ============================================
# LEVEL 1: BEGINNER - Variable Basics
# ============================================

print("LEVEL 1: BEGINNER")
print("-" * 50)

# Exercise 1.1: Create Variables
# Create variables to store the following information:
# - Your name (string)
# - Your age (integer)
# - Your height in meters (float)
# - Whether you are a student (boolean)

print("\n📝 Exercise 1.1: Create Variables")

# YOUR CODE HERE (uncomment and fill in)
# my_name = ___
# my_age = ___
# my_height = ___
# is_student = ___

# Uncomment below to test your answer:
# print(f"Name: {my_name}, Age: {my_age}, Height: {my_height}m, Student: {is_student}")


# ----------------------------------------

# Exercise 1.2: Variable Reassignment
# Start with x = 10, then change it to 20, then to "hello"

print("\n📝 Exercise 1.2: Variable Reassignment")

# YOUR CODE HERE
# x = ___
# print(f"x is now: {x}, type: {type(x)}")
# x = ___
# print(f"x is now: {x}, type: {type(x)}")
# x = ___
# print(f"x is now: {x}, type: {type(x)}")


# ----------------------------------------

# Exercise 1.3: Multiple Assignment
# Create three variables a, b, c with values 1, 2, 3 in ONE line

print("\n📝 Exercise 1.3: Multiple Assignment")

# YOUR CODE HERE
# ___, ___, ___ = ___, ___, ___
# print(f"a={a}, b={b}, c={c}")


# ----------------------------------------

# Exercise 1.4: Swap Variables
# Swap the values of x and y WITHOUT using a third variable

print("\n📝 Exercise 1.4: Swap Variables")

x = 100
y = 200
print(f"Before swap: x={x}, y={y}")

# YOUR CODE HERE - swap x and y
# Hint: Python has a clever way to do this in one line!


print(f"After swap: x={x}, y={y}")  # Should print x=200, y=100


# ============================================
# LEVEL 2: INTERMEDIATE - Naming Conventions
# ============================================

print("\n" + "=" * 50)
print("LEVEL 2: INTERMEDIATE")
print("-" * 50)

# Exercise 2.1: Fix the Variable Names
# The following variable names are BAD. Fix them using proper conventions.

print("\n📝 Exercise 2.1: Fix Variable Names")

# BAD names - Fix these:
# 1st_name = "John"           # Fix this
# user-age = 25               # Fix this  
# TOTALAMOUNT = 1500.50       # Fix this (it's not a constant)
# MyEmail = "test@email.com"  # Fix this (not a class)
# class = "Python 101"        # Fix this (reserved keyword!)

# YOUR CODE HERE - Create properly named variables:
# ___ = "John"
# ___ = 25
# ___ = 1500.50
# ___ = "test@email.com"
# ___ = "Python 101"


# ----------------------------------------

# Exercise 2.2: Create Proper Constants
# Create constants for:
# - Maximum login attempts (3)
# - API base URL ("https://api.example.com")
# - Pi value (3.14159)

print("\n📝 Exercise 2.2: Create Constants")

# YOUR CODE HERE (use SCREAMING_SNAKE_CASE)
# ___ = 3
# ___ = "https://api.example.com"
# ___ = 3.14159


# ----------------------------------------

# Exercise 2.3: Boolean Naming
# Create boolean variables with proper naming (use is_, has_, can_ prefix)
# - User is logged in: True
# - User has admin rights: False
# - User can edit posts: True

print("\n📝 Exercise 2.3: Boolean Naming")

# YOUR CODE HERE
# ___ = True      # is logged in
# ___ = False     # has admin rights
# ___ = True      # can edit posts


# ============================================
# LEVEL 3: ADVANCED - Variable Scope
# ============================================

print("\n" + "=" * 50)
print("LEVEL 3: ADVANCED - Scope")
print("-" * 50)

# Exercise 3.1: Identify the Scope
# Look at this code and predict the output WITHOUT running it

print("\n📝 Exercise 3.1: Predict the Output")

"""
message = "Global Hello"

def greet():
    message = "Local Hello"
    print(message)

greet()
print(message)

# What will be printed?
# Line 1: _______________
# Line 2: _______________
"""


# ----------------------------------------

# Exercise 3.2: Fix the Global Variable Bug
# This code has a bug. Fix it so the counter increments properly.

print("\n📝 Exercise 3.2: Fix the Bug")

counter = 0

def increment_counter():
    # YOUR CODE HERE - Add something to fix this function
    counter = counter + 1
    print(f"Counter is now: {counter}")

# Uncomment to test (will error until fixed):
# increment_counter()
# increment_counter()
# increment_counter()
# print(f"Final counter: {counter}")  # Should be 3


# ----------------------------------------

# Exercise 3.3: Local vs Global
# Complete this function to:
# 1. Read the global discount_rate
# 2. Use a local variable for calculations
# 3. Return the discounted price

print("\n📝 Exercise 3.3: Calculate Discount")

DISCOUNT_RATE = 0.15  # 15% discount (global constant)

def calculate_discounted_price(original_price):
    # YOUR CODE HERE
    # Create a local variable 'discount_amount'
    # Create a local variable 'final_price'
    # Return the final_price
    pass

# Test:
# result = calculate_discounted_price(100)
# print(f"Original: $100, After 15% discount: ${result}")  # Should be $85.0


# ----------------------------------------

# Exercise 3.4: Counter with Scope
# Create a function that tracks how many times it's been called
# using a global variable

print("\n📝 Exercise 3.4: Call Counter")

call_count = 0

def tracked_function():
    # YOUR CODE HERE
    # Increment call_count each time this function runs
    # Print "Function called X times"
    pass

# Test:
# tracked_function()  # Function called 1 times
# tracked_function()  # Function called 2 times
# tracked_function()  # Function called 3 times


# ============================================
# LEVEL 4: CHALLENGE - Put It All Together
# ============================================

print("\n" + "=" * 50)
print("LEVEL 4: CHALLENGE")
print("-" * 50)

# Exercise 4.1: Bank Account Simulator
# Create a simple bank account with these features:
# - Global: MINIMUM_BALANCE = 100 (constant)
# - Global: account_balance = 1000 (starting balance)
# - Function: deposit(amount) - adds money, prints new balance
# - Function: withdraw(amount) - removes money if balance stays >= MINIMUM_BALANCE
# - Function: check_balance() - returns current balance

print("\n📝 Exercise 4.1: Bank Account")

# YOUR CODE HERE - Define the constants and variables


# YOUR CODE HERE - Define the functions


# Test your code:
# check_balance()          # Balance: $1000
# deposit(500)             # Deposited $500. New balance: $1500
# withdraw(200)            # Withdrew $200. New balance: $1300
# withdraw(1500)           # Cannot withdraw. Minimum balance is $100
# check_balance()          # Balance: $1300


# ----------------------------------------

# Exercise 4.2: Temperature Tracker
# Create functions to track temperatures and calculate statistics
# - Global list to store temperatures
# - Function to add a temperature
# - Function to get average temperature
# - Function to get min and max temperatures
# - Function to clear all temperatures

print("\n📝 Exercise 4.2: Temperature Tracker")

# YOUR CODE HERE


# Test:
# add_temperature(72)
# add_temperature(68)
# add_temperature(75)
# add_temperature(70)
# print(f"Average: {get_average()}")      # Average: 71.25
# print(f"Range: {get_min()} - {get_max()}")  # Range: 68 - 75
# clear_temperatures()


# ============================================
# BONUS: Quick Quiz
# ============================================

print("\n" + "=" * 50)
print("BONUS: QUICK QUIZ")
print("-" * 50)

print("""
Answer these questions (True/False):

1. Variable names can start with a number.
   Your answer: ___

2. Python variables must be declared with a type.
   Your answer: ___

3. 'my_var' and 'My_Var' are the same variable.
   Your answer: ___

4. Constants in Python should use SCREAMING_SNAKE_CASE.
   Your answer: ___

5. A local variable can be accessed outside its function.
   Your answer: ___

6. The 'global' keyword is needed to READ a global variable inside a function.
   Your answer: ___

7. The 'global' keyword is needed to MODIFY a global variable inside a function.
   Your answer: ___
""")


# ============================================
# SOLUTIONS (Don't peek until you've tried!)
# ============================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)
print("Scroll down to see solutions...")
print("." * 50)
print("." * 50)
print("." * 50)
print("." * 50)
print("." * 50)

"""
============================================
SOLUTIONS
============================================

# ----- Exercise 1.1 -----
my_name = "John"
my_age = 25
my_height = 1.75
is_student = True


# ----- Exercise 1.2 -----
x = 10
print(f"x is now: {x}, type: {type(x)}")
x = 20
print(f"x is now: {x}, type: {type(x)}")
x = "hello"
print(f"x is now: {x}, type: {type(x)}")


# ----- Exercise 1.3 -----
a, b, c = 1, 2, 3


# ----- Exercise 1.4 -----
x, y = y, x


# ----- Exercise 2.1 -----
first_name = "John"
user_age = 25
total_amount = 1500.50
my_email = "test@email.com"
course_name = "Python 101"


# ----- Exercise 2.2 -----
MAX_LOGIN_ATTEMPTS = 3
API_BASE_URL = "https://api.example.com"
PI = 3.14159


# ----- Exercise 2.3 -----
is_logged_in = True
has_admin_rights = False
can_edit_posts = True


# ----- Exercise 3.1 -----
# Line 1: "Local Hello"   (function's local variable)
# Line 2: "Global Hello"  (global variable unchanged)


# ----- Exercise 3.2 -----
counter = 0

def increment_counter():
    global counter           # <-- This was missing!
    counter = counter + 1
    print(f"Counter is now: {counter}")


# ----- Exercise 3.3 -----
DISCOUNT_RATE = 0.15

def calculate_discounted_price(original_price):
    discount_amount = original_price * DISCOUNT_RATE  # local
    final_price = original_price - discount_amount    # local
    return final_price


# ----- Exercise 3.4 -----
call_count = 0

def tracked_function():
    global call_count
    call_count += 1
    print(f"Function called {call_count} times")


# ----- Exercise 4.1 -----
MINIMUM_BALANCE = 100
account_balance = 1000

def deposit(amount):
    global account_balance
    account_balance += amount
    print(f"Deposited ${amount}. New balance: ${account_balance}")

def withdraw(amount):
    global account_balance
    if account_balance - amount >= MINIMUM_BALANCE:
        account_balance -= amount
        print(f"Withdrew ${amount}. New balance: ${account_balance}")
    else:
        print(f"Cannot withdraw. Minimum balance is ${MINIMUM_BALANCE}")

def check_balance():
    print(f"Balance: ${account_balance}")


# ----- Exercise 4.2 -----
temperatures = []

def add_temperature(temp):
    temperatures.append(temp)
    print(f"Added {temp}°F")

def get_average():
    if temperatures:
        return sum(temperatures) / len(temperatures)
    return 0

def get_min():
    return min(temperatures) if temperatures else 0

def get_max():
    return max(temperatures) if temperatures else 0

def clear_temperatures():
    global temperatures
    temperatures = []
    print("Temperatures cleared!")


# ----- Bonus Quiz Answers -----
# 1. False - Cannot start with number
# 2. False - Python is dynamically typed
# 3. False - Python is case-sensitive
# 4. True  - Convention for constants
# 5. False - Local variables only exist inside their function
# 6. False - You can READ without 'global'
# 7. True  - You need 'global' to MODIFY

"""

print("\n✅ Exercises file created!")
print("Open the file, uncomment the code, and start practicing!")
