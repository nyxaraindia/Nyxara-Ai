# Day 13 — Python Tuples and Sets

## Objective

Understand Python tuples and sets, learn how they differ from lists and dictionaries, and use them to store fixed collections and unique values.

---

## 1. Quick Revision — Lists

A list stores multiple values in one variable.

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
```

Output:

```text
Apple
```

List characteristics:
- Uses square brackets `[]`.
- Allows duplicate values.
- Supports indexing.
- Mutable: elements can be changed.

Example:

```python
fruits[0] = "Mango"
print(fruits)
```

Output:

```text
['Mango', 'Banana', 'Orange']
```

---

## 2. What is a Tuple?

A tuple stores multiple values that cannot be modified after creation.

Tuples use parentheses `()`.

Example:

```python
birth_date = (15, 8, 2005)

print(birth_date)
```

Output:

```text
(15, 8, 2005)
```

A tuple is useful when information should remain fixed.

Examples:
- Coordinates.
- Birth dates.
- Fixed configuration values.

## 3. Accessing Tuple Elements

Tuples support indexing just like lists.

Python indexing starts at 0.

```python
colors = ("Red", "Blue", "Green", "Yellow")

print(colors[0])
print(colors[1])
print(colors[3])
```

Output:

```text
Red
Blue
Yellow
```

We can also use `len()` to count elements.

```python
print(len(colors))
```

Output:

```text
4
```

## 4. Mutable vs Immutable

### Mutable

Mutable means something can be changed after creation.

Lists are mutable.

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

### Immutable

Immutable means something cannot be changed after creation.

Tuples are immutable.

```python
numbers = (10, 20, 30)

numbers[1] = 100

print(numbers)
```

This produces a `TypeError`.

Why?

Because Python does not allow modification of tuple elements.

Remember:

- List = Mutable.
- Tuple = Immutable.

---

## 5. What is a Set?

A set stores unique values.

It automatically removes duplicate elements.

Sets use curly brackets `{}`.

Example:

```python
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
```

Output (order may vary):

```text
{10, 20, 30, 40}
```

Set characteristics:
- Stores unique values.
- Automatically removes duplicates.
- Does not support indexing.
- Can be modified.
- Uses curly brackets `{}`.

Important: An empty set must be created using `set()`, because `{}` creates an empty dictionary.

Example:

```python
empty_set = set()
```

## 6. Removing Duplicates from a List

We can convert a list into a set.

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output (order may vary):

```text
{10, 20, 30, 40}
```

This is useful when data contains repeated values.

## 7. Checking Values in a Set

Use the `in` operator to check whether a value exists.

```python
numbers = {5, 10, 15, 20}

print(15 in numbers)
print(25 in numbers)
```

Output:

```text
True
False
```

- 15 exists, so the result is True.
- 25 does not exist, so the result is False.

## 8. Adding Elements to a Set

Use the `add()` method.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

Output (order may vary):

```text
{10, 20, 30, 40}
```

If we add an existing value, the set remains unchanged.

```python
numbers.add(20)

print(numbers)
```

The set still contains only one occurrence of 20.

## 9. Removing Elements from a Set

Use the `remove()` method.

```python
numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)
```

Output (order may vary):

```text
{10, 30, 40}
```

Important:
- `remove(value)` raises a `KeyError` if the value does not exist.
- `discard(value)` removes a value if present, but does not raise an error if it is missing.

Example:

```python
numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)
```

Output:

```text
{10, 20, 30}
```

## 10. Comparing List, Tuple, Set and Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Brackets | `[]` | `()` | `{}` | `{}` |
| Ordered | Yes | Yes | No guaranteed positional order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No duplicate elements | Keys must be unique |
| Indexing | Yes | Yes | No | Access by key |
| Purpose | Collection | Fixed collection | Unique values | Key-value pairs |

Examples:

```python
my_list = [10, 20, 30]

my_tuple = (10, 20, 30)

my_set = {10, 20, 30}

my_dictionary = {
    "age": 21,
    "mark": 90
}
```

---

## 11. Practical Example — NYXARA AI Vocabulary

Imagine NYXARA AI receives repeated words from a dataset.

```python
words = ["AI", "Python", "AI", "Learning", "Python", "Model"]

unique_words = set(words)

print(len(unique_words))
print("AI" in unique_words)
print("Java" in unique_words)
```

Output:

```text
4
True
False
```

Unique words:
- AI
- Python
- Learning
- Model

This demonstrates how sets can help identify unique words.

A real tokenizer requires additional text-processing rules, but unique-value handling is one useful concept.

---

## 12. Exercises and User Progress

### Exercise 1 — Tuple Indexing

```python
colors = ("Red", "Blue", "Green", "Yellow")

print(colors[1])
print(colors[3])
print(len(colors))
```

User's answers:

1. Blue — Correct.
2. Yellow — Correct.
3. 4 — Correct.

Score: 3/3.

### Exercise 2 — Set Operations

```python
numbers = {5, 10, 5, 15, 10, 20}

print(len(numbers))
print(15 in numbers)
print(25 in numbers)
```

Unique values: `{5, 10, 15, 20}`

User's answers:

1. 4 — Correct.
2. True — Correct.
3. False — Correct.

Score: 3/3.

### Exercise 3 — NYXARA AI Vocabulary Challenge

```python
words = ["AI", "Python", "AI", "Learning", "Python", "Model"]

unique_words = set(words)

print(len(unique_words))
print("AI" in unique_words)
print("Java" in unique_words)
```

User's answers:

1. 4 — Correct.
2. True — Correct.
3. False — Correct.

Score: 3/3.

---

## 13. Day 13 Progress

Completed:

- Understanding tuples.
- Creating tuples using parentheses.
- Accessing tuple elements using indexes.
- Using `len()` with tuples.
- Understanding mutable and immutable data.
- Understanding sets.
- Removing duplicates automatically.
- Converting lists into sets.
- Checking membership using `in`.
- Adding elements using `add()`.
- Removing elements using `remove()`.
- Understanding `discard()`.
- Comparing lists, tuples, sets and dictionaries.
- Applying sets to unique vocabulary in NYXARA AI.

## 14. Important Points to Remember

- Lists use `[]` and are mutable.
- Tuples use `()` and are immutable.
- Sets use `{}` and store unique values.
- Sets do not support indexing.
- `set()` creates an empty set.
- `add()` inserts an element into a set.
- `remove()` removes an element and raises an error if missing.
- `discard()` removes an element without raising an error if missing.
- `in` checks whether an element exists.
- `len()` counts elements.

## 15. What to Review Next

- Difference between lists, tuples and sets.
- Mutable vs immutable.
- Set duplicate removal.
- Set membership checking.
- Choosing the correct data structure for a problem.

**Next lesson: Day 14 — Python Strings and String Operations.**
