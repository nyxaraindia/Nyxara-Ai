# Day 23 — Class Attributes, Instance Attributes and Instance Methods

## Objective

Understand how Python classes store shared information and individual object information.

By the end of this lesson, you should be able to:

- Understand class attributes.
- Understand instance attributes.
- Understand the difference between them.
- Understand instance methods.
- Understand how objects access class attributes.
- Understand attribute shadowing.
- Build a simple NYXARA AI model registry.

---

## 1. Quick revision

In Day 22, we learned:

- Class = Blueprint.
- Object = Instance created from a class.
- Attribute = Information stored in an object.
- Method = Function defined inside a class.
- `self` = Reference to the current object.
- `__init__()` = Initializes an object.

Now imagine NYXARA AI has three model versions:

- NYXARA 0.1
- NYXARA 0.2
- NYXARA 0.5

All these models belong to the same organization.

Instead of storing the organization name separately in every object, Python allows us to define shared information inside a class.

This brings us to class attributes.

---

## 2. What is a class attribute?

A class attribute is a variable defined directly inside a class, outside its methods.

It belongs to the class and is shared by its instances unless an instance overrides it.

Example:

```python
class AIModel:

    organization = "NYXARA INDIA"

model1 = AIModel()
model2 = AIModel()

print(model1.organization)
print(model2.organization)
```

Expected output:

```text
NYXARA INDIA
NYXARA INDIA
```

Explanation:

- `organization` is defined directly inside the class.
- It is not inside `__init__()`.
- Both objects can access it.
- Both objects see the same class attribute unless they override it.

**ELI5:**

Imagine three employees working in the same company.

Each employee has an individual name, but all employees share the same company name.

The company name is like a class attribute.

---

## 3. What is an instance attribute?

An instance attribute belongs to an individual object.

It is commonly created using `self` inside `__init__()`.

Example:

```python
class AIModel:

    def __init__(self, version):
        self.version = version

model1 = AIModel("0.1")
model2 = AIModel("0.2")

print(model1.version)
print(model2.version)
```

Expected output:

```text
0.1
0.2
```

Explanation:

- `self.version` creates an instance attribute.
- `model1` stores version `0.1`.
- `model2` stores version `0.2`.
- Each object has its own version.

**ELI5:**

Two students attend the same school.

They share the same school, but each student has a different name.

The individual name is like an instance attribute.

---

## 4. Class attributes vs instance attributes

Understand the difference:

| Class attribute | Instance attribute |
|---|---|
| Defined directly inside a class | Usually defined using `self` |
| Shared by instances | Belongs to an individual object |
| Can be accessed through the class | Accessed through an object |
| Useful for common information | Useful for individual information |

Example:

```python
class AIModel:

    organization = "NYXARA INDIA"

    def __init__(self, version):
        self.version = version

model1 = AIModel("0.1")
model2 = AIModel("0.2")

print(model1.organization)
print(model1.version)

print(model2.organization)
print(model2.version)
```

Expected output:

```text
NYXARA INDIA
0.1
NYXARA INDIA
0.2
```

Notice:

- Organization is shared.
- Version is individual.

---

## 5. Accessing class attributes using the class name

We can access a class attribute directly through the class.

Example:

```python
class AIModel:

    organization = "NYXARA INDIA"

print(AIModel.organization)
```

Expected output:

```text
NYXARA INDIA
```

This is useful because we do not need to create an object just to access a class attribute.

Remember:

```python
AIModel.organization
```

Accesses the class attribute through the class.

```python
model1.organization
```

Accesses the attribute through an object.

---

## 6. What happens when a class attribute changes?

Suppose we have two objects.

```python
class AIModel:

    organization = "NYXARA INDIA"

model1 = AIModel()
model2 = AIModel()

AIModel.organization = "NYXARA RESEARCH"

print(model1.organization)
print(model2.organization)
```

Expected output:

```text
NYXARA RESEARCH
NYXARA RESEARCH
```

Why?

Because we changed the class attribute itself.

Both objects that rely on that class attribute now see the updated value.

---

## 7. What is attribute shadowing?

Attribute shadowing happens when an instance attribute has the same name as a class attribute.

Example:

```python
class AIModel:

    organization = "NYXARA INDIA"

model1 = AIModel()
model2 = AIModel()

model1.organization = "OTHER ORGANIZATION"

print(model1.organization)
print(model2.organization)
print(AIModel.organization)
```

Expected output:

```text
OTHER ORGANIZATION
NYXARA INDIA
NYXARA INDIA
```

Understand what happened:

1. The class has an attribute called `organization`.
2. Both objects initially access that class attribute.
3. We assign a new value to `model1.organization`.
4. Python creates an instance attribute for `model1`.
5. That instance attribute takes priority when `model1.organization` is accessed.
6. The class attribute remains unchanged.

Important:

Changing an instance attribute does not automatically change the class attribute.

---

## 8. What is an instance method?

An instance method is a function defined inside a class that works with an object.

It normally receives `self` as its first parameter.

Example:

```python
class AIModel:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Model:", self.name)

model1 = AIModel("NYXARA")

model1.display()
```

Expected output:

```text
Model: NYXARA
```

Explanation:

- `display()` is an instance method.
- `self` refers to the current object.
- `self.name` accesses that object's name.
- `model1.display()` calls the method for `model1`.

---

## 9. Combining class attributes, instance attributes and methods

Let's build a simple NYXARA AI model registry.

```python
class AIModel:

    organization = "NYXARA INDIA"

    def __init__(self, name, version, parameters):
        self.name = name
        self.version = version
        self.parameters = parameters

    def display_info(self):
        print("Organization:", self.organization)
        print("Model:", self.name)
        print("Version:", self.version)
        print("Parameters:", self.parameters)


model1 = AIModel("NYXARA", "0.1", 1000000)
model2 = AIModel("NYXARA", "0.2", 5000000)

model1.display_info()
print()
model2.display_info()
```

Expected output:

```text
Organization: NYXARA INDIA
Model: NYXARA
Version: 0.1
Parameters: 1000000

Organization: NYXARA INDIA
Model: NYXARA
Version: 0.2
Parameters: 5000000
```

Our class contains:

- Class attribute: `organization`
- Instance attributes: `name`, `version`, `parameters`
- Instance method: `display_info()`

---

## 10. Important warning about mutable class attributes

Be careful when using mutable objects such as lists and dictionaries as class attributes.

Example:

```python
class AIModel:

    experiments = []

model1 = AIModel()
model2 = AIModel()

model1.experiments.append("Experiment 1")

print(model2.experiments)
```

Output:

```text
['Experiment 1']
```

Why?

Because both objects are accessing the same class-level list.

If every object needs its own list, create it inside `__init__()`:

```python
class AIModel:

    def __init__(self):
        self.experiments = []

model1 = AIModel()
model2 = AIModel()

model1.experiments.append("Experiment 1")

print(model1.experiments)
print(model2.experiments)
```

Expected output:

```text
['Experiment 1']
[]
```

Important:

- A class attribute containing an immutable value, such as a string, is often useful for shared information.
- A mutable class attribute, such as a list, is shared and can cause unexpected behavior.
- Use instance attributes when each object needs its own mutable data.

---

## 11. Why this matters for NYXARA AI

A growing AI project may contain several model versions.

For example:

| Model | Parameters |
|---|---:|
| NYXARA 0.1 | 1,000,000 |
| NYXARA 0.2 | 5,000,000 |
| NYXARA 0.5 | 100,000,000 |
| NYXARA 1.0 | 1,000,000,000 |

We can represent these models as objects.

Shared information:

- Organization name
- Project identity
- Common configuration

Individual information:

- Model version
- Parameter count
- Training status
- Model-specific settings

This helps organize a growing codebase.

---

## 12. Common mistakes

### Mistake 1: Defining a class attribute inside __init__()

Example:

```python
class AIModel:

    def __init__(self):
        self.organization = "NYXARA INDIA"
```

This creates an instance attribute, not a class attribute.

A class attribute is defined directly inside the class:

```python
class AIModel:

    organization = "NYXARA INDIA"
```

### Mistake 2: Assuming instance changes affect every object

Example:

```python
model1.organization = "OTHER"
```

This does not change the class attribute.

It creates or updates an instance attribute for `model1`.

### Mistake 3: Sharing a mutable list unintentionally

Avoid this when each object needs its own list:

```python
class AIModel:
    experiments = []
```

Prefer:

```python
class AIModel:

    def __init__(self):
        self.experiments = []
```

### Mistake 4: Forgetting self in an instance method

Incorrect:

```python
def display():
    print("NYXARA")
```

Correct:

```python
def display(self):
    print("NYXARA")
```

---

## 13. Exercises

Try these exercises yourself before checking any solution.

### Exercise 1 — Create a class attribute

Create an `AIModel` class.

Add a class attribute:

`organization = "NYXARA INDIA"`

Create two objects and print their organization.

### Exercise 2 — Create instance attributes

Add an `__init__()` method that accepts:

- name
- version

Store both using `self`.

Create two objects with different versions.

### Exercise 3 — Compare attributes

Print:

- `model1.organization`
- `model1.version`
- `model2.organization`
- `model2.version`

Identify which values are shared and which are individual.

### Exercise 4 — Change the class attribute

Change the organization using:

`AIModel.organization = "NYXARA RESEARCH"`

Print the organization using both objects.

### Exercise 5 — Test attribute shadowing

Set:

`model1.organization = "OTHER ORGANIZATION"`

Print:

- `model1.organization`
- `model2.organization`
- `AIModel.organization`

Explain why the values are different.

### Exercise 6 — Build a model registry

Create a class called `AIModel` with:

Class attribute:
- organization = "NYXARA INDIA"

Instance attributes:
- name
- version
- parameters

Instance method:
- `display_info()`

Create these three objects:

| Name | Version | Parameters |
|---|---|---:|
| NYXARA | 0.1 | 1,000,000 |
| NYXARA | 0.2 | 5,000,000 |
| NYXARA | 0.5 | 100,000,000 |

Display the information for all three objects.

---

## 14. Quiz review

1. What is a class attribute?
2. What is an instance attribute?
3. Where is a class attribute normally defined?
4. Where are instance attributes commonly created?
5. Are class attributes shared by instances?
6. Can different objects have different instance attribute values?
7. What happens when we change a class attribute through the class name?
8. What happens when we assign an instance attribute with the same name as a class attribute?
9. What is an instance method?
10. Why can a mutable class attribute cause unexpected behavior?

---

## 15. Day 23 completion checklist

- [ ] Understand class attributes.
- [ ] Understand instance attributes.
- [ ] Understand their differences.
- [ ] Access class attributes through the class.
- [ ] Access attributes through objects.
- [ ] Understand class attribute changes.
- [ ] Understand attribute shadowing.
- [ ] Understand instance methods.
- [ ] Understand mutable class attributes.
- [ ] Complete all exercises.
- [ ] Complete the quiz.

---

## Key takeaway

Remember:

- Class attribute = Shared information defined directly inside a class.
- Instance attribute = Individual information belonging to an object.
- Instance method = Function that works with an object using `self`.
- Attribute shadowing = An instance attribute takes priority over a class attribute with the same name.
- Mutable class attributes = Shared mutable data that can affect multiple objects.

**Day 23 topic: Class Attributes, Instance Attributes and Instance Methods.**
