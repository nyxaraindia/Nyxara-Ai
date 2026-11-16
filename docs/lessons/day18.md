# Day 18 — Python Error Handling

## 1. Learning Objectives

By the end of Day 18, I should understand:

- What errors are and why they happen.
- Common Python errors.
- How `try` and `except` work.
- How to use `else` and `finally`.
- How to raise an exception using `raise`.
- How to use `pass`.
- How error handling makes NYXARA AI more reliable.

---

## 2. What Is an Error?

An error is a problem that occurs when a program cannot execute an instruction successfully.

Example:

```python
print(10 / 0)
```

Output:

```
ZeroDivisionError: division by zero
```

A computer cannot divide a number by zero.

Errors can stop a program unexpectedly. Error handling helps us manage these situations.

---

## 3. Common Python Errors

### 3.1 SyntaxError

Happens when Python syntax is incorrect.

```python
if 10 > 5
    print("Correct")
```

Problem: The colon `:` is missing after the condition.

### 3.2 NameError

Happens when we use a variable that does not exist.

```python
print(username)
```

Problem: `username` was never defined.

### 3.3 ZeroDivisionError

Happens when we divide by zero.

```python
print(10 / 0)
```

### 3.4 ValueError

Happens when a value has the wrong format for an operation.

```python
number = int("hello")
```

Problem: `"hello"` cannot be converted into an integer.

---

## 4. What Is Exception Handling?

Exception handling allows a program to respond to certain errors instead of stopping unexpectedly.

Python provides these important keywords:

| Keyword   | Purpose                                            |
| --------- | -------------------------------------------------- |
| `try`     | Attempts to execute code that might cause an error |
| `except`  | Handles an error                                   |
| `else`    | Runs when no exception occurs in `try`             |
| `finally` | Always runs after the try/except structure         |
| `raise`   | Manually generates an exception                    |
| `pass`    | Does nothing; acts as a placeholder                |

---

## 5. Understanding try and except

### Example

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```
Cannot divide by zero
```

### Explanation

1. Python enters the `try` block.
2. It attempts to divide 10 by 0.
3. A `ZeroDivisionError` occurs.
4. Python moves to the matching `except` block.
5. The error is handled.
6. The program continues after the structure.

Think of it like this:

- `try` = Try doing something.
- `except` = If a particular error happens, handle it.

---

## 6. Handling Multiple Errors

A program can encounter different types of errors.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Possible outputs:

Input: `10`

```
Result: 10.0
```

Input: `hello`

```
Please enter a valid number
```

Input: `0`

```
Cannot divide by zero
```

Each `except` block handles a different type of error.

---

## 7. Understanding else

The `else` block runs only when no exception occurs inside the `try` block.

Example:

```python
try:
    number = int("25")
except ValueError:
    print("Invalid input")
else:
    print("Conversion successful")
```

Output:

```
Conversion successful
```

Remember:

- `try` attempts the operation.
- `except` handles an error.
- `else` runs if no error occurs.

---

## 8. Understanding finally

The `finally` block always runs, whether an exception occurs or not.

Example:

```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program finished")
```

Output:

```
5.0
Program finished
```

Even if an error occurs, `finally` still runs. It is useful for cleanup operations, such as closing files.

---

## 9. Combining try, except, else and finally

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Calculation completed")
```

The execution order is:

1. Python enters `try`.
2. If an error occurs, a matching `except` block handles it.
3. If no error occurs, `else` executes.
4. `finally` executes in either case.

---

## 10. Understanding raise

The `raise` keyword allows us to deliberately generate an exception.

Why would we generate an error ourselves? Sometimes a value is valid Python data but is not acceptable for our program.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

print("Age accepted")
```

Output:

```
ValueError: Age cannot be negative
```

### Another example

```python
batch_size = 0

if batch_size <= 0:
    raise ValueError("Batch size must be greater than zero")
```

In NYXARA AI, we can use this to reject invalid training settings.

### Handling a raised exception

```python
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as error:
    print("Error:", error)
```

Output:

```
Error: Age cannot be negative
```

Here:

- `raise` generates the exception.
- `except` catches it.
- `as error` stores the exception object in the variable `error`.

---

## 11. Understanding pass

The `pass` keyword does nothing. It is used when Python requires a statement but we have not written the actual code yet.

Example:

```python
try:
    number = int("hello")
except ValueError:
    pass
```

The program catches the error but performs no action inside the `except` block.

Important: `pass` does not fix an error. It simply leaves the block empty.

---

## 12. Error Handling in NYXARA AI

Imagine NYXARA AI is preparing a training batch. The program expects a positive batch size.

```python
try:
    batch_size = int(input("Enter batch size: "))
    if batch_size <= 0:
        raise ValueError("Batch size must be positive")
except ValueError as error:
    print("Training configuration error:", error)
else:
    print("Training batch accepted:", batch_size)
finally:
    print("Configuration check completed")
```

Why is this useful?

- Prevents invalid training settings.
- Handles incorrect user input.
- Makes programs more reliable.
- Helps prevent unexpected crashes from known input errors.

This is an important foundation for building reliable AI software.

---

## 13. Day 18 Knowledge Check

| Question | Topic               | Result  |
| -------- | ------------------- | ------- |
| 1        | try and except      | Correct |
| 2        | else and finally    | Correct |
| 3        | ValueError handling | Correct |
| 4        | raise               | Correct |
| 5        | pass                | Correct |

**Knowledge check score: 5/5 (100%)**

---

## 14. Day 18 Practical Exercises

Practical coding exercises are pending.

### Exercise 1 — Safe Calculator

Create this file:

`src/fundamentals/python/day18_safe_calculator.py`

Requirements:

1. Ask the user to enter two numbers.
2. Convert both inputs into numbers.
3. Divide the first number by the second.
4. Handle `ValueError`.
5. Handle `ZeroDivisionError`.
6. Use `else` to display the result when successful.
7. Use `finally` to print `"Calculation completed"`.

Expected behaviour:

Input:

```
20
5
```

Expected output:

```
Result: 4.0
Calculation completed
```

Input:

```
20
0
```

Expected output:

```
Cannot divide by zero!
Calculation completed
```

Input:

```
hello
```

Expected output:

```
Invalid input! Enter numbers only.
Calculation completed
```

### Exercise 2 — NYXARA AI Training Validator

Create this file:

`src/fundamentals/python/day18_training_validator.py`

Requirements:

1. Ask the user to enter a batch size.
2. Convert the input into an integer.
3. Use `raise ValueError` if the batch size is less than or equal to zero.
4. Catch the exception using `except`.
5. Use `else` to display the accepted batch size.
6. Use `finally` to print `"Configuration check completed"`.

Expected behaviour:

Input:

```
32
```

Expected output:

```
Batch size accepted: 32
Configuration check completed
```

Input:

```
0
```

Expected output:

```
Configuration error: Batch size must be greater than zero
Configuration check completed
```

### Exercise 3 — Predict the Output

Do not run the code immediately. First, predict its output.

```python
try:
    number = int("50")
    if number > 40:
        raise ValueError("Number is too large")
    print("Accepted")
except ValueError as error:
    print("Error:", error)
finally:
    print("Finished")
```

Write down the output and explain why `"Accepted"` does or does not appear.

Correct output:

```
Error: Number is too large
Finished
```

---

## 15. Day 18 Summary

Today I learned:

- Common Python errors: SyntaxError, NameError, ZeroDivisionError and ValueError.
- Exception handling with `try` and `except`.
- Handling multiple exceptions.
- Using `else` and `finally`.
- Generating exceptions using `raise`.
- Using `pass` as a placeholder.
- Applying error handling to NYXARA AI training configuration.

### Day 18 Status

| Activity                        | Status     |
| ------------------------------- | ---------- |
| Concepts                        | Completed  |
| Knowledge check                 | 5/5 — 100% |
| Exercise 1 — Safe Calculator    | Pending    |
| Exercise 2 — Training Validator | Pending    |
| Exercise 3 — Predict Output     | Pending    |

---

## 16. Next Lesson

**Day 19 — Python File Handling**

Topics planned:

- What files are.
- Opening files.
- Reading files.
- Writing files.
- Appending data.
- Closing files.
- Using `with open()`.
- Understanding file paths.

File handling will help NYXARA AI save datasets, training information, and other project data.
