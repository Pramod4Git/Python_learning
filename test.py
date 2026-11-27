print("\nPyramid Pattern Program")
rows = int(input("Enter the number of rows for the pyramid: "))
for i in range(rows):
	print(' ' * (rows - i - 1) + '* ' * (i + 1))
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		return "Cannot divide by zero!"
	return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

elif choice == '2':
elif choice == '3':
elif choice == '4':
if choice == '1':
	print("Result:", add(num1, num2))
elif choice == '2':
	print("Result:", subtract(num1, num2))
elif choice == '3':
	print("Result:", multiply(num1, num2))
elif choice == '4':
	print("Result:", divide(num1, num2))
else:
	print("Invalid input")

