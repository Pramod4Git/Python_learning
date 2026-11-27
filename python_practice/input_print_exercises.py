"""
============================================
INPUT & PRINT - 40 PRACTICE EXERCISES
============================================
Focus: Taking user input and printing output

Topics Covered:
1. Basic print statements
2. Print formatting (f-strings, format())
3. Taking user input
4. Type conversion (int, float, str)
5. Multiple inputs
6. Formatted output

Difficulty:
  ⭐       = Very Easy
  ⭐⭐     = Easy
  ⭐⭐⭐   = Medium

============================================
"""

print("=" * 60)
print("  INPUT & PRINT EXERCISES")
print("=" * 60)

# ============================================
# PART 1: BASIC PRINT (Exercises 1-10)
# ============================================
print("\n📌 PART 1: BASIC PRINT")
print("-" * 60)

# ----- Exercise 1 ⭐ -----
# Print "Hello, Python!" on the screen
print("\n1. Basic Print ⭐")
# YOUR CODE HERE:



# ----- Exercise 2 ⭐ -----
# Print your name, favorite color, and hobby on three separate lines
print("\n2. Multiple Lines ⭐")
# YOUR CODE HERE:



# ----- Exercise 3 ⭐ -----
# Print this exact text with quotes: He said "Python is fun!"
# Hint: Use escape character \" or mix quote types
print("\n3. Print with Quotes ⭐")
# YOUR CODE HERE:



# ----- Exercise 4 ⭐ -----
# Print this path: C:\Users\Documents\file.txt
# Hint: Use escape character \\ or raw string r""
print("\n4. Print Path ⭐")
# YOUR CODE HERE:



# ----- Exercise 5 ⭐ -----
# Print a multi-line poem using triple quotes:
# Roses are red,
# Violets are blue,
# Python is awesome,
# And so are you!
print("\n5. Multi-line Text ⭐")
# YOUR CODE HERE:



# ----- Exercise 6 ⭐ -----
# Print numbers 1 to 5 on the SAME line with spaces
# Output: 1 2 3 4 5
# Hint: Use print(x, end=" ")
print("\n6. Same Line Print ⭐")
# YOUR CODE HERE:



# ----- Exercise 7 ⭐ -----
# Print a horizontal line of 50 dashes
# Output: --------------------------------------------------
print("\n7. Print Dashes ⭐")
# YOUR CODE HERE:



# ----- Exercise 8 ⭐ -----
# Print this box pattern:
# ********
# *      *
# *      *
# ********
print("\n8. Box Pattern ⭐")
# YOUR CODE HERE:



# ----- Exercise 9 ⭐ -----
# Print 3 blank lines, then "Hello"
print("\n9. Blank Lines ⭐")
# YOUR CODE HERE:



# ----- Exercise 10 ⭐⭐ -----
# Print this using tab (\t):
# Name        Age     City
# John        25      NYC
# Alice       30      LA
print("\n10. Tab Alignment ⭐⭐")
# YOUR CODE HERE:



# ============================================
# PART 2: PRINT WITH VARIABLES (Exercises 11-20)
# ============================================
print("\n" + "=" * 60)
print("📌 PART 2: PRINT WITH VARIABLES")
print("-" * 60)

# ----- Exercise 11 ⭐ -----
# Create variables: name="John", age=25
# Print: "My name is John and I am 25 years old."
# Use f-string
print("\n11. F-string Basic ⭐")
# YOUR CODE HERE:



# ----- Exercise 12 ⭐ -----
# Create variables: price=49.99, quantity=3
# Print: "Total: $149.97"
# Use f-string with calculation
print("\n12. F-string with Math ⭐")
# YOUR CODE HERE:



# ----- Exercise 13 ⭐⭐ -----
# Create variable: pi=3.14159265359
# Print pi with only 2 decimal places
# Output: "Pi = 3.14"
# Hint: Use {variable:.2f}
print("\n13. Decimal Formatting ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 14 ⭐⭐ -----
# Create variable: amount=1234567.89
# Print with comma separators
# Output: "Amount: 1,234,567.89"
# Hint: Use {variable:,.2f}
print("\n14. Comma Separators ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 15 ⭐⭐ -----
# Create variable: percentage=0.756
# Print as percentage: "Score: 75.60%"
# Hint: Use {variable:.2%}
print("\n15. Percentage Format ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 16 ⭐⭐ -----
# Create variable: number=42
# Print in different formats:
# Decimal: 42
# Binary: 101010
# Hexadecimal: 2a
# Octal: 52
print("\n16. Number Formats ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 17 ⭐⭐ -----
# Create variable: text="python"
# Print with 20 characters width, centered with *
# Output: *******python*******
# Hint: Use {variable:*^20}
print("\n17. Center Alignment ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 18 ⭐⭐ -----
# Create variables: item="Apple", price=1.50, qty=5
# Print a formatted receipt line:
# Apple          x5     $7.50
# Hint: Use width specifiers
print("\n18. Receipt Format ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 19 ⭐⭐ -----
# Using .format() method (not f-string)
# Create: name="Alice", score=95
# Print: "Student Alice scored 95 points"
print("\n19. Using .format() ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 20 ⭐⭐ -----
# Using % formatting (old style)
# Create: name="Bob", age=30
# Print: "Bob is 30 years old"
# Hint: "Name is %s and age is %d" % (name, age)
print("\n20. Using % Format ⭐⭐")
# YOUR CODE HERE:



# ============================================
# PART 3: BASIC INPUT (Exercises 21-30)
# ============================================
print("\n" + "=" * 60)
print("📌 PART 3: BASIC INPUT")
print("-" * 60)

# ----- Exercise 21 ⭐ -----
# Ask user for their name and print "Hello, [name]!"
print("\n21. Name Input ⭐")
# YOUR CODE HERE:
# name = input("Enter your name: ")
# print(...)



# ----- Exercise 22 ⭐ -----
# Ask user for their favorite food
# Print: "Wow, [food] is delicious!"
print("\n22. Food Input ⭐")
# YOUR CODE HERE:



# ----- Exercise 23 ⭐⭐ -----
# Ask user for their age (as integer)
# Print: "You were born in [year]"
# Calculate year = 2024 - age
print("\n23. Age to Birth Year ⭐⭐")
# YOUR CODE HERE:
# age = int(input("Enter your age: "))



# ----- Exercise 24 ⭐⭐ -----
# Ask user for a number (as integer)
# Print the number doubled and tripled
# Output:
# Double: 20
# Triple: 30
print("\n24. Double and Triple ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 25 ⭐⭐ -----
# Ask user for a decimal number (as float)
# Print rounded to 2 decimal places
print("\n25. Float Input ⭐⭐")
# YOUR CODE HERE:
# num = float(input("Enter a decimal number: "))



# ----- Exercise 26 ⭐⭐ -----
# Ask user for first name and last name separately
# Print full name in format: "Last, First"
print("\n26. First and Last Name ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 27 ⭐⭐ -----
# Ask user for three numbers
# Print their sum and average
print("\n27. Sum and Average ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 28 ⭐⭐ -----
# Ask user for length and width of a rectangle
# Print area and perimeter
# Area = length × width
# Perimeter = 2 × (length + width)
print("\n28. Rectangle Calculations ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 29 ⭐⭐ -----
# Ask user for hours worked and hourly rate
# Print total salary
print("\n29. Salary Calculator ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 30 ⭐⭐ -----
# Ask user for a number
# Print its square, cube, and square root
# Hint: Square root = number ** 0.5
print("\n30. Number Operations ⭐⭐")
# YOUR CODE HERE:



# ============================================
# PART 4: MULTIPLE INPUTS (Exercises 31-35)
# ============================================
print("\n" + "=" * 60)
print("📌 PART 4: MULTIPLE INPUTS")
print("-" * 60)

# ----- Exercise 31 ⭐⭐ -----
# Take 3 numbers in ONE input separated by spaces
# Print their sum
# Example input: 10 20 30
# Hint: Use input().split()
print("\n31. Three Numbers One Line ⭐⭐")
# YOUR CODE HERE:
# nums = input("Enter 3 numbers separated by spaces: ").split()
# Convert each to int



# ----- Exercise 32 ⭐⭐ -----
# Take name and age in ONE input separated by comma
# Input: John,25
# Print: "Name: John, Age: 25"
print("\n32. Name and Age ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 33 ⭐⭐⭐ -----
# Take 5 numbers in one line, print min and max
# Example input: 45 12 67 89 23
print("\n33. Min and Max ⭐⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 34 ⭐⭐⭐ -----
# Take date in format DD/MM/YYYY
# Print: "Day: DD, Month: MM, Year: YYYY"
# Input: 25/12/2024
print("\n34. Date Parsing ⭐⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 35 ⭐⭐⭐ -----
# Take multiple items separated by commas
# Print each item on a new line with numbering
# Input: apple,banana,orange
# Output:
# 1. apple
# 2. banana
# 3. orange
print("\n35. List Items ⭐⭐⭐")
# YOUR CODE HERE:



# ============================================
# PART 5: REAL-WORLD SCENARIOS (Exercises 36-40)
# ============================================
print("\n" + "=" * 60)
print("📌 PART 5: REAL-WORLD SCENARIOS")
print("-" * 60)

# ----- Exercise 36 ⭐⭐ -----
# Create a simple greeting card
# Ask: recipient name, sender name, message
# Print a formatted card:
# ╔════════════════════════════════╗
# ║     Dear [Recipient],          ║
# ║                                ║
# ║     [Message]                  ║
# ║                                ║
# ║     From: [Sender]             ║
# ╚════════════════════════════════╝
print("\n36. Greeting Card ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 37 ⭐⭐⭐ -----
# Simple Restaurant Bill
# Ask: item name, price, quantity, tip percentage
# Print formatted bill:
# ================================
#        RESTAURANT BILL
# ================================
# Item: Pizza
# Price: $15.99
# Quantity: 2
# --------------------------------
# Subtotal: $31.98
# Tip (15%): $4.80
# --------------------------------
# TOTAL: $36.78
# ================================
print("\n37. Restaurant Bill ⭐⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 38 ⭐⭐ -----
# Student ID Card
# Ask: name, student ID, department, year
# Print formatted ID card
print("\n38. Student ID Card ⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 39 ⭐⭐⭐ -----
# Temperature Converter
# Ask user for temperature and unit (C or F)
# Convert and print both values
# C to F: (C × 9/5) + 32
# F to C: (F - 32) × 5/9
print("\n39. Temperature Converter ⭐⭐⭐")
# YOUR CODE HERE:



# ----- Exercise 40 ⭐⭐⭐ -----
# Shopping Receipt
# Ask for 3 items (name and price each)
# Print a formatted receipt with tax (8%)
# ================================
#        SHOPPING RECEIPT
# ================================
# 1. Apple         $2.50
# 2. Bread         $3.00
# 3. Milk          $4.50
# --------------------------------
# Subtotal:       $10.00
# Tax (8%):        $0.80
# --------------------------------
# TOTAL:          $10.80
# ================================
# Thank you for shopping!
print("\n40. Shopping Receipt ⭐⭐⭐")
# YOUR CODE HERE:



# ============================================
print("\n" + "=" * 60)
print("🎉 GREAT JOB! You completed Input & Print exercises!")
print("=" * 60)
print("\nScroll down for SOLUTIONS...")
print("." * 30)
print("." * 30)
print("." * 30)


"""
============================================
SOLUTIONS
============================================

# ----- Exercise 1 -----
print("Hello, Python!")


# ----- Exercise 2 -----
print("John")
print("Blue")
print("Coding")


# ----- Exercise 3 -----
print('He said "Python is fun!"')
# Or: print("He said \"Python is fun!\"")


# ----- Exercise 4 -----
print("C:\\Users\\Documents\\file.txt")
# Or: print(r"C:\Users\Documents\file.txt")


# ----- Exercise 5 -----
print('''Roses are red,
Violets are blue,
Python is awesome,
And so are you!''')


# ----- Exercise 6 -----
for i in range(1, 6):
    print(i, end=" ")
print()  # New line at end


# ----- Exercise 7 -----
print("-" * 50)


# ----- Exercise 8 -----
print("********")
print("*      *")
print("*      *")
print("********")


# ----- Exercise 9 -----
print("\n\n")
print("Hello")
# Or: print("\n\n\nHello")


# ----- Exercise 10 -----
print("Name\t\tAge\tCity")
print("John\t\t25\tNYC")
print("Alice\t\t30\tLA")


# ----- Exercise 11 -----
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")


# ----- Exercise 12 -----
price = 49.99
quantity = 3
print(f"Total: ${price * quantity}")


# ----- Exercise 13 -----
pi = 3.14159265359
print(f"Pi = {pi:.2f}")


# ----- Exercise 14 -----
amount = 1234567.89
print(f"Amount: {amount:,.2f}")


# ----- Exercise 15 -----
percentage = 0.756
print(f"Score: {percentage:.2%}")


# ----- Exercise 16 -----
number = 42
print(f"Decimal: {number}")
print(f"Binary: {number:b}")
print(f"Hexadecimal: {number:x}")
print(f"Octal: {number:o}")


# ----- Exercise 17 -----
text = "python"
print(f"{text:*^20}")


# ----- Exercise 18 -----
item = "Apple"
price = 1.50
qty = 5
print(f"{item:<15}x{qty:<5}${price * qty:.2f}")


# ----- Exercise 19 -----
name = "Alice"
score = 95
print("Student {} scored {} points".format(name, score))


# ----- Exercise 20 -----
name = "Bob"
age = 30
print("%s is %d years old" % (name, age))


# ----- Exercise 21 -----
name = input("Enter your name: ")
print(f"Hello, {name}!")


# ----- Exercise 22 -----
food = input("What's your favorite food? ")
print(f"Wow, {food} is delicious!")


# ----- Exercise 23 -----
age = int(input("Enter your age: "))
year = 2024 - age
print(f"You were born in {year}")


# ----- Exercise 24 -----
num = int(input("Enter a number: "))
print(f"Double: {num * 2}")
print(f"Triple: {num * 3}")


# ----- Exercise 25 -----
num = float(input("Enter a decimal number: "))
print(f"Rounded: {num:.2f}")


# ----- Exercise 26 -----
first = input("Enter first name: ")
last = input("Enter last name: ")
print(f"{last}, {first}")


# ----- Exercise 27 -----
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
total = num1 + num2 + num3
average = total / 3
print(f"Sum: {total}")
print(f"Average: {average:.2f}")


# ----- Exercise 28 -----
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")


# ----- Exercise 29 -----
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
salary = hours * rate
print(f"Total Salary: ${salary:.2f}")


# ----- Exercise 30 -----
num = float(input("Enter a number: "))
print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}")
print(f"Square Root: {num ** 0.5:.2f}")


# ----- Exercise 31 -----
nums = input("Enter 3 numbers separated by spaces: ").split()
num1, num2, num3 = int(nums[0]), int(nums[1]), int(nums[2])
print(f"Sum: {num1 + num2 + num3}")


# ----- Exercise 32 -----
data = input("Enter name,age: ").split(",")
name, age = data[0], data[1]
print(f"Name: {name}, Age: {age}")


# ----- Exercise 33 -----
nums = input("Enter 5 numbers: ").split()
nums = [int(n) for n in nums]
print(f"Min: {min(nums)}, Max: {max(nums)}")


# ----- Exercise 34 -----
date = input("Enter date (DD/MM/YYYY): ").split("/")
day, month, year = date[0], date[1], date[2]
print(f"Day: {day}, Month: {month}, Year: {year}")


# ----- Exercise 35 -----
items = input("Enter items (comma separated): ").split(",")
for i, item in enumerate(items, 1):
    print(f"{i}. {item.strip()}")


# ----- Exercise 36 -----
recipient = input("Enter recipient name: ")
sender = input("Enter sender name: ")
message = input("Enter message: ")
print("╔" + "═" * 32 + "╗")
print(f"║     Dear {recipient},".ljust(33) + "║")
print("║" + " " * 32 + "║")
print(f"║     {message}".ljust(33) + "║")
print("║" + " " * 32 + "║")
print(f"║     From: {sender}".ljust(33) + "║")
print("╚" + "═" * 32 + "╝")


# ----- Exercise 37 -----
item = input("Enter item name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))
tip_pct = float(input("Enter tip percentage: "))

subtotal = price * qty
tip = subtotal * (tip_pct / 100)
total = subtotal + tip

print("=" * 32)
print("       RESTAURANT BILL")
print("=" * 32)
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {qty}")
print("-" * 32)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tip ({tip_pct}%): ${tip:.2f}")
print("-" * 32)
print(f"TOTAL: ${total:.2f}")
print("=" * 32)


# ----- Exercise 38 -----
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
dept = input("Enter department: ")
year = input("Enter year: ")

print("┌" + "─" * 30 + "┐")
print("│" + "STUDENT ID CARD".center(30) + "│")
print("├" + "─" * 30 + "┤")
print(f"│ Name: {name}".ljust(31) + "│")
print(f"│ ID: {student_id}".ljust(31) + "│")
print(f"│ Dept: {dept}".ljust(31) + "│")
print(f"│ Year: {year}".ljust(31) + "│")
print("└" + "─" * 30 + "┘")


# ----- Exercise 39 -----
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit:.2f}°F")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius:.2f}°C")
else:
    print("Invalid unit!")


# ----- Exercise 40 -----
print("Enter 3 items:")
item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: "))
item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: "))
item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: "))

subtotal = price1 + price2 + price3
tax = subtotal * 0.08
total = subtotal + tax

print("=" * 32)
print("       SHOPPING RECEIPT")
print("=" * 32)
print(f"1. {item1:<15}${price1:.2f}")
print(f"2. {item2:<15}${price2:.2f}")
print(f"3. {item3:<15}${price3:.2f}")
print("-" * 32)
print(f"Subtotal:       ${subtotal:.2f}")
print(f"Tax (8%):        ${tax:.2f}")
print("-" * 32)
print(f"TOTAL:          ${total:.2f}")
print("=" * 32)
print("Thank you for shopping!")

"""

print("\n✅ Exercises file created!")
print("Start practicing!")
