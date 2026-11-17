# Day 20 — Python File Handling: Advanced Concepts

## 1. Learning Objective

Today we will learn advanced file-handling concepts.

By the end of this lesson, you should understand:

- File paths.
- Current working directory.
- Checking whether a file or directory exists.
- Checking whether a path is a file or directory.
- Creating directories.
- Reading files line by line.
- Removing unnecessary whitespace.
- Counting lines and words.
- Handling file-related errors.
- Inspecting datasets for NYXARA AI.

---

## 2. What Is a File Path?

A file path tells Python where a file is located.

Imagine your computer has this structure:

```text
NYXARA AI/
|
|-- dataset.txt
|
|-- docs/
|   |
|   |-- lessons/
|       |
|       |-- day20.md
|
|-- src/
    |
    |-- fundamentals/
        |
        |-- python/
            |
            |-- day20_dataset_inspector.py
```

Examples of file paths:

```text
"dataset.txt"
"docs/lessons/day20.md"
"src/fundamentals/python/day20_dataset_inspector.py"
```

A path can be:

### Relative Path

A relative path describes a location relative to the current working directory.

Example:

```text
"dataset.txt"
```

### Absolute Path

An absolute path gives the complete location of a file.

Example:

```text
"/run/media/amalkaji/AMAL/E/NYXARA/Nyxara AI/dataset.txt"
```

Important:

The correct path depends on where your Python program is running.

---

## 3. Current Working Directory

Python provides `os.getcwd()` to find the current working directory.

Example:

```python
import os

current_location = os.getcwd()
print(current_location)
```

Possible output:

```text
/run/media/amalkaji/AMAL/E/NYXARA/Nyxara AI
```

Explanation:

- `import os` imports Python's operating-system utilities.
- `os.getcwd()` gets the current working directory.
- `print()` displays the location.

Why is this useful?

It helps us understand where Python is looking for relative file paths.

---

## 4. Checking Whether a Path Exists

Python provides:

```python
os.path.exists()
```

Example:

```python
import os

if os.path.exists("dataset.txt"):
    print("Dataset exists")
else:
    print("Dataset not found")
```

Possible output:

```text
Dataset exists
```

Or:

```text
Dataset not found
```

`os.path.exists()` returns a Boolean:

- `True` means the path exists.
- `False` means the path does not exist.

Important:

It checks both files and directories.

---

## 5. Checking Whether a Path Is a File or Directory

Python provides two useful methods.

### os.path.isfile()

Checks whether a path points to a file.

Example:

```python
import os

if os.path.isfile("dataset.txt"):
    print("This is a file")
else:
    print("This is not a file")
```

### os.path.isdir()

Checks whether a path points to a directory.

Example:

```python
import os

if os.path.isdir("docs"):
    print("This is a directory")
else:
    print("This is not a directory")
```

Difference:

| Method             | Purpose                          |
| ------------------ | -------------------------------- |
| `os.path.exists()` | Checks whether a path exists     |
| `os.path.isfile()` | Checks whether it is a file      |
| `os.path.isdir()`  | Checks whether it is a directory |

---

## 6. Creating Directories

A directory is another name for a folder.

Python provides `os.mkdir()` to create one directory.

Example:

```python
import os

os.mkdir("NYXARA_DATA")
```

This creates a folder named:

```text
NYXARA_DATA/
```

Important:

`os.mkdir()` raises `FileExistsError` if that directory already exists.

### Creating Nested Directories

Use `os.makedirs()` to create nested directories.

Example:

```python
import os

os.makedirs("NYXARA_DATA/training/text")
```

This creates:

```text
NYXARA_DATA/
|
|-- training/
    |
    |-- text/
```

### What Is exist_ok=True?

Example:

```python
import os

os.makedirs("NYXARA_DATA", exist_ok=True)
```

Explanation:

- If the directory does not exist, Python creates it.
- If the directory already exists, Python does not raise an error.

This is useful when running a program multiple times.

---

## 7. Reading a File Line by Line

Imagine a dataset contains thousands of lines.

Instead of loading everything at once, we can process one line at a time.

Example:

```python
with open("fruits.txt", "r") as file:
    for line in file:
        print(line)
```

If the file contains:

```text
Apple
Mango
Orange
Banana
```

Output:

```text
Apple

Mango

Orange

Banana
```

Why are there extra blank lines?

Each line read from the file may already contain a newline character (`\n`).

The `print()` function adds another newline.

We can fix this using `strip()`.

Example:

```python
with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Output:

```text
Apple
Mango
Orange
Banana
```

### What Does strip() Do?

`strip()` removes whitespace from the beginning and end of a string.

It also removes newline characters at the ends.

Example:

```python
text = "  NYXARA AI\n"
clean_text = text.strip()
print(clean_text)
```

Output:

```text
NYXARA AI
```

Important:

`strip()` does not modify the original file.

It returns a cleaned string.

---

## 8. Counting Lines in a File

We can count the number of lines using a loop.

Example:

```python
line_count = 0

with open("fruits.txt", "r") as file:
    for line in file:
        line_count += 1

print("Total lines:", line_count)
```

Explanation:

- `line_count = 0` starts the counter.
- The loop reads one line at a time.
- `line_count += 1` increases the counter for every line.
- `print()` displays the total.

If the file contains four lines:

```text
Total lines: 4
```

This technique is called counting with an accumulator.

---

## 9. Counting Words in a File

We can count words using `split()` and `len()`.

Example:

```python
with open("dataset.txt", "r") as file:
    content = file.read()

words = content.split()
word_count = len(words)

print("Total words:", word_count)
```

Explanation:

- `read()` reads the entire file as a string.
- `split()` separates the text into words using whitespace by default.
- `len()` counts the items in the resulting list.

Example:

```python
text = "NYXARA AI is learning"
words = text.split()

print(words)
print(len(words))
```

Output:

```text
['NYXARA', 'AI', 'is', 'learning']
4
```

Important:

This is a simple whitespace-based word count, not a complete linguistic tokenizer.

---

## 10. split() vs splitlines()

These methods perform different jobs.

### split()

Separates text into parts, using whitespace by default.

Example:

```python
text = "NYXARA AI is learning"
print(text.split())
```

Output:

```text
['NYXARA', 'AI', 'is', 'learning']
```

### splitlines()

Separates text into individual lines.

Example:

```python
text = "NYXARA AI\nPython\nMachine Learning"
lines = text.splitlines()
print(lines)
```

Output:

```text
['NYXARA AI', 'Python', 'Machine Learning']
```

Difference:

| Method         | Result                         |
| -------------- | ------------------------------ |
| `split()`      | List of words or text segments |
| `splitlines()` | List of lines                  |

---

## 11. Handling File-Related Errors

Sometimes a file operation can fail.

Python provides exceptions to describe these problems.

### FileNotFoundError

Occurs when a file does not exist and we try to open it in read mode.

Example:

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

Output:

```text
File not found!
```

### PermissionError

Occurs when Python does not have permission to access a file or directory.

Example:

```python
try:
    with open("protected.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Permission denied!")
except FileNotFoundError:
    print("File not found!")
```

Important:

These exceptions can be handled separately because they describe different problems.

---

## 12. Inspecting a NYXARA AI Dataset

Imagine NYXARA AI has a text dataset.

File: `dataset.txt`

Contents:

```text
Artificial intelligence is interesting.
Python is useful for machine learning.
NYXARA AI is an independent AI project.
```

We can inspect the dataset using Python.

Example:

```python
import os

filename = "dataset.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    print("Dataset inspection")
    print("------------------")
    print("Total lines:", len(lines))
    print("Total words:", len(words))
else:
    print("Dataset not found!")
```

Possible output:

```text
Dataset inspection
------------------
Total lines: 3
Total words: 15
```

Why is this useful?

Before preparing training data, we need to inspect and understand it.

This example performs basic inspection only. Real dataset preparation also needs cleaning, validation, deduplication, encoding checks, and other processing.

---

## 13. Complete Example — NYXARA AI Dataset Inspector

Create this Python file:

`src/fundamentals/python/day20_dataset_inspector.py`

Program:

```python
import os

filename = "dataset.txt"

# Step 1: Check whether the dataset exists
if os.path.exists(filename):
    try:
        # Step 2: Open and read the dataset
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Separate lines and words
        lines = content.splitlines()
        words = content.split()

        # Step 4: Count lines and words
        line_count = len(lines)
        word_count = len(words)

        # Step 5: Display the results
        print("NYXARA AI Dataset Inspector")
        print("---------------------------")
        print("Total lines:", line_count)
        print("Total words:", word_count)

    except PermissionError:
        print("Permission denied!")
else:
    print("Dataset not found!")
```

Note:

The program checks whether the file exists before opening it, so the `else` branch handles a missing dataset. The `PermissionError` handler covers the case where the file exists but cannot be read.

---

## 14. Important Concepts to Remember

| Concept             | Purpose                                         |
| ------------------- | ----------------------------------------------- |
| `os.getcwd()`       | Gets current working directory                  |
| `os.path.exists()`  | Checks whether a path exists                    |
| `os.path.isfile()`  | Checks whether a path is a file                 |
| `os.path.isdir()`   | Checks whether a path is a directory            |
| `os.mkdir()`        | Creates one directory                           |
| `os.makedirs()`     | Creates directories, including nested ones      |
| `exist_ok=True`     | Avoids an error if the directory already exists |
| `strip()`           | Removes whitespace from both ends               |
| `split()`           | Separates text into parts                       |
| `splitlines()`      | Separates text into lines                       |
| `len()`             | Counts items                                    |
| `FileNotFoundError` | File does not exist                             |
| `PermissionError`   | Access is not permitted                         |

---

## 15. Day 20 Quiz

Answer each question to check your understanding.

### Question 1

What does `os.getcwd()` return?

A. Current working directory.

B. Current Python version.

C. Current filename.

D. Current username.

### Question 2

What does `os.path.exists("dataset.txt")` check?

A. Whether the path exists.

B. Whether the file is empty.

C. Whether the file contains numbers.

D. Whether the file is open.

### Question 3

What is the difference between `os.path.isfile()` and `os.path.isdir()`?

A. One checks files and the other checks directories.

B. Both delete files.

C. Both create directories.

D. There is no difference.

### Question 4

What does this code do?

```python
os.makedirs("NYXARA_DATA", exist_ok=True)
```

A. Creates the directory if needed and avoids an error if it already exists.

B. Deletes the directory.

C. Creates a text file.

D. Reads a dataset.

### Question 5

What does `line.strip()` do?

A. Removes whitespace from the beginning and end of the line.

B. Deletes the entire line from the file.

C. Converts the line into an integer.

D. Counts the characters in the line.

### Question 6

What happens when we use this code?

```python
for line in file:
    print(line)
```

A. Reads the file one line at a time.

B. Deletes every line.

C. Reads only the last line.

D. Counts the number of files.

### Question 7

What does `.split()` do?

A. Converts the string into a list of words by default.

B. Converts the string into an integer.

C. Deletes all words.

D. Counts the number of characters.

### Question 8

What does `len(words)` return?

```python
words = ["NYXARA", "AI", "is", "learning"]
print(len(words))
```

A. 4 — the number of items in the list.

B. 20 — the total number of characters.

C. 1 — the number of lists.

D. 0 — because the list is empty.

### Question 9

What error occurs when Python tries to open a file that does not exist in read mode (`"r"`)?

A. FileNotFoundError

B. ZeroDivisionError

C. TypeError

D. IndexError

### Question 10

What is the purpose of `exist_ok=True`?

A. Avoids an error if the directory already exists.

B. Deletes the directory if it exists.

C. Creates a text file.

D. Checks whether a file is empty.

---

## 16. Practical Exercise — NYXARA AI Dataset Inspector

Create this file:

`src/fundamentals/python/day20_dataset_inspector.py`

### Your task

Build a program that:

1. Imports `os`.
2. Checks whether `dataset.txt` exists.
3. If it does not exist, displays `Dataset not found!`.
4. If it exists, opens it in read mode.
5. Reads all the content.
6. Counts the total number of lines.
7. Counts the total number of words.
8. Displays both counts.

### Hints

Use these concepts:

```python
import os
os.path.exists()
open()
.read()
.splitlines()
.split()
len()
```

### Expected output

Suppose `dataset.txt` contains:

```text
Artificial intelligence is interesting.
Python is useful for machine learning.
NYXARA AI is an independent AI project.
```

Expected output:

```text
NYXARA AI Dataset Inspector
---------------------------
Total lines: 3
Total words: 15
```

Try writing the code independently before looking for a complete solution.

---

## 17. Day 20 Completion Checklist

- Understand relative and absolute paths.
- Use `os.getcwd()`.
- Use `os.path.exists()`.
- Use `os.path.isfile()`.
- Use `os.path.isdir()`.
- Create directories using `os.mkdir()`.
- Create nested directories using `os.makedirs()`.
- Understand `exist_ok=True`.
- Read files line by line.
- Understand `strip()`.
- Count lines.
- Count words.
- Understand `split()` and `splitlines()`.
- Handle `FileNotFoundError`.
- Understand `PermissionError`.
- Complete the Dataset Inspector exercise.
- Complete the Day 20 quiz.

---

## 18. Next Lesson

**Day 21 — Python JSON and Structured Data**

Next, we will learn:

- What JSON is.
- JSON objects and arrays.
- Python dictionaries and JSON.
- `json.load()` and `json.dump()`.
- Reading JSON files.
- Writing JSON files.
- Saving structured configuration for NYXARA AI.

---

## 19. Day 20 Progress

**Topic:** Advanced Python File Handling

**Quiz Score:** 10/10 (100%)

**Quiz Status:** Completed

**Practical Exercise:** Pending

**Next:** Day 21 — Python JSON and Structured Data.
