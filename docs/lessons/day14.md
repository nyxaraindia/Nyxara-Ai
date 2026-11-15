# Day 14 – Python Strings and Text Processing

## Learning Objective

Understand Python strings, access individual characters, extract text,
use string methods, and perform basic text processing. These concepts
will prepare us to build a tokenizer for NYXARA AI.

---

## 1. What Is a String?

A string is a sequence of characters (text).

Examples:

```python
name = "Amal"
language = "Python"
message = "Building NYXARA AI"
```

Strings can use single or double quotation marks.

```python
a = 'Hello'
b = "Hello"
```

Both are valid.

Strings can contain:
- Letters
- Numbers
- Spaces
- Symbols
- Special characters

---

## 2. String Indexing

Indexing means accessing an individual character using its position.

Python starts counting from 0.

Example:

```python
word = "PYTHON"

print(word[0])
print(word[1])
print(word[3])
```

Output:

```text
P
Y
H
```

### Index positions

| Character | P | Y | T | H | O | N |
|-----------|---|---|---|---|---|---|
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

Remember:
- First character = index 0
- Second character = index 1
- Third character = index 2

---

## 3. Negative Indexing

Python also allows indexing from the end of a string.

Negative indexing starts at -1.

Example:

```python
word = "PYTHON"

print(word[-1])
print(word[-2])
print(word[-3])
```

Output:

```text
N
O
H
```

### Negative index positions

| Character | P | Y | T | H | O | N |
|-----------|---|---|---|---|---|---|
| Index     | -6 | -5 | -4 | -3 | -2 | -1 |

Remember:
- -1 = Last character
- -2 = Second-last character
- -3 = Third-last character

---

## 4. Finding String Length – len()

The `len()` function counts the number of characters in a string.

Example:

```python
word = "NYXARA"

print(len(word))
```

Output:

```text
6
```

Why?

NYXARA contains six characters.

Spaces are also counted.

Example:

```python
message = "NYXARA AI"
print(len(message))
```

Output:

```text
9
```

---

## 5. String Concatenation

Concatenation means joining strings together.

We use the `+` operator.

Example:

```python
first = "NYXARA"
second = " AI"

result = first + second

print(result)
```

Output:

```text
NYXARA AI
```

Important:

The `+` operator joins strings. It does not perform numerical
addition when both operands are strings.

---

## 6. String Repetition

We can repeat strings using the `*` operator.

Example:

```python
word = "AI"

print(word * 3)
```

Output:

```text
AIAIAI
```

Python repeats the string three times.
It does not automatically insert spaces.

---

## 7. String Immutability

Strings are immutable.

Immutable means that we cannot directly change an individual
character after creating a string.

Example:

```python
word = "PYTHON"

word[0] = "J"

print(word)
```

This produces a TypeError because Python does not allow
direct modification of string characters.

### Creating a new string instead

We can create a new string using the old string.

```python
word = "PYTHON"

word = "J" + word[1:]

print(word)
```

Output:

```text
JYTHON
```

We created a new string and assigned it to the variable.

---

## 8. String Slicing

Slicing means extracting a portion of a string.

Syntax:

```python
string[start:end]
```

Important rules:

- Starting index is included.
- Ending index is excluded.

Example:

```python
word = "PYTHON"

print(word[0:3])
```

Output:

```text
PYT
```

Explanation:

| Index | Character |
|-------|-----------|
| 0 | P |
| 1 | Y |
| 2 | T |
| 3 | H |

Index 3 is excluded.

### Omitting the starting index

```python
word = "NYXARA"

print(word[:3])
```

Output:

```text
NYX
```

Python starts from the beginning.

### Omitting the ending index

```python
word = "NYXARA"

print(word[3:])
```

Output:

```text
ARA
```

Python continues until the end.

---

## 9. Reversing a String

Python provides a slicing technique to reverse strings.

Example:

```python
word = "NYXARA"

print(word[::-1])
```

Output:

```text
ARAXYN
```

Explanation:

The `-1` step tells Python to move backwards through the string.

---

## 10. Changing Letter Case

Python provides two useful string methods.

### upper()

Converts letters to uppercase.

```python
word = "Nyxara Ai"

print(word.upper())
```

Output:

```text
NYXARA AI
```

### lower()

Converts letters to lowercase.

```python
word = "Nyxara Ai"

print(word.lower())
```

Output:

```text
nyxara ai
```

---

## 11. Removing Unwanted Spaces – strip()

The `strip()` method removes spaces from the beginning and end
of a string.

Example:

```python
name = "   Amal   "

print(name.strip())
```

Output:

```text
Amal
```

Important:

`strip()` does not remove spaces between words.

---

## 12. Replacing Text – replace()

The `replace()` method replaces one piece of text with another.

Syntax:

```python
string.replace(old, new)
```

Example:

```python
message = "I love Java"

print(message.replace("Java", "Python"))
```

Output:

```text
I love Python
```

---

## 13. Splitting a String – split()

The `split()` method divides a string into a list.

By default, it separates words using whitespace.

Example:

```python
sentence = "I love NYXARA AI"

words = sentence.split()

print(words)
```

Output:

```python
['I', 'love', 'NYXARA', 'AI']
```

Important:

`split()` converts a string into a list.

---

## 14. Joining Strings – join()

The `join()` method combines strings from a list into one string.

Example:

```python
words = ["I", "love", "NYXARA"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
I love NYXARA
```

The space inside `" "` is used to separate the words.

### Difference

| Method | Result |
|--------|--------|
| split() | String → List |
| join() | List → String |

---

## 15. Membership Checking – in

The `in` operator checks whether a character or word exists
inside a string.

Example:

```python
word = "NYXARA"

print("X" in word)
print("Z" in word)
```

Output:

```text
True
False
```

Explanation:

- X exists in NYXARA.
- Z does not exist in NYXARA.

---

## 16. Practical Example – Text Processing

Let's combine the concepts we learned.

```python
sentence = "  I LOVE NYXARA AI  "

cleaned = sentence.strip()

lowercase = cleaned.lower()

words = lowercase.split()

print(cleaned)
print(lowercase)
print(words)
print(len(words))
```

Output:

```text
I LOVE NYXARA AI
i love nyxara ai
['i', 'love', 'nyxara', 'ai']
4
```

### Step-by-step explanation

1. `strip()` removes spaces from the beginning and end.
2. `lower()` converts the text to lowercase.
3. `split()` divides the sentence into a list of words.
4. `len()` counts the number of words in the list.

---

## 17. Connection to NYXARA AI

Text processing is an important foundation for language models.

A tokenizer converts text into smaller units called tokens.

For example:

Input:

```text
I love NYXARA AI
```

Simple word splitting:

```python
['I', 'love', 'NYXARA', 'AI']
```

This is only a basic word-level splitting example.

A real tokenizer may split words into subwords, characters,
or other token units.

We will develop this concept further in the NYXARA AI project.

---

## 18. Day 14 Exercises and Results

The following exercises were completed during the lesson.

| Exercise | Topic | Result |
|----------|-------|--------|
| 1 | Positive and negative indexing | 4/4 |
| 2 | len() | Correct |
| 3 | Concatenation | Correct |
| 4 | String repetition | Correct |
| 5 | Immutability | Correct |
| 6 | Basic slicing | Correct |
| 7 | Extended slicing | 2/2 |
| 8 | Reverse string | Correct |
| 9 | upper() and lower() | 2/2 |
| 10 | strip() | Correct |
| 11 | replace() | Correct |
| 12 | split() | Correct |
| 13 | join() | Correct |
| 14 | Membership checking | 2/2 |
| 15 | Final text-processing challenge | 4/4 |

---

## 19. Final Challenge

Given:

```python
sentence = "  I LOVE NYXARA AI  "

cleaned = sentence.strip()
lowercase = cleaned.lower()
words = lowercase.split()

print(cleaned)
print(lowercase)
print(words)
print(len(words))
```

User's answers:

```text
I LOVE NYXARA AI
i love nyxara ai
['i', 'love', 'nyxara', 'ai']
4
```

All four final challenge answers were correct.

---

## 20. What I Learned

By completing Day 14, I learned:

- What strings are.
- How positive and negative indexing work.
- How to count characters using `len()`.
- How to join strings using `+`.
- How to repeat strings using `*`.
- Why strings are immutable.
- How to extract text using slicing.
- How to reverse a string.
- How to use `upper()` and `lower()`.
- How to clean text using `strip()`.
- How to replace text.
- How to split and join strings.
- How to check membership using `in`.
- How to perform basic text processing.

---

## 21. Next Lesson

### Day 15 – Practical String Processing and Text Analysis

Planned topics:

- Counting characters and words.
- Counting vowels and consonants.
- Finding specific words.
- Processing text using loops.
- Building simple text-analysis programs.
- Preparing for tokenizer implementation.

**Day 14 Status: COMPLETED**

**Final challenge score: 4/4**

**Overall lesson performance: Excellent.**
