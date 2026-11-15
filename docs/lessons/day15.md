# NYXARA AI – Day 15
# Practical String Processing and Text Analysis

**Course:** Build Your Own AI Model  
**Day:** 15  
**Topic:** Practical String Processing and Text Analysis  
**Status:** COMPLETED  
**Score:** 7/7 (100%)

---

## 1. Learning Objective

The objective of Day 15 is to learn how computers analyse text.

By completing this lesson, I should be able to:

- Count characters in text.
- Count vowels and consonants.
- Count words in a sentence.
- Find how many times a character appears.
- Process text using loops.
- Build a basic text analyser.
- Understand how text processing connects to tokenizers in NYXARA AI.

---

## 2. Why Is Text Processing Important?

Computers process text as data.

For example:

```python
text = "NYXARA AI"
```

A computer can analyse this text in several ways:

- Count its characters.
- Identify individual letters.
- Count repeated letters.
- Separate the text into words.
- Analyse the frequency of characters.

This is an important foundation for Natural Language Processing (NLP) and tokenizer development.

---

## 3. Counting Characters

Python provides the `len()` function to count the number of characters in a string.

```python
text = "NYXARA"
print(len(text))
```

Output:

```
6
```

### Counting Characters Using a Loop

```python
text = "NYXARA"
count = 0

for char in text:
    count = count + 1

print(count)
```

Output:

```
6
```

Explanation:

1. `count = 0` initializes the counter.
2. `for char in text` visits each character.
3. `count = count + 1` increases the counter.
4. `print(count)` displays the final result.

Computational logic:

```
START
    Set count = 0
    Read each character
    Increase count by 1
    Display count
STOP
```

---

## 4. Identifying Vowels and Consonants

For this lesson, the five vowels are:

```
a, e, i, o, u
```

Other English alphabet letters are consonants.

### The `in` Operator

```python
letter = "a"

if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

Output:

```
Vowel
```

### The `lower()` Method

`lower()` converts uppercase letters to lowercase, so one check works for both cases.

```python
letter = "A"
print(letter.lower())
```

Output:

```
a
```

---

## 5. Counting Vowels

```python
text = "NYXARA"
count = 0

for char in text:
    if char.lower() in "aeiou":
        count = count + 1

print(count)
```

Output:

```
2
```

Explanation:

- N → consonant
- Y → consonant
- X → consonant
- A → vowel
- R → consonant
- A → vowel

Therefore, the vowel count is 2.

---

## 6. Counting Consonants

A consonant is an English alphabet letter that is not one of the five vowels.

```python
text = "NYXARA"
count = 0

for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        count += 1

print(count)
```

Output:

```
4
```

Explanation:

- `isalpha()` checks whether a character is a letter.
- `not in` checks that the character is not a vowel.
- `count += 1` increases the counter.

---

## 7. Counting Words Using `split()`

```python
sentence = "I LOVE NYXARA AI"
words = sentence.split()

print(words)
print(len(words))
```

Output:

```
['I', 'LOVE', 'NYXARA', 'AI']
4
```

- `split()` separates a string into a list of words.
- `len()` returns the number of items in the list.

---

## 8. Counting a Specific Character Using `count()`

```python
text = "BANANA"
print(text.count("A"))
```

Output:

```
3
```

---

## 9. Building a Basic Text Analyser

```python
text = "NYXARA AI IS AMAZING"

print("Characters:", len(text))
print("Words:", len(text.split()))
print("A count:", text.count("A"))
```

Output:

```
Characters: 20
Words: 4
A count: 5
```

Note: `len(text)` counts spaces too.

---

## 10. Exercises and Answers

| # | Exercise | My Answer | Result |
|---|----------|-----------|--------|
| 1 | Count characters in `"AI"` | 2 | Correct |
| 2 | Is `"x"` a vowel or consonant? | Consonant | Correct |
| 3 | Count vowels in `"HELLO"` | 2 | Correct |
| 4 | Count consonants in `"NYXARA"` | 4 | Correct |
| 5 | Count words in `"I AM BUILDING NYXARA AI"` | 5 | Correct |
| 6 | Output of `"BANANA".count("A")` | 3 | Correct |
| 7 | Text analyser outputs | 20, 4, 5 | Correct |

**Final Score: 7/7 (100%)**

---

## 11. Mistakes and Corrections

During the lesson, the vowel count for `NYXARA` was first stated incorrectly as 3.

The correct count is 2, because only the two A characters are vowels.

---

## 12. Connection to NYXARA AI

A language model cannot directly understand raw text the way humans do. Text must first be converted into a form the model can process.

A **tokenizer** divides text into smaller units called tokens.

A simple word-based tokenizer might turn:

```
I LOVE NYXARA AI
```

into:

```
["I", "LOVE", "NYXARA", "AI"]
```

Real tokenizers can also split text into subwords or individual characters. Day 15 gives the text-processing foundation needed before studying tokenization.

---

## 13. Day 16 Preview

**Next lesson:** Python Modules and Imports

We will learn:

- What modules are.
- Why programmers organize code into modules.
- How `import` works.
- How to use Python's built-in modules.
- How to create our own Python modules.

These concepts will help us organize the NYXARA AI codebase.

---

## Learning Record

**Project:** NYXARA AI  
**Learning Track:** Python Fundamentals  
**Day:** 15  
**Topic:** Practical String Processing and Text Analysis  
**Score:** 7/7 (100%)  
**Status:** Completed
