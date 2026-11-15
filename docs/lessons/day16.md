# Day 16 — Python Modules and Imports

## 1. Objective

By the end of this lesson, I should understand:

- What a Python module is.
- Why modules are useful.
- How to import built-in Python modules.
- How to use functions from imported modules.
- How to import specific functions.
- How to create my own Python module.
- How to use a custom module in another Python file.

---

## 2. What Is a Python Module?

A module is a Python file containing reusable code.

It can contain:

- Functions
- Variables
- Classes
- Other Python statements

Think of a module as a toolbox.

A toolbox contains different tools. Similarly, a Python module contains reusable programming tools.

For example, Python provides a built-in module called `math`.

It contains mathematical functions such as:

- `sqrt()` — square root
- `floor()` — round down
- `ceil()` — round up
- `pow()` — power

---

## 3. Why Are Modules Important?

Imagine building NYXARA AI.

The project may require:

- Mathematical calculations.
- Text processing.
- Random number generation.
- Data processing.
- File management.

Writing everything in one Python file would make the project difficult to manage.

Modules help us:

1. Organize code.
2. Reuse existing functions.
3. Avoid unnecessary repetition.
4. Maintain large projects.
5. Divide projects into smaller components.

---

## 4. Importing a Module

Python uses the `import` keyword to bring a module into a program.

Example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

### Explanation

- `import math` imports the math module.
- `math.sqrt(25)` calls the square-root function.
- `print()` displays the result.

The dot (`.`) connects the module name with its function.

---

## 5. Understanding Float Results

Why does `math.sqrt(36)` produce `6.0` instead of `6`?

Because `math.sqrt()` returns a floating-point number (`float`).

Example:

```python
print(6)
print(6.0)

print(type(6))
print(type(6.0))
```

Output:

```text
6
6.0
<class 'int'>
<class 'float'>
```

Both values represent the same mathematical quantity.

However:

- `6` is an integer.
- `6.0` is a floating-point number.

Square roots can produce decimal values, so the function returns a float.

Example:

```python
import math

print(math.sqrt(25))
print(math.sqrt(2))
```

Output:

```text
5.0
1.4142135623730951
```

---

## 6. The math.floor() Function

`math.floor()` rounds a number down to the nearest integer.

Example:

```python
import math

print(math.floor(8.9))
print(math.floor(5.7))
print(math.floor(4.1))
```

Output:

```text
8
5
4
```

Important:

Floor means rounding down.

---

## 7. The math.ceil() Function

`math.ceil()` rounds a number up to the nearest integer.

Example:

```python
import math

print(math.ceil(8.1))
print(math.ceil(8.9))
print(math.ceil(8.0))
```

Output:

```text
9
9
8
```

Important:

Ceil means rounding up.

---

## 8. The math.pow() Function

`math.pow()` calculates the power of a number.

Syntax:

```python
math.pow(base, exponent)
```

Example:

```python
import math

print(math.pow(2, 3))
print(math.pow(3, 2))
print(math.pow(5, 2))
```

Output:

```text
8.0
9.0
25.0
```

Mathematical explanation:

2³ = 2 × 2 × 2 = 8

3² = 3 × 3 = 9

5² = 5 × 5 = 25

Important:

`math.pow()` returns a float.

---

## 9. Importing Specific Functions

We do not always need to import an entire module.

We can import only the functions we need.

Example:

```python
from math import sqrt

print(sqrt(49))
```

Output:

```text
7.0
```

Explanation:

- `from math` identifies the module.
- `import sqrt` imports only the square-root function.
- `sqrt(49)` calls the imported function directly.

We do not need to write `math.sqrt()` here.

### Importing Multiple Functions

```python
from math import sqrt, pow

print(sqrt(64))
print(pow(3, 2))
```

Output:

```text
8.0
9.0
```

---

## 10. Two Ways to Import

### Method 1: Import the Complete Module

```python
import math

print(math.sqrt(49))
print(math.pow(2, 3))
```

### Method 2: Import Specific Functions

```python
from math import sqrt, pow

print(sqrt(49))
print(pow(2, 3))
```

Both methods work.

The difference is how we access the functions.

---

## 11. Creating Our Own Python Module

We can create our own modules.

A Python file can be imported into another Python file.

For example, imagine we have two files:

```text
project/
    calculator.py
    main.py
```

### File 1: calculator.py

```python
def add(a, b):
    return a + b
```

This file contains a function named `add()`.

### File 2: main.py

```python
import calculator

result = calculator.add(10, 20)

print(result)
```

Output:

```text
30
```

### Explanation

1. `import calculator` imports our own module.
2. `calculator.add(10, 20)` calls the function.
3. The function adds the two numbers.
4. `return` sends the result back.
5. `print(result)` displays the answer.

Both files should be in the same directory for this simple example.

---

## 12. Adding More Functions to Our Module

We can store multiple functions inside one module.

### calculator.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

### main.py

```python
import calculator

print(calculator.add(10, 20))
print(calculator.subtract(20, 5))
print(calculator.multiply(4, 5))
```

Output:

```text
30
15
20
```

One module can contain many reusable functions.

---

## 13. Understanding the Logic

Consider this structure:

```text
main.py
   |
   | imports
   v
calculator.py
   |
   | contains
   v
add(), subtract(), multiply()
```

The main program uses functions stored in another file.

This helps us divide a large project into smaller parts.

For NYXARA AI, we can eventually organize different components into separate modules.

For example:

```text
NYXARA AI/
    src/
        tokenizer/
        data_processing/
        model/
        training/
        evaluation/
```

This is a conceptual example of project organization. We will develop the actual structure gradually.

---

## 14. Important Difference: print() and return

A function can display a result or return a result.

Example:

```python
def add(a, b):
    print(a + b)


add(10, 20)
```

Output:

```text
30
```

Here, the function displays the result.

Now consider:

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

Output:

```text
30
```

Here, the function returns the result so another part of the program can use it.

Remember:

- `print()` displays information.
- `return` sends a value back to the caller.

---

## 15. Day 16 Quiz and Results

All eight quiz questions were answered correctly.

| Question | Topic | Result |
|----------|-------|--------|
| 1 | math.sqrt() | Correct |
| 2 | math.floor() | Correct |
| 3 | math.ceil() | Correct |
| 4 | math.pow() | Correct |
| 5 | Importing sqrt | Correct |
| 6 | Importing multiple functions | Correct |
| 7 | Creating a custom module | Correct |
| 8 | Combined math operations | Correct |

### Final Quiz Score

- Correct answers: 8
- Incorrect answers: 0
- Total questions: 8
- Score: 100%

**Day 16 Quiz: 8/8**

---

## 16. Practical Coding Exercise

### Exercise: Create Your Own Calculator Module

Create two Python files inside:

`src/fundamentals/python/`

File 1:

`calculator.py`

File 2:

`day16_modules.py`

### Requirements

In `calculator.py`:

Create these three functions:

1. `add(a, b)` — addition.
2. `subtract(a, b)` — subtraction.
3. `multiply(a, b)` — multiplication.

Each function must return its result.

In `day16_modules.py`:

1. Import the calculator module.
2. Call all three functions.
3. Store their returned values in variables.
4. Print all three results.

### Expected Output

```text
Addition: 30
Subtraction: 15
Multiplication: 20
```

Use these test values:

- Addition: 10 and 20.
- Subtraction: 20 and 5.
- Multiplication: 4 and 5.

### Learning Rule

Try writing the code independently.

Do not copy a complete solution before understanding the logic.

---

## 17. Mistakes to Avoid

### Mistake 1: Forgetting to Import

Incorrect:

```python
print(math.sqrt(25))
```

If `math` has not been imported, Python raises a `NameError`.

Correct:

```python
import math

print(math.sqrt(25))
```

### Mistake 2: Forgetting the Module Name

Incorrect:

```python
import math

print(sqrt(25))
```

Correct:

```python
import math

print(math.sqrt(25))
```

Alternatively:

```python
from math import sqrt

print(sqrt(25))
```

### Mistake 3: Incorrect File Location

If Python cannot find your custom module, check:

- Whether both files are in the expected directory.
- Whether the module filename is correct.
- Whether the import statement matches the filename.

### Mistake 4: Confusing print() and return

Remember that displaying a value and returning a value are different operations.

---

## 18. Day 16 Summary

Today I learned:

- A module is a Python file containing reusable code.
- `import` brings a module into a program.
- Python provides built-in modules such as `math`.
- `math.sqrt()` calculates square roots.
- `math.floor()` rounds down.
- `math.ceil()` rounds up.
- `math.pow()` calculates powers.
- `from ... import ...` imports specific functions.
- We can create our own modules.
- Multiple Python files can work together.
- Modules help organize large projects.

### Day 16 Status

- Lesson completed: Yes
- Quiz completed: Yes
- Quiz score: 8/8
- Quiz percentage: 100%
- Practical coding exercise: Pending
- Overall status: In progress until the coding exercise is completed.

---

## 19. Day 17 Preview

### Topic: Python Packages and Project Organization

In Day 17, we will learn:

- Difference between modules and packages.
- What is a Python package?
- How folders organize Python modules.
- The purpose of `__init__.py`.
- How to import modules from packages.
- How to organize a larger Python project.

We will connect these concepts to the NYXARA AI project structure.

---

# End of Day 16
# NYXARA AI — Building Intelligence from the Foundations
