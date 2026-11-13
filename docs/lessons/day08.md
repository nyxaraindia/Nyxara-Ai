# Day 8 — Python Functions: Reusable Code

## Learning objective

By the end of this lesson, you should be able to define and call a Python function, distinguish parameters from arguments, and use `return` to send a result back to the calling code.

## 1. What is a function?

A function is a named, reusable group of instructions. Instead of writing the same instructions repeatedly, define them once and call the function whenever needed.

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

The function executes twice because it is called twice.

## 2. Parameters and arguments

- **Parameters** are the names written inside the parentheses in the function definition. In `def multiply(a, b):`, the parameters are `a` and `b`.
- **Arguments** are the actual values supplied when calling the function. In `multiply(4, 5)`, the arguments are `4` and `5`.

The parameters receive the argument values when the function is called.

## 3. `print()` versus `return`

`print()` displays information on the screen. `return` sends a value back to the code that called the function.

Consider:

```python
def add(a, b):
    result = a + b
    print(result)

answer = add(5, 3)
print(answer)
```

The first print displays `8`. The function has no explicit `return`, so Python returns `None` automatically. The final print displays `None`. This is not an error.

With `return`:

```python
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)
```

Output:

```text
8
```

## 4. Using returned values

```python
def calculate(x):
    return x * 2

a = calculate(5)
b = calculate(10)

print(a)
print(b)
print(a + b)
```

Output:

```text
10
20
30
```

Reasoning:
- `calculate(5)` returns `10`, which is stored in `a`.
- `calculate(10)` returns `20`, which is stored in `b`.
- `a + b` is `30`.

A returned value can also be passed directly into another function:

```python
def square(number):
    return number * number

print(square(4))
```

Output: `16`.

## 5. Independent coding challenge — completed

**Task:** Write a function named `calculate_total` that accepts `price` and `quantity`, multiplies them, returns the total, and then prints the result for price `50` and quantity `4`.

Student's completed code (confirmed in the VS Code screenshot):

```python
def calculate_total(price,quantity):
    return price*quantity

total=calculate_total(50,4)
print(f'Total={total}')
```

Output confirmed:

```text
Total=200
```

The solution is correct. A style improvement is to add spaces after commas and around operators:

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(50, 4)
print(f'Total={total}')
```

## 6. Terminal troubleshooting

The student initially tried to run the file using a path with extra quotation marks and a literal `...`, then mistyped the filename as `day08_calulate_total.py`.

The file was present at:

`src/fundamentals/python/day08_calculate_total.py`

From the project root, the correct command was:

```bash
python src/fundamentals/python/day08_calculate_total.py
```

The command ran successfully and displayed `Total=200`.

**Learning point:** A correct Python program still cannot run if the command points to the wrong file path or filename.

## 7. Progress and understanding

- Correctly predicted the outputs `20` and `21` from two function calls.
- Explained that `a` and `b` receive values supplied by the function call; learned the precise terms *parameters* and *arguments*.
- Initially thought a function without `return` would cause an error. Corrected this: it returns `None` automatically.
- Correctly reasoned that `calculate(5)` returns `10`, `calculate(10)` returns `20`, and their sum is `30`.
- Independently wrote and ran the `calculate_total` function successfully.

## 8. What to review next

Before moving on, make sure you can explain these without memorising:
1. What is the difference between a parameter and an argument?
2. What is the difference between `print()` and `return`?
3. What does Python return when a function has no explicit `return`?
4. How can a returned value be stored and used in another calculation?

**Next lesson:** Build confidence with functions through multiple parameters, local variables, and small independent problem-solving exercises. Continue at a pace guided by understanding.
