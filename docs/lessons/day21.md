# Day 21 — JSON and Structured Data

## Objective

Understand how Python stores structured information and how to exchange data using JSON.

By the end of this lesson, you should be able to:
- Understand what JSON is.
- Understand JSON objects and arrays.
- Connect JSON data with Python dictionaries and lists.
- Convert Python data into JSON.
- Convert JSON into Python data.
- Read and write JSON files.

---

## 1. What is structured data?

Imagine NYXARA AI has the following information:

- Model name: NYXARA
- Version: 0.1
- Parameters: 1,000,000
- Training status: True

This information has different values and types.

Instead of storing everything separately, we can organize it into a structured format.

Structured data means arranging information in a predictable organization.

---

## 2. What is JSON?

JSON means JavaScript Object Notation.

It is a text-based format used to store and exchange structured data.

Example:

```json
{
    "name": "NYXARA",
    "version": "0.1",
    "parameters": 1000000,
    "training": true
}
```

Understand the structure:

| JSON part | Meaning |
|---|---|
| `{ }` | Object |
| `"name"` | Key |
| `"NYXARA"` | String value |
| `1000000` | Number |
| `true` | Boolean |

JSON is commonly used by APIs, applications, configuration files and data pipelines.

---

## 3. JSON and Python data types

Python and JSON use similar data structures.

| JSON | Python |
|---|---|
| Object `{}` | Dictionary `dict` |
| Array `[]` | List `list` |
| String | String `str` |
| Number | Integer or float |
| true | True |
| false | False |
| null | None |

Important:

JSON uses lowercase `true`, `false`, and `null`.

Python uses `True`, `False`, and `None`.

---

## 4. Creating structured data in Python

Example:

```python
model = {
    "name": "NYXARA",
    "version": "0.1",
    "parameters": 1000000,
    "training": True
}

print(model)
```

Here:

- `model` is a dictionary.
- Each key describes a piece of information.
- Each value stores the actual information.

Access values:

```python
print(model["name"])
print(model["version"])
print(model["parameters"])
```

Expected output:

```text
NYXARA
0.1
1000000
```

---

## 5. The json module

Python provides a built-in module named `json`.

We import it like this:

```python
import json
```

The JSON module helps convert Python data into JSON and JSON into Python data.

There are four important functions.

| Function | Purpose |
|---|---|
| `json.dumps()` | Python data → JSON string |
| `json.dump()` | Python data → JSON file |
| `json.loads()` | JSON string → Python data |
| `json.load()` | JSON file → Python data |

Remember the difference between `s` and no `s`.

- `dumps` and `loads` work with strings.
- `dump` and `load` work with files.

---

## 6. Python dictionary to JSON string

We use `json.dumps()`.

```python
import json

model = {
    "name": "NYXARA",
    "version": "0.1",
    "parameters": 1000000
}

json_data = json.dumps(model)

print(json_data)
print(type(json_data))
```

Expected output:

```text
{"name": "NYXARA", "version": "0.1", "parameters": 1000000}
<class 'str'>
```

Important:

`json.dumps()` returns a string, not a dictionary.

We can make the JSON output easier to read:

```python
json_data = json.dumps(model, indent=4)

print(json_data)
```

The `indent=4` argument adds indentation.

---

## 7. JSON string to Python dictionary

We use `json.loads()`.

```python
import json

json_data = '{"name": "NYXARA", "version": "0.1"}'

model = json.loads(json_data)

print(model)
print(type(model))
```

Expected output:

```text
{'name': 'NYXARA', 'version': '0.1'}
<class 'dict'>
```

Understand the process:

1. JSON text is stored in `json_data`.
2. `json.loads()` converts that text into Python data.
3. The resulting value is a Python dictionary.

---

## 8. Writing JSON into a file

Suppose we want to save NYXARA model information permanently.

We use `json.dump()`.

```python
import json

model = {
    "name": "NYXARA",
    "version": "0.1",
    "parameters": 1000000,
    "training": True
}

with open("model.json", "w") as file:
    json.dump(model, file, indent=4)

print("Model information saved!")
```

Explanation:

- `open()` creates or opens the file.
- `"w"` opens it in write mode.
- `json.dump()` writes the dictionary as JSON.
- `indent=4` makes the file readable.
- `with` automatically closes the file.

The file `model.json` will contain:

```json
{
    "name": "NYXARA",
    "version": "0.1",
    "parameters": 1000000,
    "training": true
}
```

---

## 9. Reading JSON from a file

We use `json.load()`.

```python
import json

with open("model.json", "r") as file:
    model = json.load(file)

print(model)
print(model["name"])
print(model["parameters"])
```

Expected output:

```text
{'name': 'NYXARA', 'version': '0.1', 'parameters': 1000000, 'training': True}
NYXARA
1000000
```

Important:

`json.load()` reads the JSON file and converts its contents into Python data.

---

## 10. Nested JSON data

JSON can contain objects inside other objects and arrays.

Example:

```json
{
    "model": {
        "name": "NYXARA",
        "version": "0.1"
    },
    "languages": ["English", "Malayalam", "Hindi"],
    "active": true
}
```

Python equivalent:

```python
model = {
    "model": {
        "name": "NYXARA",
        "version": "0.1"
    },
    "languages": ["English", "Malayalam", "Hindi"],
    "active": True
}
```

Access nested information:

```python
print(model["model"]["name"])
print(model["languages"][0])
```

Expected output:

```text
NYXARA
English
```

Understand:

- `model["model"]` accesses the inner dictionary.
- `["name"]` accesses the name inside it.
- `model["languages"][0]` accesses the first list element.

---

## 11. Why JSON matters for NYXARA AI

A model development project needs to store structured information.

For example:

- Model configuration
- Training settings
- Dataset information
- Experiment results
- Model version details
- Evaluation results

JSON can store this information in a readable format.

Example configuration:

```json
{
    "model_name": "NYXARA",
    "version": "0.1",
    "learning_rate": 0.001,
    "batch_size": 16,
    "epochs": 10
}
```

Python can read this configuration and use its values during a training experiment.

JSON is a data format. It does not train the AI model by itself.

---

## 12. Common mistakes

### Mistake 1: Confusing dump and dumps

Incorrect:

```python
json_data = json.dump(model)
```

Correct for a JSON string:

```python
json_data = json.dumps(model)
```

### Mistake 2: Confusing load and loads

Use:

```python
json.loads(json_text)
```

when you have a JSON string.

Use:

```python
json.load(file)
```

when you have an open JSON file.

### Mistake 3: Using Python Boolean values in JSON text

Incorrect JSON:

```json
{
    "active": True
}
```

Correct JSON:

```json
{
    "active": true
}
```

### Mistake 4: Forgetting quotation marks around JSON keys

Incorrect:

```json
{
    name: "NYXARA"
}
```

Correct:

```json
{
    "name": "NYXARA"
}
```

---

## 13. Exercises

Try these exercises yourself before checking the answers.

### Exercise 1 — Create a dictionary

Create a Python dictionary called `model` with:

- name: NYXARA
- version: 0.1
- parameters: 1000000
- active: True

Print the model name and version.

### Exercise 2 — Convert to JSON

Import the JSON module.

Convert your dictionary into a JSON string using `json.dumps()`.

Print the JSON string.

### Exercise 3 — Convert back

Use `json.loads()` to convert the JSON string back into a Python dictionary.

Print its type.

### Exercise 4 — Save a file

Save the model dictionary into a file named `nyxara.json` using `json.dump()`.

Use indentation of 4.

### Exercise 5 — Read a file

Read `nyxara.json` using `json.load()`.

Print the model name and parameter count.

---

## 14. Quiz review

1. What does JSON stand for?
2. Which Python data type represents a JSON object?
3. Which Python data type represents a JSON array?
4. Which function converts Python data into a JSON string?
5. Which function converts a JSON string into Python data?
6. Which function writes Python data into a JSON file?
7. Which function reads a JSON file into Python data?
8. What is the difference between `json.dump()` and `json.dumps()`?
9. What is the difference between `json.load()` and `json.loads()`?
10. Why is JSON useful in an AI project?

---

## 15. Day 21 completion checklist

- [ ] Understand structured data.
- [ ] Understand JSON objects and arrays.
- [ ] Understand JSON and Python type mapping.
- [ ] Use `json.dumps()`.
- [ ] Use `json.loads()`.
- [ ] Use `json.dump()`.
- [ ] Use `json.load()`.
- [ ] Understand nested JSON.
- [ ] Complete all exercises.
- [ ] Complete the quiz.

---

## Key takeaway

JSON is a common format for organizing and exchanging structured information.

Remember these four functions:

- `dumps()` — Python data to JSON string.
- `dump()` — Python data to JSON file.
- `loads()` — JSON string to Python data.
- `load()` — JSON file to Python data.

**Day 21 topic: JSON and Structured Data — Completed.**
