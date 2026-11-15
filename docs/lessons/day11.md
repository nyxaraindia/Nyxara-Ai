# Day 11 — Python Lists

## Objective
Understand how to store multiple values in a single variable, access and modify elements, use list methods, and process lists using loops.

---

## 1. What is a List?

A list stores multiple values inside one variable.

Example:

```python
marks = [85, 90, 75, 95, 80]
```

- Square brackets `[]` create a list.
- Commas separate elements.
- Each value is called an element.
- Lists can store multiple values.

## 2. List Indexing

Every element has an index.
Python indexing starts from 0.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[2])  # 30
print(numbers[4])  # 50
```

| Index | Value |
|---|---|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |
| 4 | 50 |

## 3. Modifying List Elements

Lists are mutable, which means their elements can be changed.

```python
fruits = ["Apple", "Banana", "Orange", "Mango"]

fruits[1] = "Grapes"
fruits[3] = "Pineapple"

print(fruits)
```

Output:

```text
['Apple', 'Grapes', 'Orange', 'Pineapple']
```

## 4. Adding Elements — append()

The `append()` method adds an element to the end of a list.

```python
numbers = [10, 20, 30]

numbers.append(40)
numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

## 5. Finding List Length — len()

The `len()` function returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

Output:

```text
5
```

## 6. Removing Elements

### remove()

Removes the first matching value.

```python
numbers = [10, 20, 30, 40, 50]

numbers.remove(30)

print(numbers)
```

Output:

```text
[10, 20, 40, 50]
```

### pop()

Removes an element using its index.

```python
numbers = [10, 20, 30, 40, 50]

numbers.pop(0)

print(numbers)
```

Output:

```text
[20, 30, 40, 50]
```

## 7. Looping Through a List

A `for` loop can visit every element in a list.

```python
prices = [100, 200, 300]

for price in prices:
    print(price * 2)
```

Output:

```text
200
400
600
```

The loop executes three times because the list contains three elements.

## 8. Accumulator — Calculating a Total

An accumulator stores a running result.

```python
prices = [100, 200, 300, 400]

total = 0

for price in prices:
    total = total + price

print(total)
```

Output:

```text
1000
```

### Understanding the logic

| Iteration | Price | Total |
|---|---:|---:|
| Start | - | 0 |
| 1 | 100 | 100 |
| 2 | 200 | 300 |
| 3 | 300 | 600 |
| 4 | 400 | 1000 |

Why initialize `total = 0`?

- We need a starting value for addition.
- Zero does not change the result.
- Without initialization, Python cannot use the variable before it has a value.

Mathematical logic:

`total = previous_total + current_price`

## 9. Exercises and Progress

### Exercise 1 — Indexing

```python
numbers = [10, 20, 30, 40, 50]
```

User correctly identified:
- First element: 10
- Third element: 30
- Fifth element: 50

### Exercise 2 — Modifying Elements

```python
fruits = ["Apple", "Banana", "Orange", "Mango"]
fruits[1] = "Grapes"
fruits[3] = "Pineapple"
```

Correct result:

```text
['Apple', 'Grapes', 'Orange', 'Pineapple']
```

### Exercise 3 — append() and len()

```python
numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)
```

User correctly identified:
- Final length: 5

### Exercise 4 — remove() and pop()

```python
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
numbers.pop(0)
```

Correct result:

```text
[20, 40, 50]
```

Length: 3

### Exercise 5 — Looping

```python
prices = [100, 200, 300]

for price in prices:
    print(price * 2)
```

Correct output:

```text
200
400
600
```

- Number of iterations: 3
- Second iteration value of `price`: 200

### Exercise 6 — Accumulator

```python
numbers = [5, 10, 15, 20]

total = 0

for number in numbers:
    total = total + number

print(total)
```

User's answers:
1. Final output: 50 — Correct.
2. Total after second iteration: 15 — Correct.
3. Why initialize total to 0? Because addition needs a starting value. Starting from 1 would add an unwanted extra 1 — Correct.

---

## 10. Day 11 Progress

Completed:
- Creating lists.
- Accessing elements using indexes.
- Modifying list elements.
- Adding elements using `append()`.
- Counting elements using `len()`.
- Removing elements using `remove()` and `pop()`.
- Looping through lists.
- Calculating totals using accumulators.

## 11. Important Points to Remember

- Lists use square brackets `[]`.
- Indexing starts at 0.
- Lists are mutable.
- `append()` adds an element.
- `remove()` removes a matching value.
- `pop()` removes an element by index.
- `len()` counts elements.
- A `for` loop processes list elements.
- An accumulator stores a running result.

## 12. What to Review Next

- List indexing and modification.
- List methods.
- Looping through lists.
- Accumulator logic.
- Calculating totals and averages.

**Next lesson:** Day 12 — Python Dictionaries.
