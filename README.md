# Logic Box 🎲

## 📌 Project Description

The **Logic Box** is a beginner-friendly Python project that demonstrates fundamental programming concepts through two interactive utilities: a **Pattern Generator** and a **Number Analyzer**.

This project demonstrates important Python concepts such as:

- Variables
- Data Types
- Type Casting
- User Input
- Loops (for & while)
- Conditional Statements (if/else)
- Nested Loops
- Pattern Generation
- Arithmetic Operations
- Match Statement (Switch Case)

The program provides an interactive menu system where users can generate ASCII patterns or analyze numbers within a specified range.

---

# 🚀 Features

✅ Interactive menu-driven interface  
✅ Pattern Generator - creates star patterns based on user input  
✅ Number Analyzer - identifies even/odd numbers and calculates sum  
✅ Uses loops and conditional logic  
✅ Handles user input validation  
✅ Beginner-friendly and easy to understand  
✅ Demonstrates match/case statement (Python 3.10+)  

---

# 🛠 Technologies Used

- Python 3.10+
- Python Standard Library

---

# 📂 Project Structure

```bash
PR. 2 Logic Box
│
├── PR. 2 Logic Box.png
├── PR. 2 Logic Box.py
└── README.md
```

---

# 🧠 Concepts Used

## 1. While Loop

Used for creating an interactive menu that runs continuously.

Example:

```python
while True:
    print("select any option")
```

---

## 2. For Loop

Used to iterate through ranges and generate patterns.

Example:

```python
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print("*", end="")
```

---

## 3. Nested Loops

Used in pattern generation to control rows and columns.

Example:

```python
for i in range(1, x + 1):          # Outer loop
    for j in range(1, i + 1):      # Inner loop
        print("*", end="")
```

---

## 4. Conditional Statements (if/else)

Used to check if a number is even or odd.

Example:

```python
if i % 2 == 0:
    print(i, " is even")
else:
    print(i, " is odd")
```

---

## 5. Match Statement (Switch Case)

Used to handle menu selection with different cases.

Example:

```python
match n:
    case 0:
        print("exit")
        break
    case 1:
        # Pattern generator code
    case _:
        print("invalid input")
```

---

## 6. Type Casting

Type casting converts input strings to integers.

Example:

```python
n = int(input("Enter any option: "))
age = int(input("enter value."))
```

---

## 7. Modulo Operator (%)

Used to check if a number is even or odd.

Example:

```python
if i % 2 == 0:  # If remainder is 0, number is even
```

---

# ⚙️ How the Program Works

## Step 1

The program displays a welcome message and an interactive menu.

```python
print("welcome to the pattern generator and number analyzer program")
while True:
    print("select any option")
    print("0. exit")
    print("1. pattern generator")
    print("2. number analyzer")
```

---

## Step 2

The user selects an option (0, 1, or 2).

```python
n = int(input("Enter any option: "))
```

---

## Step 3: Option 1 - Pattern Generator

The user enters a number to generate a star pattern.

**Input:**
- A number representing rows

**Process:**
- Uses nested loops to generate triangular pattern
- Outer loop controls rows
- Inner loop controls columns (stars per row)

**Output:**
- Triangular pattern made of asterisks

---

## Step 4: Option 2 - Number Analyzer

The user enters a start and end value for the range.

**Input:**
- Start value
- Last value

**Process:**
- Iterates through range
- Checks if each number is even or odd
- Calculates sum of all numbers

**Output:**
- List of numbers with even/odd classification
- Total sum of all values

---

## Step 5

The program loops back to menu unless user selects option 0 (exit).

---

# 💻 Code Explanation

## Welcome Message and Menu Loop

```python
print("welcome to the pattern generator and number analyzer program")
while True:
    print("select any option")
    print("0. exit")
    print("1. pattern generator")
    print("2. number analyzer")
    n = int(input("Enter any option: "))
```

Creates infinite loop with menu options.

---

## Exit Option

```python
case 0:
    print("exit")
    break
```

Breaks the loop and exits the program.

---

## Pattern Generator Logic

```python
case 1:
    a = int(input("enter value."))
    x = a
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")
```

This code creates a triangle of stars (`*`) step by step:

1. `a = int(input("enter value."))`
   - Asks the user for a number.
   - Converts the typed value into an integer.

2. `x = a`
   - Saves the number as `x` so the next part knows how many rows to print.
   - This line keeps the code easy to read.

3. `for i in range(1, x + 1):`
   - Starts the outer loop.
   - `i` goes from `1` to `x`.
   - Each `i` means one row of the pattern.

4. `for j in range(1, i + 1):`
   - Starts the inner loop for the current row.
   - It prints one star for each value of `j`.
   - When `i` is `3`, it prints 3 stars in that row.

5. `print("*", end="")`
   - Prints a star without moving to a new line.
   - This makes the stars appear next to each other.

6. `print("")`
   - Moves to the next line after finishing one row.
   - This starts a new row of stars.

So, if the user enters `5`, the program prints:

```
*
**
***
****
*****
```

Each row has one more star than the previous row, forming a triangle.

---

## Number Analyzer Logic

```python
case 2:
    first = int(input("enter start value : "))
    last = int(input("enter last value : "))
    sum = 0
    for i in range(first, last + 1):
        if i % 2 == 0:
            print(i, " is even")
        else:
            print(i, " is odd")
        sum = sum + i
    print("sum of all values is", sum)
```

This code checks each number between two values and finds whether it is even or odd.

1. `first = int(input("enter start value : "))`
   - Asks the user for the starting number.
   - Converts the answer to an integer.

2. `last = int(input("enter last value : "))`
   - Asks the user for the ending number.
   - Converts that answer to an integer too.

3. `sum = 0`
   - Creates a variable called `sum` to save the total of all numbers.
   - It starts at `0` because nothing has been added yet.

4. `for i in range(first, last + 1):`
   - Starts a loop from the start number to the end number.
   - `i` becomes each number in the range, one by one.

5. `if i % 2 == 0:`
   - Checks if the current number `i` can be divided by 2 exactly.
   - If yes, the number is even.

6. `print(i, " is even")`
   - Shows the number and says it is even.

7. `else:` and `print(i, " is odd")`
   - If the number is not even, it is odd.
   - The program prints the number and says it is odd.

8. `sum = sum + i`
   - Adds the current number to the running total.
   - This keeps a total of every number in the range.

9. `print("sum of all values is", sum)`
   - After the loop finishes, the program shows the total sum.

So if the user enters `first = 5` and `last = 10`, the program checks 5, 6, 7, 8, 9, and 10.
It prints whether each one is even or odd, and then it prints the sum of all those numbers.

---

## Invalid Input Handling

```python
case _:
    print("invalid input")
```

Handles any invalid menu selection.

---

# ▶️ How to Run the Program

## Step 1: Open Terminal

Navigate to the project folder.

```bash
cd "PR. 2 Logic Box"
```

---

## Step 2: Run Python File

```bash
python '.\PR. 2 Logic Box.py'
```

---

## Step 3: Select Option

```
select any option
0. exit
1. pattern generator
2. number analyzer
Enter any option: 
```

---

# 🖥 Sample Output

### Pattern Generator (Input: 5)

```
*
**
***
****
*****
```

### Number Analyzer (Input: Start=5, Last=10)

```
5  is odd
6  is even
7  is odd
8  is even
9  is odd
10  is even
sum of all values is 45
```

---

# 🖼 Project Screenshot

![Logic Box Program Output](PR.%202%20Logic%20Box.png)

---

# 👨‍💻 Author

## Krish Patel

Data Analytics Learner.

---

# 🔗 Resources

- **GitHub Repository**: [https://github.com/patel0506/PR.-2-Logic-Box](https://github.com/patel0506/PR.-2-Logic-Box)

- **Video Tutorial**: <a href="https://drive.google.com/file/d/1ixFwMIOnLtEW-nEHthZpZipppQjD67EZ/view?usp=sharing" target="_blank" rel="noopener noreferrer">Watch Video</a>
