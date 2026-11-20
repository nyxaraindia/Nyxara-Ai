# Day 24 – Python Encapsulation

## Learning Objectives

By the end of this lesson, you should understand:

1. What encapsulation means.
2. Why encapsulation is useful.
3. Public attributes.
4. Protected attributes.
5. Private-style attributes.
6. Getters and setters.
7. Data validation.
8. How encapsulation protects important AI model settings.

---

## 1. What Is Encapsulation?

Imagine NYXARA AI has an important setting called `learning_rate`.

The learning rate controls how much a model changes its internal weights during training.

Suppose the correct learning rate is `0.01`.

But someone accidentally changes it to `-500`.

This could cause problems during training.

How can we prevent invalid values from being assigned?

Python provides a concept called Encapsulation.

### Simple Explanation (ELI5)

Imagine a medicine bottle.

You cannot simply take any amount you want. There are instructions and controls.

Encapsulation works similarly. It helps control how important data is accessed and modified.

### Definition

Encapsulation is the practice of keeping data and the methods that operate on that data together, while controlling how that data is accessed or modified.

---

## 2. Public Attributes

A public attribute can be accessed and modified from outside its class.

Example:

```python
class AIModel:
    def __init__(self):
        self.name = "NYXARA"

model = AIModel()

print(model.name)

model.name = "NYXARA-Vision"

print(model.name)
```

Output:

```
NYXARA
NYXARA-Vision
```

### Explanation

- `self.name` creates an attribute.
- `model.name` accesses the attribute.
- `model.name = "NYXARA-Vision"` changes its value.

Public attributes are easy to use, but they do not restrict modification.

---

## 3. Protected Attributes

Python uses a single underscore before an attribute name to indicate that it is intended for internal use.

Example:

```python
class AIModel:
    def __init__(self):
        self._version = "0.1"

model = AIModel()
print(model._version)
```

Output:

```
0.1
```

### Important

The underscore is a convention.

Python does not strictly prevent outside code from accessing `_version`.

It communicates:

"Please treat this attribute as an internal implementation detail."

---

## 4. Private-Style Attributes

Python supports name mangling using two leading underscores.

Example:

```python
class AIModel:
    def __init__(self):
        self.__learning_rate = 0.01

model = AIModel()
print(model.__learning_rate)
```

This produces an AttributeError.

### Why?

Python changes the internal attribute name using name mangling.

Inside the class, `__learning_rate` is internally stored under a name similar to:

`_AIModel__learning_rate`

This makes accidental access or modification from outside the class harder.

### Important

Double underscores do not provide absolute security.

They provide a mechanism to reduce accidental access and name conflicts.

---

## 5. Getters

If an attribute is private-style, how can outside code read its value?

We can create a method called a getter.

Example:

```python
class AIModel:
    def __init__(self):
        self.__learning_rate = 0.01

    def get_learning_rate(self):
        return self.__learning_rate

model = AIModel()
print(model.get_learning_rate())
```

Output:

```
0.01
```

### Explanation

- `__learning_rate` stores the value.
- `get_learning_rate()` provides controlled access.
- `return` sends the value back to the caller.

A getter is a method used to retrieve an attribute's value.

---

## 6. Setters

What if we want to change the learning rate?

We can create a setter.

Example:

```python
class AIModel:
    def __init__(self):
        self.__learning_rate = 0.01

    def get_learning_rate(self):
        return self.__learning_rate

    def set_learning_rate(self, new_rate):
        self.__learning_rate = new_rate

model = AIModel()
model.set_learning_rate(0.05)
print(model.get_learning_rate())
```

Output:

```
0.05
```

### Explanation

- `set_learning_rate()` receives a new value.
- `new_rate` stores the incoming value.
- The method updates the private-style attribute.

A setter is a method used to change an attribute's value.

However, this setter accepts every value.

What if someone enters a negative learning rate?

We need validation.

---

## 7. Validation Inside a Setter

We can check the incoming value before accepting it.

Example:

```python
class AIModel:
    def __init__(self):
        self.__learning_rate = 0.01

    def get_learning_rate(self):
        return self.__learning_rate

    def set_learning_rate(self, new_rate):
        if new_rate > 0:
            self.__learning_rate = new_rate
            print("Learning rate updated!")
        else:
            print("Invalid learning rate!")

model = AIModel()
model.set_learning_rate(0.05)
model.set_learning_rate(-0.5)
print(model.get_learning_rate())
```

Output:

```
Learning rate updated!
Invalid learning rate!
0.05
```

### Step-by-step execution

1. The model starts with learning rate `0.01`.
2. We try to set it to `0.05`.
3. Python checks whether `0.05 > 0`.
4. The condition is true, so the value changes.
5. We try to set it to `-0.5`.
6. Python checks whether `-0.5 > 0`.
7. The condition is false, so the value is rejected.
8. The learning rate remains `0.05`.

This is an example of controlled modification.

---

## 8. Why Encapsulation Matters in NYXARA AI

Imagine an AI model has these settings:

- Learning rate
- Model version
- Training status
- Number of parameters
- Model name

Some values may need controlled modification.

For example:

A learning rate should not accept a negative value.

A model's training status may need to change only through specific methods.

Encapsulation helps organize these controls.

It is useful for:

1. Protecting important application state from accidental changes.
2. Validating incoming values.
3. Keeping implementation details inside classes.
4. Making code easier to maintain.
5. Creating clear interfaces for other parts of a program.

---

## 9. Important Comparison

| Type                 | Python notation | Meaning                                       |
| -------------------- | --------------- | --------------------------------------------- |
| Public               | `name`          | Normal external access                        |
| Protected convention | `_name`         | Intended for internal use                     |
| Private-style        | `__name`        | Name mangling helps prevent accidental access |

Remember:

- Public does not mean unsafe.
- Protected is a naming convention.
- Private-style attributes are not absolutely inaccessible.
- Getters retrieve values.
- Setters modify values.
- Validation checks whether a new value is acceptable.

---

## 10. Day 24 Knowledge Check

### Question 1

What is encapsulation?

A. Creating loops  
B. Controlling access to data through a class  
C. Importing modules  
D. Creating lists

### Question 2

Which is a public attribute?

A. `__name`  
B. `_name`  
C. `name`  
D. `private_name()`

### Question 3

What does a single underscore usually indicate?

A. A public variable  
B. An attribute intended for internal use  
C. A function  
D. A constant

### Question 4

What is the purpose of double underscores before an attribute name?

A. Create a loop  
B. Make an attribute a list  
C. Trigger name mangling  
D. Import a class

### Question 5

What is a getter?

A. A method that retrieves an attribute's value  
B. A method that deletes a class  
C. A loop  
D. A constructor

### Question 6

What is a setter?

A. A method that prints text  
B. A method that changes an attribute's value  
C. A Python package  
D. A list operation

### Question 7

What is the purpose of validation inside a setter?

A. To make the program slower  
B. To prevent all object creation  
C. To check whether an incoming value is acceptable  
D. To delete attributes

### Question 8

What happens when we access a name-mangled attribute using its original double-underscore name from outside the class?

A. It always works  
B. It normally raises AttributeError  
C. Python deletes the class  
D. Python creates a new object

### Question 9

What does `return` do in a getter?

A. Sends a value back to the caller  
B. Stops the computer  
C. Creates a class  
D. Changes the attribute automatically

### Question 10

Why is encapsulation useful in an AI model?

A. It removes the need for training  
B. It makes every attribute inaccessible  
C. It helps control and validate important model settings  
D. It replaces neural networks

---

## 11. Practical Exercise

### Project: NYXARA AI Learning Rate Controller

Create this Python file:

`src/fundamentals/python/day24_encapsulation.py`

### Requirements

Create a class named `AIModel`.

It must contain:

1. An `__init__()` method.
2. A private-style attribute called `__learning_rate`.
3. A getter named `get_learning_rate()`.
4. A setter named `set_learning_rate(new_rate)`.
5. The setter must accept only positive values.
6. Invalid values must be rejected.
7. The original learning rate must remain unchanged when an invalid value is entered.

### Test your class

Create an object with an initial learning rate of `0.01`.

Then:

1. Display the learning rate.
2. Change it to `0.05`.
3. Try changing it to `-0.5`.
4. Display the learning rate again.

### Expected behavior

```
Initial learning rate: 0.01
Learning rate updated!
Invalid learning rate!
Final learning rate: 0.05
```

Try writing the code yourself before looking for a solution.

---

## 12. Day 24 Completion Checklist

- Understand encapsulation.
- Understand public attributes.
- Understand protected attributes.
- Understand private-style attributes.
- Understand getters.
- Understand setters.
- Understand validation.
- Complete the knowledge check with 10/10.
- Complete the practical Python exercise.
- Test the program on Fedora.
- Review mistakes and corrections.

---

## 13. Next Lesson

### Day 25 – Python Inheritance

Topics:

1. What inheritance means.
2. Parent and child classes.
3. Reusing methods.
4. Inheriting attributes.
5. The `super()` function.
6. Method overriding.
7. Types of inheritance.

We will use examples from NYXARA AI and learn each concept slowly, step by step.

---

**Project:** NYXARA AI  
**Course:** Python Fundamentals for AI Development  
**Lesson:** Day 24  
**Topic:** Encapsulation  
**Status:** Teaching completed; practical exercise pending.
