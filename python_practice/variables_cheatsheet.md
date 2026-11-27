# Python Variables - Cheat Sheet

Quick reference guide for Python variables and naming conventions.

---

## Variable Basics

```python
# Creating variables (no declaration needed)
name = "John"           # String
age = 25                # Integer
price = 19.99           # Float
is_active = True        # Boolean
items = [1, 2, 3]       # List
person = {"name": "John"}  # Dictionary
```

---

## Naming Rules

| Rule | Example ✅ | Invalid ❌ |
|------|-----------|-----------|
| Start with letter/underscore | `name`, `_count` | `1name`, `@var` |
| Letters, numbers, underscores only | `user_1`, `total_count` | `user-name`, `my.var` |
| Case sensitive | `Name` ≠ `name` | - |
| No reserved keywords | `my_class` | `class`, `for`, `if` |

---

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | `snake_case` | `user_name`, `total_amount` |
| Functions | `snake_case` | `calculate_total()`, `get_user()` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_SIZE`, `API_KEY` |
| Classes | `PascalCase` | `UserAccount`, `ShoppingCart` |
| Private | `_leading_underscore` | `_internal_method()` |
| Booleans | `is_`, `has_`, `can_` prefix | `is_active`, `has_permission` |

---

## Variable Scope

### Local Variables
```python
def my_function():
    local_var = "I'm local"    # Only exists inside this function
    print(local_var)           # ✅ Works

my_function()
# print(local_var)             # ❌ Error - not accessible here
```

### Global Variables
```python
global_var = "I'm global"      # Defined outside functions

def my_function():
    print(global_var)          # ✅ Can READ global

my_function()
print(global_var)              # ✅ Works
```

### Modifying Global Variables
```python
counter = 0

def increment():
    global counter             # Required to MODIFY global
    counter += 1

increment()
print(counter)                 # 1
```

---

## Quick Reference Table

| Action | Need `global` keyword? |
|--------|----------------------|
| Read global variable | ❌ No |
| Modify global integer/string | ✅ Yes |
| Append to global list | ❌ No (modifying content) |
| Reassign global list | ✅ Yes |

---

## Common Patterns

### Multiple Assignment
```python
a, b, c = 1, 2, 3
```

### Swap Variables
```python
x, y = y, x
```

### Default Values
```python
name = input("Name: ") or "Guest"
```

### Constants with Type Hints
```python
MAX_RETRIES: int = 3
API_URL: str = "https://api.example.com"
```

---

## LEGB Rule (Scope Resolution Order)

```
L - Local      (inside current function)
E - Enclosing  (outer function, if nested)
G - Global     (module level)
B - Built-in   (Python built-ins)
```

Python searches for variables in this order: L → E → G → B

---

## Common Mistakes to Avoid

```python
# ❌ BAD: Starting with number
1st_name = "John"

# ✅ GOOD
first_name = "John"


# ❌ BAD: Using reserved keyword
class = "Python"

# ✅ GOOD
class_name = "Python"


# ❌ BAD: Forgetting global keyword
count = 0
def add():
    count += 1    # Error!

# ✅ GOOD
count = 0
def add():
    global count
    count += 1


# ❌ BAD: Vague names
x = 50000
y = 12
z = x / y

# ✅ GOOD
annual_salary = 50000
months = 12
monthly_salary = annual_salary / months
```

---

## Python Reserved Keywords (Cannot Use as Variable Names)

```
False    True     None     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

Check if a word is keyword:
```python
import keyword
print(keyword.iskeyword("class"))  # True
print(keyword.kwlist)              # List all keywords
```
