# Day 12 — Python Dictionaries

## Objective
Understand how to store information using key-value pairs, access and modify dictionary values, remove entries, check keys, and process dictionaries using loops.

---

## 1. What is a Dictionary?

A dictionary stores information using key-value pairs.

Example:

```python
student = {
    "name": "Amal",
    "age": 21,
    "mark": 85
}
```

A dictionary contains:
- Keys: names used to identify information.
- Values: data associated with each key.

Examples:
- `"name"` is a key.
- `"Amal"` is its value.
- `"age"` is a key.
- `21` is its value.

Dictionaries use curly brackets `{}`.

## 2. Accessing Dictionary Values

We access values using their keys.

```python
student = {
    "name": "Amal",
    "age": 21,
    "mark": 85
}

print(student["name"])
print(student["age"])
```

Output:

```text
Amal
21
```

Unlike lists, dictionaries use keys instead of numerical indexes to access values.

## 3. Adding New Values

Assign a value to a new key to add an entry.

```python
student = {
    "name": "Amal",
    "age": 21
}

student["mark"] = 90

print(student)
```

Result:

```python
{
    "name": "Amal",
    "age": 21,
    "mark": 90
}
```

## 4. Updating Existing Values

If the key already exists, assigning a new value updates it.

```python
student = {
    "name": "Amal",
    "age": 21
}

student["age"] = 22

print(student)
```

Result:

```python
{'name': 'Amal', 'age': 22}
```

Remember:
- Existing key: value gets updated.
- New key: new key-value pair gets added.

## 5. Removing Values — pop()

The `pop()` method removes a key and its associated value.

```python
student = {
    "name": "Amal",
    "age": 21,
    "mark": 90
}

student.pop("age")

print(student)
```

Output:

```python
{'name': 'Amal', 'mark': 90}
```

## 6. Checking Whether a Key Exists — in

The `in` operator checks whether a key exists in a dictionary.

```python
student = {
    "name": "Amal",
    "age": 21
}

print("name" in student)
print("mark" in student)
```

Output:

```text
True
False
```

- `"name"` exists, so the result is `True`.
- `"mark"` does not exist, so the result is `False`.

## 7. Finding Dictionary Length — len()

The `len()` function returns the number of key-value pairs.

```python
employee = {
    "name": "Arun",
    "salary": 25000,
    "department": "IT"
}

print(len(employee))
```

Output:

```text
3
```

## 8. Looping Through a Dictionary

### Looping through keys

```python
student = {
    "name": "Amal",
    "age": 21,
    "mark": 90
}

for key in student:
    print(key)
```

Output:

```text
name
age
mark
```

### Looping through keys and values

Use `.items()` to access both together.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Amal
age 21
mark 90
```

Explanation:
- `key` receives the current key.
- `value` receives the corresponding value.
- `.items()` provides key-value pairs.

## 9. Practical Example — Product Inventory

A dictionary can store product information.

```python
product = {
    "name": "Laptop",
    "price": 45000,
    "stock": 5
}

product["stock"] = product["stock"] - 1

print(product["stock"])
```

Output:

```text
4
```

The stock decreases by one when a product is sold.

## 10. Dictionary Loop and Accumulator

Example: Calculate the total quantity of products.

```python
prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

total = 0

for fruit, price in prices.items():
    total = total + price

print(total)
```

Output:

```text
230
```

Second iteration:
- `fruit = "banana"`
- `price = 50`

Mathematical logic:

`total = previous_total + current_value`

## 11. Exercises and User Progress

### Exercise 1 — Accessing Values

```python
product = {
    "name": "Laptop",
    "price": 45000,
    "quantity": 2
}

print(product["name"])
print(product["price"])
print(product["quantity"])
```

User's answers:
1. Laptop — Correct.
2. 45000 — Correct.
3. 2 — Correct.

Score: 3/3.

### Exercise 2 — Adding and Updating

```python
phone = {
    "brand": "Samsung",
    "price": 20000
}

phone["color"] = "Black"
phone["price"] = 25000

print(phone)
```

Correct result:

```python
{
    "brand": "Samsung",
    "price": 25000,
    "color": "Black"
}
```

User understood the logic correctly. A small quotation-mark formatting mistake was corrected.

### Exercise 3 — Removing and Updating

```python
car = {
    "brand": "Toyota",
    "model": "Innova",
    "year": 2025,
    "price": 2000000
}

car.pop("year")
car["price"] = 1800000

print(car)
```

User correctly identified:
- Brand: Toyota.
- Model: Innova.
- Price: 1800000.
- Year: Removed.

### Exercise 4 — Checking Keys and Length

```python
employee = {
    "name": "Arun",
    "salary": 25000,
    "department": "IT"
}

print("salary" in employee)
print("age" in employee)
print(len(employee))
```

User's answers:
1. True — Correct.
2. False — Correct.
3. 3 — Correct.

Score: 3/3.

### Exercise 5 — Dictionary Loop

```python
prices = {
    "apple": 100,
    "banana": 50,
    "orange": 80
}

total = 0

for fruit, price in prices.items():
    total = total + price

print(total)
```

User's answers:
1. Final output: 230 — Correct.
2. Second iteration: banana, 50 — Correct.

Score: 2/2.

### Exercise 6 — Final Inventory Challenge

```python
inventory = {
    "laptop": 5,
    "mouse": 10,
    "keyboard": 8
}

inventory["mouse"] = inventory["mouse"] - 2
inventory["monitor"] = 3

total = 0

for item, quantity in inventory.items():
    total = total + quantity

print(inventory["mouse"])
print("monitor" in inventory)
print(total)
```

User's answers:
1. Mouse quantity: 8 — Correct.
2. `"monitor" in inventory`: True — Correct.
3. Total quantity: 24 — Correct.

Score: 3/3.

---

## 12. Day 12 Progress

Completed:
- Creating dictionaries.
- Understanding keys and values.
- Accessing values using keys.
- Adding new key-value pairs.
- Updating existing values.
- Removing entries using `pop()`.
- Checking key existence using `in`.
- Counting entries using `len()`.
- Looping through dictionaries.
- Using `.items()` to access keys and values.
- Applying dictionaries to product inventory.
- Calculating totals using dictionary loops.

## 13. Important Points to Remember

| Operation | Python |
|---|---|
| Create dictionary | `{}` |
| Access value | `data["key"]` |
| Add value | `data["new_key"] = value` |
| Update value | `data["key"] = new_value` |
| Remove entry | `data.pop("key")` |
| Check key | `"key" in data` |
| Count entries | `len(data)` |
| Loop through keys | `for key in data:` |
| Loop through pairs | `for key, value in data.items():` |

## 14. Connection to NYXARA AI

Dictionaries will be useful in future AI development.

Possible applications:
- Vocabulary-to-token ID mappings.
- Model configuration settings.
- Structured training data.
- Tracking word frequencies.
- Organizing metadata.

Example of a simple vocabulary mapping:

```python
vocabulary = {
    "hello": 0,
    "world": 1,
    "AI": 2
}

print(vocabulary["hello"])
```

Output:

```text
0
```

This is a simple illustration of how a tokenizer could map words to numerical IDs. A real tokenizer also needs rules for splitting text into tokens.

## 15. What to Review Next

- Difference between lists and dictionaries.
- Dictionary keys and values.
- Adding, updating and removing entries.
- Dictionary loops using `.items()`.
- Combining dictionaries with conditions and loops.

**Next lesson:** Day 13 — Python Tuples and Sets.
