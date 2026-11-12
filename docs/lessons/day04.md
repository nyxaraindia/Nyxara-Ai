# NYXARA AI — Day 4
## Python Input and Output

**Topic:** Receiving information from users and displaying results  
**Level:** Beginner  
**Status:** Completed

---

## 1. Learning Objectives

By the end of this lesson, we learned how to:

- Receive information using `input()`.
- Display information using `print()`.
- Understand why `input()` returns a string.
- Convert strings into integers using `int()`.
- Convert strings into decimal numbers using `float()`.
- Perform calculations using user input.
- Display formatted output using f-strings.
- Understand the difference between string joining and numerical addition.

---

## 2. Input and Output

A computer program can communicate with a user.

There are two important Python functions:

| Function | Purpose |
|---|---|
| `input()` | Receives information from the user |
| `print()` | Displays information to the user |

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Example output:

```text
Enter your name: Amal
Hello Amal
```

### Explanation

- `input()` asks the user to enter information.
- The entered information is stored in `name`.
- `print()` displays the greeting.

---

## 3. Important Concept: input() Returns a String

Even when a user enters a number, Python initially treats the input as text.

Example:

```python
age = input("Enter your age: ")
```

If the user enters `19`, Python stores:

```python
"19"
```

Its data type is `str`, not `int`.

### Converting input into an integer

Use `int()`:

```python
age = int(input("Enter your age: "))
```

Now the value is an integer.

### Converting input into a decimal

Use `float()`:

```python
price = float(input("Enter product price: "))
```

Example: `25.50` becomes a floating-point number.

---

## 4. Independent Coding Challenge

### Problem

Create a program that:

1. Asks the user's name.
2. Asks the user's age.
3. Asks for two numbers.
4. Calculates their sum.
5. Displays the user's name, age and sum.

### Algorithm

1. Start.
2. Ask for the user's name.
3. Ask for the user's age.
4. Ask for the first number.
5. Ask for the second number.
6. Add both numbers.
7. Display the name, age and result.
8. Stop.

### Student's Code

File: `src/fundamentals/python/day04_input_output.py`

```python
name = input('Enter your name:')
age = int(input('Enter your age:'))
num1 = int(input('First number:'))
num2 = int(input('Second number:'))
sum = num1 + num2

print(f'Name={name}')
print(f'Age={age}')
print(f'Sum={sum}')
```

### Test Run

```text
Enter your name:Amal
Enter your age:19
First number:3
Second number:4
Name=Amal
Age=19
Sum=7
```

**Result:** The program executed successfully.

### Code Review

| Code | Explanation |
|---|---|
| `input()` | Receives information |
| `int()` | Converts text into an integer |
| `num1 + num2` | Adds the numbers |
| `print()` | Displays information |
| `f'Name={name}'` | Inserts a variable value into text |

### Improvement

The student initially used:

```python
sum = num1 + num2
```

This works, but `sum()` is already a built-in Python function.

A better variable name is:

```python
total = num1 + num2
```

Avoid using built-in function names as variable names.

---

## 5. String Concatenation vs Numerical Addition

This is an important concept.

Consider:

```python
num1 = input("First number: ")
num2 = input("Second number: ")

total = num1 + num2

print(total)
```

If the user enters:

```text
10
20
```

Python displays:

```text
1020
```

Why?

Because both values are strings.

When `+` is used with strings, Python joins the text together.

Compare:

| Expression | Result |
|---|---|
| `10 + 20` | `30` |
| `"10" + "20"` | `"1020"` |
| `int("10") + int("20")` | `30` |

To perform numerical addition, convert the input into integers.

---

## 6. Type Conversion Practice

Example:

```python
a = "5"
b = "3"

result = int(a) + int(b)

print(result)
```

Output:

```text
8
```

Explanation:

1. `a` contains the string `"5"`.
2. `b` contains the string `"3"`.
3. `int(a)` converts `"5"` into `5`.
4. `int(b)` converts `"3"` into `3`.
5. Python calculates `5 + 3`.
6. The result is `8`.

---

## 7. Quiz and Student Performance

### Initial Quiz

| Question | Student's Answer | Result |
|---|---|---|
| Which function receives user information? | `input()` | Correct |
| What is the default input data type? | `str` | Correct |
| Which function converts text into a whole number? | `int()` | Correct |

**Score: 3/3**

### Final Understanding Challenge

Question:

What happens when two inputs are added without converting them into integers?

Student's initial answer: Error.

Correction:

The correct answer is `1020`, because Python joins the two strings.

### Final Practice

Question:

```python
a = "5"
b = "3"

result = int(a) + int(b)

print(result)
```

Student's answer: `8`

Result: Correct.

---

## 8. Concepts Learned

- `input()` receives information from the user.
- `print()` displays information.
- `input()` returns a string.
- `int()` converts compatible text into an integer.
- `float()` converts compatible text into a decimal number.
- Strings can be joined using `+`.
- Numbers can be added using `+`.
- F-strings help display variable values inside text.
- Variable names should not overwrite Python built-in functions.

---

## 9. Student Progress

- Created an independent input/output program.
- Collected name and age using `input()`.
- Converted numerical inputs using `int()`.
- Added two user-provided numbers.
- Used `print()` and f-strings to display results.
- Scored 3/3 in the initial quiz.
- Learned that string inputs are joined, not numerically added.
- Correctly predicted `int("5") + int("3") = 8`.
- Learned to avoid using built-in names such as `sum` as variables.

---

## 10. Day 4 Result

**Status: Successfully Completed**

The student independently wrote and executed a working Python input/output program.

---

## 11. Next Lesson

**Day 5: Python Operators and Expressions**

Planned topics:

- Arithmetic operators
- Comparison operators
- Logical operators
- Operator precedence
- Expressions and evaluation
- Independent coding exercises

