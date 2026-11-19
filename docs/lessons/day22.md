# Day 22 — Python Classes and Objects

## Objective

Understand Object-Oriented Programming (OOP), classes and objects.

By the end of this lesson, you should be able to:

- Understand what a class is.
- Understand what an object is.
- Create a class in Python.
- Create objects from a class.
- Understand attributes and methods.
- Understand `self`.
- Understand the `__init__()` method.
- Build a simple AI model representation.

---

## 1. What is Object-Oriented Programming?

Imagine we are developing NYXARA AI.

We may need to represent several AI models:

- NYXARA 0.1
- NYXARA 0.2
- NYXARA 0.5
- NYXARA 1.0

Every model has information:

- Name
- Version
- Number of parameters

Every model may also perform actions:

- Display model information.
- Start training.
- Evaluate performance.

Instead of creating separate variables and functions for every model, we can organize related information and actions together.

This programming approach is called Object-Oriented Programming (OOP).

**ELI5:**

Think about a house blueprint.

A blueprint describes how a house should be built.

The actual houses built using that blueprint are individual houses.

In programming:

- Class = Blueprint.
- Object = Actual thing created from the blueprint.

---

## 2. What is a class?

A class is a blueprint used to create objects.

Example:

```python
class AIModel:
    pass
```

Explanation:

- `class` is the Python keyword used to define a class.
- `AIModel` is the class name.
- `pass` means do nothing for now.

We have created a class, but it does not contain any functionality yet.

---

## 3. What is an object?

An object is an instance of a class.

Example:

```python
class AIModel:
    pass

model1 = AIModel()
model2 = AIModel()

print(model1)
print(model2)
```

Here:

- `AIModel` is the class.
- `model1` is an object.
- `model2` is another object.

Both objects are created from the same class.

Think:

One blueprint can create many houses.

Similarly, one class can create many objects.

---

## 4. What are attributes?

Attributes are variables that store information about an object.

For an AI model, attributes may include:

- Name
- Version
- Parameters

Example:

```python
class AIModel:
    pass

model1 = AIModel()

model1.name = "NYXARA"
model1.version = "0.1"
model1.parameters = 1000000

print(model1.name)
print(model1.version)
print(model1.parameters)
```

Expected output:

```text
NYXARA
0.1
1000000
```

Explanation:

- `model1.name` stores the model name.
- `model1.version` stores its version.
- `model1.parameters` stores its parameter count.

Each object can have its own attribute values.

---

## 5. What is a method?

A method is a function defined inside a class.

A normal function exists independently.

A method belongs to a class and is generally called through its object.

Example:

```python
class AIModel:

    def display_info(self):
        print("NYXARA AI Model")

model1 = AIModel()

model1.display_info()
```

Expected output:

```text
NYXARA AI Model
```

Explanation:

- `def` defines a function.
- `display_info` is the method name.
- `self` refers to the current object.
- `model1.display_info()` calls the method using the object.

---

## 6. Understanding self

`self` is one of the most important concepts in Python classes.

ELI5:

Imagine two students:

- Student A has a name.
- Student B has a different name.

When Student A accesses their information, Python needs to know which student is being referred to.

`self` tells Python which object is currently working.

Example:

```python
class AIModel:

    def display(self):
        print(self)

model1 = AIModel()
model2 = AIModel()

model1.display()
model2.display()
```

The output shows different object representations.

Why?

Because:

- When `model1.display()` runs, `self` refers to `model1`.
- When `model2.display()` runs, `self` refers to `model2`.

Important:

You normally do not pass `self` manually.

Python passes the object automatically when you call an instance method.

---

## 7. What is __init__()?

`__init__()` is a special method called automatically when an object is created.

It is commonly used to initialize an object's attributes.

Example:

```python
class AIModel:

    def __init__(self, name, version):
        self.name = name
        self.version = version

model1 = AIModel("NYXARA", "0.1")

print(model1.name)
print(model1.version)
```

Expected output:

```text
NYXARA
0.1
```

Understand the process:

1. Python creates the object.
2. Python automatically calls `__init__()`.
3. The supplied values are received as arguments.
4. `self.name` stores the name inside the object.
5. `self.version` stores the version inside the object.

Important:

`__init__()` is commonly called a constructor by beginners, but technically it initializes an already-created object. Object creation itself is handled by `__new__()`.

---

## 8. Creating multiple objects

One class can create multiple objects with different information.

Example:

```python
class AIModel:

    def __init__(self, name, version, parameters):
        self.name = name
        self.version = version
        self.parameters = parameters

model1 = AIModel("NYXARA", "0.1", 1000000)
model2 = AIModel("NYXARA", "0.2", 5000000)
model3 = AIModel("NYXARA", "0.5", 100000000)

print(model1.name, model1.version, model1.parameters)
print(model2.name, model2.version, model2.parameters)
print(model3.name, model3.version, model3.parameters)
```

Expected output:

```text
NYXARA 0.1 1000000
NYXARA 0.2 5000000
NYXARA 0.5 100000000
```

Notice:

- All objects use the same class.
- Each object stores its own values.
- Changing one object's attributes does not automatically change the others.

---

## 9. Combining attributes and methods

Now let's build a more complete AIModel class.

```python
class AIModel:

    def __init__(self, name, version, parameters):
        self.name = name
        self.version = version
        self.parameters = parameters

    def display_info(self):
        print("Model:", self.name)
        print("Version:", self.version)
        print("Parameters:", self.parameters)

model1 = AIModel("NYXARA", "0.1", 1000000)

model1.display_info()
```

Expected output:

```text
Model: NYXARA
Version: 0.1
Parameters: 1000000
```

Our class now contains:

- Attributes: name, version, parameters.
- Method: display_info().
- Initialization method: __init__().

This is a basic example of organizing data and behavior together.

---

## 10. Why OOP matters for NYXARA AI

As NYXARA AI grows, we may need to represent many components:

- AI models
- Neural network layers
- Datasets
- Training sessions
- Optimizers
- Evaluation results

Classes can help organize these components.

For example:

```python
class Dataset:
    pass

class NeuralNetwork:
    pass

class Trainer:
    pass

class AIModel:
    pass
```

Each class can later contain its own attributes and methods.

OOP helps organize large programs, but it does not automatically make a program intelligent or faster.

---

## 11. Common mistakes

### Mistake 1: Forgetting parentheses when creating an object

Incorrect:

```python
model1 = AIModel
```

Correct:

```python
model1 = AIModel()
```

The first statement refers to the class itself.

The second creates an object.

### Mistake 2: Forgetting self in an instance method

Incorrect:

```python
class AIModel:

    def display_info():
        print("NYXARA")
```

Correct:

```python
class AIModel:

    def display_info(self):
        print("NYXARA")
```

### Mistake 3: Forgetting self when storing attributes

Incorrect:

```python
def __init__(self, name):
    name = name
```

Correct:

```python
def __init__(self, name):
    self.name = name
```

The correct version stores the value as an object attribute.

### Mistake 4: Calling an attribute that does not exist

Example:

```python
class AIModel:
    pass

model1 = AIModel()

print(model1.name)
```

This produces an AttributeError because `name` was never created.

---

## 12. Exercises

Try these exercises yourself before checking any solution.

### Exercise 1 — Create a class

Create a class called `AIModel`.

Use `pass` inside it initially.

### Exercise 2 — Create objects

Create two objects:

- model1
- model2

Both must come from the `AIModel` class.

### Exercise 3 — Add attributes

Give the objects these attributes:

model1:
- name = NYXARA
- version = 0.1

model2:
- name = NYXARA
- version = 0.2

Print their names and versions.

### Exercise 4 — Use __init__()

Create a new `AIModel` class with an `__init__()` method.

It should accept:

- name
- version
- parameters

Store all three using `self`.

### Exercise 5 — Create a method

Add a method called `display_info()`.

It should display:

- Model name
- Version
- Parameters

Create one object and call the method.

### Exercise 6 — Build a model registry

Create three objects:

| Model | Version | Parameters |
|---|---|---:|
| NYXARA | 0.1 | 1,000,000 |
| NYXARA | 0.2 | 5,000,000 |
| NYXARA | 0.5 | 100,000,000 |

Call `display_info()` for all three objects.

---

## 13. Quiz review

1. What is a class?
2. What is an object?
3. What is the difference between a class and an object?
4. What are attributes?
5. What is a method?
6. What does `self` represent?
7. When is `__init__()` called?
8. What is the purpose of `__init__()`?
9. Can one class create multiple objects?
10. Can different objects have different attribute values?

---

## 14. Day 22 completion checklist

- [ ] Understand Object-Oriented Programming.
- [ ] Understand classes.
- [ ] Understand objects.
- [ ] Create a class.
- [ ] Create multiple objects.
- [ ] Understand attributes.
- [ ] Understand methods.
- [ ] Understand self.
- [ ] Understand __init__().
- [ ] Complete the exercises.
- [ ] Complete the quiz.

---

## Key takeaway

Remember:

- Class = Blueprint.
- Object = Instance created from a class.
- Attribute = Information stored in an object.
- Method = Function defined inside a class.
- self = Reference to the current object.
- __init__() = Special method used to initialize an object.

**Day 22 topic: Python Classes and Objects.**
