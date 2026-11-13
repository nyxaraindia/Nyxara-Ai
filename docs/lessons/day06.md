# NYXARA AI --- Day 6

## Python Conditions, Branching and Nested Decisions

**Status:** Completed\
**Learning style:** Beginner-friendly, logic before syntax, independent
practice

## Learning goals

-   Use `if`, `elif`, and `else`.
-   Understand how Python chooses one branch.
-   Use nested `if` statements.
-   Check boundary values.
-   Build an independent marks-grading program.

## 1. How a program makes decisions

A program can choose what to do based on a condition.

Example: a student-result system: - Marks 90 or above → Excellent. -
Marks 50 to 89 → Passed. - Marks below 50 → Failed.

``` python
marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Passed")
else:
    print("Failed")
```

### How Python evaluates this

Python checks the conditions from top to bottom:

1.  Is `marks >= 90` true? No.
2.  Is `marks >= 50` true? Yes.
3.  Print `Passed`.
4.  Skip the remaining branches.

Only the first matching branch in an `if`/`elif`/`else` chain runs.

The user correctly predicted: - 95 → Excellent - 45 → Failed?
**Correction to note:** With the exact example above, 45 is below 50, so
it prints `Failed`. - 30 → Failed

During the lesson's first exercise, the actual question cases were 95,
45, and 30. The user answered "Excellent, Passed, Failed"; the assistant
mistakenly marked all correct. The correct result for 45 in the shown
code is **Failed**, because `45 >= 50` is false. This correction is
important for accurate records.

## 2. Nested decisions

A nested `if` is an `if` statement placed inside another `if` or `else`
block.

Example: college admission requires: - Age at least 18. - Marks at least
50.

``` python
age = 19
marks = 65

if age >= 18:
    if marks >= 50:
        print("Admission allowed")
    else:
        print("Marks too low")
else:
    print("Age requirement not met")
```

### How it works

1.  Check age.
2.  If age is below 18, print `Age requirement not met`; the inner marks
    check is never reached.
3.  If age is at least 18, check marks.
4.  If marks are at least 50, print `Admission allowed`.
5.  Otherwise, print `Marks too low`.

The user correctly predicted all three cases:

    Age   Marks Output
  ----- ------- -------------------------
     17      80 Age requirement not met
     20      40 Marks too low
     20      75 Admission allowed

**Nested-decision exercise: 3/3.**

## 3. Independent coding challenge: marks grading

### Requirements

Ask the user for marks and print: - Below 0 or above 100 → Invalid
marks. - 90--100 → Grade A. - 75--89 → Grade B. - 50--74 → Grade C. -
0--49 → Fail.

Use `input()`, `int()`, `if`, `elif`, and `else`.

### User's submitted code

``` python
m = int(input('Enter mark:'))

if m < 0 or m > 100:
    print('Invalid mark')
elif m > 89:
    print('A')
elif m > 74:
    print('B')
elif m > 49:
    print('C')
else:
    print('fail')
```

### Review

The code is logically correct for every required range.

    Marks Expected result   Code result
  ------- ----------------- -------------
       -5 Invalid           Invalid
        0 Fail              Fail
       49 Fail              Fail
       50 C                 C
       74 C                 C
       75 B                 B
       89 B                 B
       90 A                 A
      100 A                 A
      101 Invalid           Invalid

### Important reasoning

Why can the code use `m > 89` instead of `m >= 90 and m <= 100`?

Because the first condition already rejects values below 0 and above
100. If Python reaches the later branches, the value is known to be in
the valid range. Earlier failed conditions also narrow down what values
remain possible.

## 4. Key concepts to remember

-   `if` checks the first condition.
-   `elif` checks another condition only if earlier branches did not
    match.
-   `else` handles the remaining cases.
-   A nested `if` performs a second decision inside an earlier decision.
-   Indentation defines which statements belong to each branch.
-   Boundary values should always be tested, especially where ranges
    meet.

## 5. Progress record

-   `if` / `elif` / `else`: practised.
-   Nested decisions: correctly reasoned through three cases.
-   Independent marks-grading program: submitted and reviewed; all
    boundary ranges are correct.
-   One earlier quiz marking error is corrected in this record: for the
    example with `marks = 45` and the threshold `marks >= 50`, the
    output is `Failed`, not `Passed`.

## 6. Review before the next lesson

1.  What happens when the first `if` condition is true?
2.  When does Python execute an `else` branch?
3.  Why might a nested `if` be useful?
4.  What is the output for marks exactly equal to 50 in the grading
    program?
5.  Why should a program check invalid marks before assigning a grade?

**Next lesson:** Day 7 --- Python Loops (`for` and `while`).
