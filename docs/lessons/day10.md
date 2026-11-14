# Day 10 — Python Functions: Default Parameters and Keyword Arguments

## Learning Objective

By the end of this lesson, I should be able to:

- Understand function parameters and arguments.
- Understand default parameter values.
- Use positional arguments.
- Use keyword arguments.
- Combine positional and keyword arguments.
- Predict function outputs by manually tracing code.
- Write and execute Python functions using different argument types.

---

## 1. What Are Function Parameters?

A parameter is a variable listed inside a function definition.

Example:

```python
def calculate(price, quantity):
    total = price * quantity
    return total
```

Here:

- `price` is a parameter.
- `quantity` is a parameter.

Parameters receive values when we call the function.

## 2. What Are Arguments?

Arguments are the actual values supplied when calling a function.

Example:

```python
result = calculate(100, 3)
```

Here:

- `100` is an argument for `price`.
- `3` is an argument for `quantity`.

Remember:

- Parameter = variable in the function definition.
- Argument = value supplied when calling the function.

---

## 3. Default Parameters

A default parameter already has a value assigned in the function definition.

Example:

```python
def calculate_total(price, quantity=2):
    total = price * quantity
    return total
```

Here:

- `price` is a normal parameter.
- `quantity=2` is a default parameter.

When we call:

```python
result = calculate_total(100)
print(result)
```

Python automatically uses `quantity=2`.

Calculation:

```text
price = 100
quantity = 2

total = 100 * 2
total = 200
```

Output:

```text
200
```

### Overriding a Default Parameter

We can provide a different quantity.

```python
result = calculate_total(100, 4)
print(result)
```

Now:

```text
price = 100
quantity = 4

total = 100 * 4
total = 400
```

Output:

```text
400
```

The supplied value 4 replaces the default value 2.

---

## 4. Positional Arguments

Positional arguments are assigned according to their position in the function call.

Example:

```python
def calculate(price, quantity):
    return price * quantity

result = calculate(100, 3)
print(result)
```

Python assigns:

```text
First argument 100  -> price
Second argument 3   -> quantity
```

Output:

```text
300
```

The first argument goes to the first parameter, and the second argument goes to the second parameter.

---

## 5. Keyword Arguments

Keyword arguments assign values using parameter names.

Example:

```python
def calculate(price, quantity, discount):
    total = price * quantity
    final = total - discount
    return final

result = calculate(
    price=100,
    quantity=2,
    discount=20
)

print(result)
```

Calculation:

```text
100 * 2 = 200
200 - 20 = 180
```

Output:

```text
180
```

### Changing the Order

Keyword arguments can be supplied in a different order.

```python
result = calculate(
    discount=20,
    quantity=2,
    price=100
)

print(result)
```

Output:

```text
180
```

Python identifies the correct parameter using its name.

---

## 6. Combining Positional and Keyword Arguments

We can combine both types of arguments.

Example:

```python
def calculate(price, quantity=2, discount=0):
    total = price * quantity
    final = total - discount
    return final

result = calculate(100, discount=20)

print(result)
```

Python assigns:

```text
price = 100
quantity = 2
discount = 20
```

Why?

- `100` is the positional argument for price.
- Quantity is not supplied, so Python uses its default value 2.
- `discount=20` is a keyword argument.

Calculation:

```text
total = 100 * 2
total = 200

final = 200 - 20
final = 180
```

Output:

```text
180
```

### Important Rule

Positional arguments must come before keyword arguments.

Correct:

```python
calculate(100, discount=20)
```

Incorrect:

```python
calculate(price=100, 2, 20)
```

Python does not allow a positional argument after a keyword argument.

---

## 7. Complete Function Example

```python
def calculate(price, quantity=2, discount=0):
    total = price * quantity
    final = total - discount
    return final

a = calculate(100)
b = calculate(100, 3)
c = calculate(100, discount=20)
d = calculate(price=200, discount=50, quantity=2)

print(a)
print(b)
print(c)
print(d)
```

Expected output:

```text
200
300
180
350
```

Explanation:

| Variable | Price | Quantity | Discount | Result |
|---|---:|---:|---:|---:|
| a | 100 | 2 | 0 | 200 |
| b | 100 | 3 | 0 | 300 |
| c | 100 | 2 | 20 | 180 |
| d | 200 | 2 | 50 | 350 |

---

## 8. Practice Exercises and My Answers

### Exercise 1

```python
def calculate_total(price, quantity=2):
    return price * quantity

print(calculate_total(50))
```

My answer: 100

Correct answer: 100

### Exercise 2

```python
print(calculate_total(50, 4))
```

My answer: 200

Correct answer: 200

### Exercise 3

```python
def calculate(price, quantity=2, tax=0):
    total = price * quantity
    final = total + tax
    return final

print(calculate(100, tax=20))
```

My answer: 220

Correct answer: 220

### Exercise 4

```python
print(calculate(price=50, quantity=3, tax=5))
```

My answer: 155

Correct answer: 155

### Exercise 5

```python
print(calculate(100, quantity=4, tax=10))
```

My answer: 410

Correct answer: 410

### Exercise 6 — Combined Arguments

```python
def calculate(price, quantity=2, discount=0):
    total = price * quantity
    final = total - discount
    return final

a = calculate(100)
b = calculate(100, 3)
c = calculate(100, discount=20)
d = calculate(price=200, discount=50, quantity=2)
```

My initial answers:

- a = 200
- b = 300
- c = 220
- d = 450

Corrections:

- a = 200
- b = 300
- c = 180
- d = 350

Mistake: I added the discount instead of subtracting it.

### Exercise 7 — Final Test

```python
x = calculate(50, discount=10)
```

My answers:

1. price = 50
2. quantity = 2 (default value)
3. discount = 10
4. Calculation = 100 - 10 = 90

Correct output: 90

---

## 9. Mistakes and Improvements

During the combined argument exercise, I initially made a calculation mistake by adding the discount instead of subtracting it.

I later identified and corrected the mistake.

Important learning:

- Read the function body carefully.
- Follow the operations in their actual order.
- Do not assume that every value is added.
- Check calculations before deciding the output.
- Debugging includes checking logic, not only finding syntax errors.

---

## 10. Day 10 Summary

Concepts learned:

- Function parameters and arguments.
- Default parameters.
- Positional arguments.
- Keyword arguments.
- Combining different argument types.
- Overriding default values.
- Manually tracing function execution.
- Identifying and correcting calculation mistakes.

### Progress

Day 10: COMPLETED

I can now understand how Python assigns arguments to parameters and predict function outputs using default, positional, and keyword arguments.

---

## 11. Practical Coding File

Python practice file:

`src/fundamentals/python/day10_default_parameters.py`

### What the Python File Contains

- A function with default parameters.
- Positional argument examples.
- Keyword argument examples.
- Combined argument examples.
- A final test.
- Printed results.

### Expected Output

```text
NYXARA AI - Day 10
-------------------
Example 1: 200
Example 2: 300
Example 3: 180
Example 4: 350
Final Test: 90
```

### Practical Task — Complete After Running the Code

Run the file:

```bash
python src/fundamentals/python/day10_default_parameters.py
```

Answer these questions in your own words:

1. Did the Python file execute without errors?
2. Did the output match all five expected results: 200, 300, 180, 350, and 90?
3. Which function call uses both default parameter values?
4. Which function call overrides the default quantity?
5. Which function call combines a positional argument with a keyword argument?
6. Why does `calculate(50, discount=10)` use quantity 2?
7. What would happen if you changed `quantity=2` to `quantity=5` in the function definition? Predict the new result of `calculate(50, discount=10)`.

### My Practical Answers

- Execution status:
- Output verification:
- Question 3:
- Question 4:
- Question 5:
- Question 6:
- Question 7:

---

## 12. What to Review Next

Before moving forward, review:

1. Difference between a parameter and an argument.
2. Difference between positional and keyword arguments.
3. How default parameters work.
4. How supplied arguments override default values.
5. How to trace a function line by line.

### Next Lesson

**Day 11 — Python Lists**

Learning objective:

Understand how to store multiple values in one variable, access individual elements, and work with collections of data.
