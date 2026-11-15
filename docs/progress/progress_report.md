# NYXARA AI — Python Learning Progress Report

**Learning Programme:** Build Your Own AI Model  
**Student:** NYXARA AI Project Learner  
**Report Period:** Day 1 to Day 13  
**Current Stage:** Python Fundamentals  
**Report Status:** Day 13 Completed  
**Next Lesson:** Day 14 — Python Strings and String Operations

---

# 1. Overall Performance

## Overall Learning Score: 89/100

| Measurement | Result |
|---|---:|
| Lessons completed | 13 |
| Lessons remaining in current stage | Ongoing |
| Recorded scored answers correct | 52 |
| Recorded scored answers incorrect | 0 |
| Provisional day assessments | 7 |
| Overall estimated score | 89/100 |
| Overall status | Excellent progress |

### Score calculation

The assessment uses 10 points per completed learning day.

Six days have recorded numerical exercises with all recorded answers correct.

Seven other days have been assessed provisionally based on demonstrated understanding, completed exercises and coding work.

| Assessment group | Points earned | Maximum points |
|---|---:|---:|
| Days 2, 4, 5, 11, 12, 13 | 60 | 60 |
| Days 1, 3, 6, 7, 8, 9, 10 | 56 | 70 |
| Total | 116 | 130 |

Calculation:

116 / 130 × 100 = 89.23%

**Rounded overall score: 89/100**

Important: This is an estimated learning-progress score, not a standardized examination result. Provisional scores are based on available learning evidence and should be validated through a comprehensive practical examination.

---

# 2. Day-by-Day Learning Record

## Day 1 — Understanding Computers and Logic

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- What is a computer?
- Input, processing and output.
- Computational thinking.
- Logical decisions.
- TRUE and FALSE.
- Algorithms.
- Pseudocode.
- IF and ELSE logic.
- Dry-running algorithms.

### Demonstrated understanding
- Created a marks-based pass/fail algorithm.
- Understood decision-making logic.
- Identified that a marks threshold of 40 should allow exactly 40 to pass when using an inclusive condition.
- Applied logic to a shopping purchase decision.

### Review
- Writing algorithms independently.
- Converting real-world problems into pseudocode.
- Flowchart development.

---

## Day 2 — Conditions and Decision Logic

**Status:** Completed  
**Score:** 10/10

### Topics covered
- Comparison operators.
- Assignment versus equality.
- AND, OR and NOT.
- IF and ELSE.
- Multiple conditions.
- Range checking.

### Assessment
Quiz: 5/5.

### Demonstrated understanding
- Correctly answered all five recorded quiz questions.
- Understood TRUE/FALSE conditions.
- Applied multiple conditions to decision-making.

---

## Day 3 — Variables, Values and Data Types

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- Variables.
- Assignment and reassignment.
- Integer.
- Float.
- String.
- Boolean.
- Arithmetic expressions.
- Type conversion.

### Demonstrated understanding
- Calculated 68 + 5 = 73.
- Understood variable reassignment.
- Identified integer, float, string and Boolean values.
- Correctly calculated int("10") + int("20") = 30.

### Review
- Variable naming.
- Data type conversion.
- Mathematical expressions.

---

## Day 4 — Python Input and Output

**Status:** Completed  
**Score:** 10/10

### Topics covered
- input().
- print().
- int().
- float().
- String conversion.
- F-strings.
- Concatenation.
- Arithmetic with user input.

### Assessment
Quiz: 3/3.

### Practical work
Created and executed:

src/fundamentals/python/day04_input_output.py

Successfully accepted user input and calculated a sum.

### Demonstrated understanding
- Understood that input() returns a string.
- Understood why numeric conversion is necessary.
- Differentiated string concatenation from arithmetic addition.

---

## Day 5 — Python Operators and Expressions

**Status:** Completed  
**Score:** 10/10

### Topics covered
- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Comparison operators.
- Logical operators.
- Operator precedence.

### Assessment

| Category | Score |
|---|---:|
| Arithmetic | 3/3 |
| Comparisons | 5/5 |
| Logical operators | 5/5 |
| Operator precedence | 5/5 |
| Total | 18/18 |

### Practical work
Worked on an eligibility checker using age and marks.

### Review
- Boundary conditions.
- Correct use of >= and >.
- Writing complete IF/ELSE programs.

---

## Day 6 — Conditions, Branching and Nested Decisions

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- IF.
- ELIF.
- ELSE.
- Nested IF.
- Multiple decision branches.
- Validation.
- Marks grading.

### Practical work
Independently developed a marks grading program.

Demonstrated understanding of:
- Invalid marks.
- Grade ranges.
- Multiple conditions.
- Branch selection.

### Review
- Boundary-value testing.
- Nested decision logic.
- Independent problem-solving.

---

## Day 7 — Python Loops

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- FOR loops.
- WHILE loops.
- RANGE().
- Start, stop and step.
- Loop iterations.
- Accumulators.
- Infinite loops.
- Dry-running loops.

### Practical work

Independently wrote a multiplication table program:

```python
n = int(input("Enter a number:"))

for i in range(1, 11):
    print(f"{i} x {n} = {i*n}")
```

Also solved accumulator and countdown exercises.

### Review
- Nested loops.
- Pattern printing.
- Loop-based problem-solving.

---

## Day 8 — Python Functions

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- Defining functions.
- Calling functions.
- Parameters.
- Arguments.
- RETURN.
- PRINT versus RETURN.
- Local variables.
- Reusable code.

### Practical work

Created:

src/fundamentals/python/day08_calculate_total.py

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(50, 4)

print(f"Total={total}")
```

Output:

Total=200

### Demonstrated understanding
- Function calls.
- Parameters and arguments.
- Returning calculated values.
- Understanding None when a function has no explicit return statement.

### Review
- Functions with multiple return paths.
- Function decomposition.
- Reusable program design.

---

## Day 9 — Function Parameters and Scope

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- Multiple parameters.
- Positional arguments.
- Local scope.
- Global scope.
- Function calculations.
- Discount calculations.

### Practical work

Independently developed a discount calculator.

```python
def calculate_discount(price, discount):
    discount = (price * discount) / 100
    result = price - discount
    return result

final = calculate_discount(1000, 10)

print(f"Total price to pay:{final}")
```

Output:

Total price to pay:900.0

### Demonstrated understanding
- Calculated function outputs.
- Distinguished local and global variables.
- Understood returned values.
- Applied functions to a practical pricing problem.

### Review
- Variable scope.
- Descriptive variable naming.
- More complex functions.

---

## Day 10 — Default Parameters and Keyword Arguments

**Status:** Completed  
**Provisional score:** 8/10

### Topics covered
- Default parameters.
- Positional arguments.
- Keyword arguments.
- Overriding defaults.
- Combined function arguments.

### Demonstrated understanding
- Correctly calculated default quantity examples.
- Understood keyword argument assignment.
- Corrected an initial confusion between addition and subtraction when applying discounts.

### Review
- Complex function calls.
- Combining positional and keyword arguments.
- Function design.

---

## Day 11 — Python Lists

**Status:** Completed  
**Score:** 10/10

### Topics covered
- Creating lists.
- Indexing.
- Modifying elements.
- append().
- len().
- remove().
- pop().
- FOR loops over lists.
- Accumulators.
- Calculating totals.

### Demonstrated understanding
- Correctly identified list indexes.
- Modified list values.
- Predicted append and removal results.
- Understood loop iterations.
- Calculated totals using an accumulator.

### Important code

```python
prices = [100, 200, 300, 400]

total = 0

for price in prices:
    total = total + price

print(total)
```

Output:

1000

### Review
- List slicing.
- Searching lists.
- Calculating averages.
- Filtering list elements.

---

## Day 12 — Python Dictionaries

**Status:** Completed  
**Score:** 10/10

### Topics covered
- Dictionary creation.
- Key-value pairs.
- Accessing values.
- Adding entries.
- Updating values.
- pop().
- Membership checking using in.
- len().
- Dictionary loops.
- items().
- Accumulators with dictionaries.

### Assessment
All 11 recorded answers across exercises were correct.

### Practical example

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

print(total)
```

Output:

24

### NYXARA AI connection
Dictionaries can be used for vocabulary-to-token ID mappings and model configuration.

### Review
- Nested dictionaries.
- Dictionary methods.
- Structured data processing.

---

## Day 13 — Python Tuples and Sets

**Status:** Completed  
**Score:** 10/10

### Topics covered

#### Tuples
- Tuple creation.
- Indexing.
- len().
- Mutable versus immutable.
- Tuple modification errors.

#### Sets
- Set creation.
- Unique values.
- Removing duplicates.
- List-to-set conversion.
- Membership checking.
- add().
- remove().
- discard().

#### Data structure comparison
- Lists.
- Tuples.
- Sets.
- Dictionaries.

### Assessment
All nine recorded answers were correct.

### NYXARA AI connection
Sets can help identify unique vocabulary entries in datasets.

Example:

```python
words = [
    "AI",
    "Python",
    "AI",
    "Learning",
    "Python",
    "Model"
]

unique_words = set(words)

print(len(unique_words))
```

Output:

4

### Review
- Set operations.
- Tuple unpacking.
- Choosing the right data structure.

---

# 3. Current Python Knowledge Map

| Category | Topics covered |
|---|---|
| Computational logic | Input, processing, output, algorithms |
| Variables | Assignment, reassignment, data types |
| Operators | Arithmetic, comparison, logical |
| Decisions | IF, ELIF, ELSE, nested IF |
| Loops | FOR, WHILE, RANGE |
| Functions | Parameters, arguments, return |
| Scope | Local and global variables |
| Function arguments | Default and keyword arguments |
| Lists | Indexing, modification, methods |
| Dictionaries | Keys, values, methods, loops |
| Tuples | Indexing, immutability |
| Sets | Uniqueness, membership, methods |

---

# 4. Strengths

Based on the recorded exercises and practical work:

1. Strong understanding of computational logic.
2. Good output prediction skills.
3. Good understanding of conditions and operators.
4. Ability to dry-run loops.
5. Understanding of function parameters and return values.
6. Ability to write simple Python programs independently.
7. Good progress with Python data structures.
8. Ability to apply programming logic to practical examples.

---

# 5. Areas Requiring More Practice

These are recommended review areas, not confirmed weaknesses.

- Writing algorithms before coding.
- Nested loops.
- Complex function design.
- Local and global scope.
- Nested data structures.
- List slicing and filtering.
- Set operations.
- Combining multiple Python concepts in one program.
- Debugging independently.
- Writing programs without step-by-step assistance.

---

# 6. Next Learning Roadmap

| Day | Topic | Status |
|---|---|---|
| 14 | Python Strings and String Operations | Next |
| 15 | String Slicing and Methods | Planned |
| 16 | List and Dictionary Comprehensions | Planned |
| 17 | Nested Data Structures | Planned |
| 18 | Exception Handling | Planned |
| 19 | File Handling | Planned |
| 20 | Modules and Imports | Planned |
| 21 | Python Revision and Practical Assessment | Planned |

The exact syllabus may evolve according to learning progress.

---

# 7. Upcoming Practical Assessment

After completing the next lessons, conduct a comprehensive Python examination.

It should include:

1. Computational logic.
2. Variables and data types.
3. Operators.
4. Conditional statements.
5. Loops.
6. Functions.
7. Parameters and scope.
8. Lists.
9. Dictionaries.
10. Tuples.
11. Sets.
12. String operations.
13. Debugging.
14. Independent program development.

Assessment should include:
- Multiple-choice questions.
- Output prediction.
- Find-the-error questions.
- Algorithm writing.
- Pseudocode.
- Independent coding challenges.
- A final practical project.

A new examination score should replace the provisional progress estimate when sufficient evidence is available.

---

# 8. Connection to the NYXARA AI Project

Python fundamentals are the foundation for future NYXARA AI implementation.

Upcoming technical learning will include:

- NumPy.
- Mathematical foundations.
- Linear algebra.
- Probability and statistics.
- Data processing.
- PyTorch.
- Neural networks.
- Tokenization.
- Training pipelines.
- Model evaluation.

The goal is to understand the implementation rather than blindly copy code.

The long-term project roadmap remains:

- NYXARA 0.1: Approximately 1 million parameters.
- NYXARA 0.2 and 0.5: Intermediate development stages.
- NYXARA 1.0: Approximately 1 billion parameters.

These are project targets, not current achievements.

---

# 9. Final Assessment

**Current estimated score: 89/100**

**Learning status:** Excellent progress.

**Completed:** Python Fundamentals Days 1–13.

**Next:** Day 14 — Python Strings and String Operations.

The learner has demonstrated a growing ability to understand computational logic, predict program output, solve beginner programming problems and independently write simple Python programs.

The next priority is to strengthen independent coding ability through increasingly complex exercises and practical assessments.

---

*Report maintained as part of the NYXARA AI learning programme.*

*Scoring note: This report records available evidence as of Day 13. Scores for days without numerical quiz records are provisional estimates and must not be interpreted as independently verified examination marks.*
