# Day 19 — Python File Handling

## 1. Learning Objective

Today we will learn how Python works with files.

By the end of this lesson, you should understand:

- What file handling means.
- How to open files.
- How to read files.
- How to write files.
- How to append content.
- How to use different file modes.
- Why the `with open()` statement is useful.
- How to handle missing files.
- How file handling helps NYXARA AI.

---

## 2. What Is File Handling?

Imagine you are writing notes in a notebook.

You can:

1. Create a notebook.
2. Write information.
3. Read information.
4. Add more information.
5. Close the notebook.

Python can perform similar operations with computer files.

This process is called **File Handling**.

Examples of files:

- notes.txt
- dataset.txt
- training_data.txt
- model_config.json

For NYXARA AI, file handling is important because we need to store and read training data.

---

## 3. Opening a File

Python provides the `open()` function.

Syntax:

```python
open("filename", "mode")
```

Example:

```python
file = open("notes.txt", "r")
```

Explanation:

- `open()` opens a file.
- `"notes.txt"` is the filename.
- `"r"` means read mode.
- `file` stores the opened file object.

Important:

Opening a file does not automatically display its contents.

We need to use a reading method.

---

## 4. File Modes

A file mode tells Python what operation we want to perform.

| Mode  | Meaning                       |
| ----- | ----------------------------- |
| `"r"` | Read a file                   |
| `"w"` | Write to a file               |
| `"a"` | Append content                |
| `"x"` | Create a new file exclusively |

### Read Mode — r

Used to read an existing file.

```python
file = open("notes.txt", "r")
```

If the file does not exist, Python raises `FileNotFoundError`.

### Write Mode — w

Used to write content into a file.

```python
file = open("notes.txt", "w")
file.write("Learning Python")
file.close()
```

Important:

If the file already contains information, `"w"` overwrites its existing content.

If the file does not exist, Python creates it.

### Append Mode — a

Used to add new content at the end of a file.

```python
file = open("notes.txt", "a")
file.write("\nBuilding NYXARA AI")
file.close()
```

Important:

Append mode preserves existing content.

If the file does not exist, Python creates it.

### Exclusive Create Mode — x

Used to create a new file.

```python
file = open("new_notes.txt", "x")
file.write("My first file")
file.close()
```

Important:

If the filename already exists, Python raises `FileExistsError`.

---

## 5. Reading a File

Python provides several methods for reading file content.

### read()

Reads the entire file content as a string.

Example:

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

If the file contains:

```
Learning Python
Building NYXARA AI
```

Output:

```
Learning Python
Building NYXARA AI
```

### readline()

Reads one line at a time.

Example:

```python
file = open("notes.txt", "r")
first_line = file.readline()
print(first_line)
file.close()
```

Output:

```
Learning Python
```

### readlines()

Reads all lines and returns them as a list.

Example:

```python
file = open("notes.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

Output:

```
['Learning Python\n', 'Building NYXARA AI']
```

Notice:

Each line may contain `\n`, which represents a newline character.

---

## 6. Closing a File

After working with a file, we should close it.

Example:

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

Why close a file?

- Releases system resources.
- Helps prevent unnecessary file access.
- Ensures the file is properly closed.

---

## 7. The with open() Statement

Python provides a better way to work with files.

Example:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

Explanation:

- `with` manages the file automatically.
- `open()` opens the file.
- `as file` gives the opened file a variable name.
- The indented statements work with the file.
- Python automatically closes the file when the block finishes.

This means we do not need to write `file.close()` manually.

**Recommended:** Use `with open()` in most file-handling programs.

---

## 8. Writing with with open()

Example:

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")
```

Python automatically closes the file after the indented block finishes.

Appending:

```python
with open("notes.txt", "a") as file:
    file.write("\nBuilding NYXARA AI")
```

Reading:

```python
with open("notes.txt", "r") as file:
    content = file.read()

print(content)
```

---

## 9. Handling FileNotFoundError

What happens if we try to read a file that does not exist?

Example:

```python
with open("missing.txt", "r") as file:
    content = file.read()
```

Python raises:

```
FileNotFoundError
```

We can handle this using `try` and `except`.

Example:

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
```

Now the program handles the error instead of stopping with an unhandled exception.

---

## 10. File Handling in NYXARA AI

Imagine NYXARA AI has a training dataset.

File:

`training_data.txt`

Contents:

```
Artificial intelligence is interesting.
Python is useful for machine learning.
NYXARA AI is an independent AI project.
```

Python can read the dataset:

```python
with open("training_data.txt", "r") as file:
    dataset = file.read()

print(dataset)
```

The variable `dataset` now contains the text.

Why is this important?

A language model needs training data.

A simplified data pipeline looks like this:

```
Text Files
    |
    v
Python File Handling
    |
    v
Read Training Data
    |
    v
Text Processing
    |
    v
Tokenization
    |
    v
Training Data Preparation
```

This is a simplified example of one part of an AI data pipeline.

Real training pipelines involve additional processing, validation, batching, and other steps.

---

## 11. Complete Example — NYXARA Notes Manager

The following program demonstrates writing, appending, and reading.

```python
# Save the first note
with open("nyxara_notes.txt", "w") as file:
    first_note = input("Enter first note: ")
    file.write(first_note + "\n")

# Add another note
with open("nyxara_notes.txt", "a") as file:
    second_note = input("Enter second note: ")
    file.write(second_note + "\n")

# Read all saved notes
with open("nyxara_notes.txt", "r") as file:
    saved_notes = file.read()

print("\nSaved notes:")
print(saved_notes)
```

Example output:

```
Enter first note: Learning Python
Enter second note: Building NYXARA AI

Saved notes:
Learning Python
Building NYXARA AI
```

---

## 12. Important Concepts to Remember

| Concept             | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| `open()`            | Opens a file                                         |
| `read()`            | Reads the entire file                                |
| `readline()`        | Reads one line                                       |
| `readlines()`       | Reads all lines into a list                          |
| `write()`           | Writes content                                       |
| `"r"`               | Read mode                                            |
| `"w"`               | Write and overwrite                                  |
| `"a"`               | Append content                                       |
| `"x"`               | Create a new file exclusively                        |
| `close()`           | Closes a file                                        |
| `with open()`       | Automatically closes a file                          |
| `FileNotFoundError` | File does not exist when opening for reading         |
| `FileExistsError`   | File already exists when using exclusive create mode |

---

## 13. Day 19 Quiz

Answer each question to check your understanding.

### Question 1

Which mode is used to read a file?

A. `"w"`

B. `"r"`

C. `"a"`

D. `"x"`

### Question 2

What happens when we open an existing file using `"w"`?

A. Reads the file.

B. Appends new content.

C. Overwrites the existing content.

D. Deletes the filename.

### Question 3

Which method reads the entire file as a string?

A. `read()`

B. `readline()`

C. `readlines()`

D. `close()`

### Question 4

What is the purpose of `"a"` mode?

A. Read content.

B. Add content at the end.

C. Delete content.

D. Create a directory.

### Question 5

What does `readlines()` return?

A. An integer.

B. A dictionary.

C. A list of lines.

D. A Boolean.

### Question 6

What is the main benefit of `with open()`?

A. Automatically closes the file.

B. Deletes the file.

C. Converts text into numbers.

D. Creates a folder.

### Question 7

Which error occurs when we try to read a file that does not exist?

A. TypeError

B. ValueError

C. FileNotFoundError

D. IndexError

### Question 8

Which mode creates a file but raises an error if it already exists?

A. `"r"`

B. `"w"`

C. `"a"`

D. `"x"`

### Question 9

What does `file.readline()` do?

A. Reads one line.

B. Reads all lines.

C. Deletes one line.

D. Counts all words.

### Question 10

Why is file handling useful for NYXARA AI?

A. It helps store and read training data.

B. It automatically trains a model.

C. It creates a GPU.

D. It automatically creates neural networks.

---

## 14. Practical Exercise — NYXARA AI Notes Manager

Create this Python file:

`src/fundamentals/python/day19_file_handling.py`

### Your task

Build a notes manager that:

1. Asks the user for the first note.
2. Saves the first note using `"w"` mode.
3. Asks for a second note.
4. Appends the second note using `"a"` mode.
5. Reads the saved notes using `"r"` mode.
6. Displays all saved notes.

### Expected output

```
Enter first note: Learning Python
Enter second note: Building NYXARA AI

Saved notes:

Learning Python
Building NYXARA AI
```

### Hints

- Use `input()` to collect notes.
- Use `with open()` to work with files.
- Use `file.write()` to save content.
- Use `"\n"` to move to a new line.
- Use `file.read()` to read the saved notes.

Try writing the program independently before looking for a complete solution.

---

## 15. Day 19 Completion Checklist

- Understand file handling.
- Understand file modes.
- Use `open()`.
- Read files with `read()`.
- Read one line with `readline()`.
- Read multiple lines with `readlines()`.
- Write files with `"w"`.
- Append files with `"a"`.
- Understand `"x"` mode.
- Use `with open()`.
- Handle `FileNotFoundError`.
- Complete the Notes Manager practical exercise.
- Complete the Day 19 quiz.

---

## 16. Next Lesson

**Day 20 — Python File Handling: Advanced Concepts**

Next, we will learn:

- Working with file paths.
- Checking whether files exist.
- Creating directories.
- Reading files line by line.
- Counting lines and words.
- Handling file-related errors.
- Inspecting datasets for NYXARA AI.

**Day 19 Status:** Quiz completed — 10/10 (100%).

Practical exercise: Pending.
