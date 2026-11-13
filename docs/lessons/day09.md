# Day 9 — Python Functions: Parameters, Scope and Problem Solving

## Learning Objective

By the end of this lesson, you should be able to:
- Use functions with multiple parameters.
- Understand arguments and parameters.
- Trace function execution step by step.
- Understand local variables and variable scope.
- Distinguish local and global variables.
- Solve practical problems using functions and return values.

---

## 1. Revision: What Is a Function?

A function is a named, reusable block of instructions.

Instead of writing the same instructions repeatedly, we define a function once and call it whenever needed.

Example:

```python
def multiply(a, b):
    result = a * b
    print(result)

multiply(4, 5)
multiply(3, 7)
```

Output:

```text
20
21
```

The function executes twice because we called it twice.

## 2. Parameters and Arguments

### Parameters

Parameters are the variable names written inside the parentheses when defining a function.

Example:

```python
def multiply(a, b):
    return a * b
```

Here:
- `a` is a parameter.
- `b` is a parameter.

### Arguments

Arguments are the actual values supplied when calling a function.

Example:

```python
multiply(4, 5)
```

Here:
- `4` is an argument.
- `5` is an argument.

Python assigns argument values to parameters by position in this example.

### Remember

| Term | Meaning |
|---|---|
| Parameter | Name in the function definition |
| Argument | Actual value supplied during a function call |

---

## 3. Functions with Multiple Parameters

A function can accept more than two parameters.

Example:

```python
def calculate_final_price(price, quantity, tax):
    subtotal = price * quantity
    final_price = subtotal + tax
    return final_price

total = calculate_final_price(100, 2, 20)

print(total)
```

Output:

```text
220
```

### Step-by-step calculation

1. Price = 100
2. Quantity = 2
3. Tax = 20
4. Subtotal = 100 * 2 = 200
5. Final price = 200 + 20 = 220

The function receives three arguments and uses them to calculate the result.

---

## 4. Dry-Run Exercise 1

Code:

```python
def calculate(a, b, c):
    result = a + b
    final = result * c
    return final

answer = calculate(5, 3, 2)

print(answer)
```

### Student's Answers

1. `result = 8`
2. Initially answered `final = 10`, then corrected after reviewing the calculation.
3. Correct final output = 16.
4. Correctly explained that arguments are assigned to parameters by position.

### Correct Calculation

- a = 5
- b = 3
- c = 2
- result = 5 + 3 = 8
- final = 8 * 2 = 16
- answer = 16

Output:

```text
16
```

### Learning Point

Always follow the actual mathematical operator in the code.

- `+` means addition.
- `*` means multiplication.
- `-` means subtraction.
- `/` means division.

---

## 5. Dry-Run Exercise 2

Code:

```python
def calculate(x, y):
    first = x * y
    second = first + 10
    third = second - 5
    return third

answer = calculate(4, 3)
print(answer)
```

### Student's Answers

1. first = 12
2. second = 22
3. third = 17
4. Output = 17

### Correct Calculation

- first = 4 * 3 = 12
- second = 12 + 10 = 22
- third = 22 - 5 = 17

Output:

```text
17
```

All four answers were correct.

---

## 6. What Is Variable Scope?

Variable scope means the part of a program where a variable can be accessed.

Python has local and global variables.

### Local Variables

A local variable is created inside a function.

Example:

```python
def calculate(a, b):
    result = a + b
    return result

answer = calculate(10, 20)

print(answer)
print(result)
```

Expected behaviour:

- `answer` displays 30.
- `result` causes a NameError because it is not defined in the outside scope.

Why?

1. The function creates `result` inside itself.
2. It calculates 10 + 20.
3. `return result` sends the value 30 back.
4. `answer` receives 30.
5. The local variable `result` is not normally accessible outside the function.

Expected output before the error:

```text
30
NameError: name 'result' is not defined
```

This is not because `return` failed. It is because of variable scope.

---

## 7. Local and Global Variables with the Same Name

Consider:

```python
def calculate(a, b):
    result = a + b
    return result

answer = calculate(10, 20)
result = 100

print(answer)
print(result)
```

Output:

```text
30
100
```

### Explanation

Inside the function:

- A local variable `result` is created.
- Its value is 30.
- The function returns 30.

Outside the function:

- Another variable named `result` is created.
- Its value is 100.

These are two separate variables.

### Student's Understanding

The student correctly predicted:
- First output = 30.
- Second output = 100.

The student explained that the outside variable is defined independently rather than accessing the local variable inside the function.

---

## 8. Independent Coding Challenge — Discount Calculator

### Objective

Create a function called `calculate_discount`.

Requirements:

1. Accept `price` and `discount`.
2. Calculate the discount amount.
3. Subtract the discount amount from the original price.
4. Return the final price.
5. Call the function with price 1000 and discount 10.
6. Print the returned result.

### Student's Independent Code

```python
def calculate_discount(price, discount):
    discount = (price * discount) / 100
    result = price - discount
    return result

final = calculate_discount(1000, 10)

print(f'Total price to pay:{final}')
```

### Calculation

Original price = 1000

Discount percentage = 10%

Discount amount:

1000 * 10 / 100 = 100

Final price:

1000 - 100 = 900

### Verified Terminal Output

```text
Total price to pay:900.0
```

< The program was successfully executed in the NYXARA AI VS Code terminal.

### Code Review

The student's code is correct.

One improvement is to use a more descriptive variable name:

```python
def calculate_discount(price, discount):
    discount_amount = (price * discount) / 100
    final_price = price - discount_amount
    return final_price

final = calculate_discount(1000, 10)

print(f'Total price to pay: {final}')
```

Why is this better?

- `discount_amount` clearly represents the calculated money amount.
- `discount` remains the percentage parameter.
- `final_price` clearly represents the amount after discount.

### Why Does Python Display 900.0?

Python's `/` operator performs normal division and produces a floating-point result.

Example:

```python
print(100 / 10)
```

Output:

```text
10.0
```

Therefore, the discount calculator displays `900.0` instead of `900`.

This is correct.

---

## 9. Terminal and File Troubleshooting

During Day 9, the student worked with:

File:

```text
src/fundamentals/python/day09_calculate_discount.py
```

Correct execution command from the project root:

```bash
python src/fundamentals/python/day09_calculate_discount.py
```

The program executed successfully.

### Important Lessons

- Check the filename carefully.
- Check the current working directory.
- Use the correct relative path.
- Do not include unnecessary quotation marks.
- Use `ls` to inspect files and directories.

---

## 10. Day 9 Knowledge Review

Questions to revise:

1. What is a function?
2. What is the difference between a parameter and an argument?
3. Can a function accept multiple parameters?
4. What is variable scope?
5. What is a local variable?
6. Why can't a local variable normally be accessed outside its function?
7. Can a local variable and a global variable have the same name?
8. What is the difference between `print()` and `return`?
9. Why does normal division using `/` produce a floating-point result?
10. How can functions help us avoid repeating code?

---

## 11. Student Progress Record

### Concepts Successfully Learned

- Function definitions and function calls.
- Multiple parameters.
- Arguments and parameter positions.
- Returning calculated values.
- Local variables.
- Variable scope.
- Difference between local and global variables.
- Practical calculations using functions.

### Exercises Completed

- Multiple-parameter calculation.
- Function execution dry runs.
- Arithmetic tracing.
- Local variable scope exercise.
- Local and global variable exercise.
- Independent discount calculator.

### Practical Achievement

The student independently wrote and executed a discount calculator.

Verified result:

```text
900.0
```

### Mistakes and Corrections

1. Initially miscalculated multiplication in the first dry-run exercise. Corrected by tracing the operation step by step.
2. Initially described local-variable errors as missing variables. Learned the precise concept of variable scope.
3. Learned why `/` produces floating-point results.

### Overall Progress

Day 9 practical challenge completed successfully.

The student demonstrated the ability to write, execute and reason about a function independently.

---

## 12. What Comes Next?

### Day 10 — Default Parameters and Keyword Arguments

Planned topics:

1. Default parameter values.
2. Calling functions with keyword arguments.
3. Positional arguments versus keyword arguments.
4. Understanding argument assignment.
5. More independent coding exercises.

The next lesson should continue with simple explanations, dry runs, independent coding and debugging.

---

**NYXARA AI — Learning from fundamentals to independent AI development.**
