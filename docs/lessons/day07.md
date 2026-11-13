# NYXARA AI --- Day 7

## Python Loops: Teaching Computers to Repeat

**Status:** Completed\
**Learning style:** Beginner-friendly, logic before syntax, independent
practice

## Learning goals

-   Understand why loops are useful.
-   Use `for` loops and `range()`.
-   Understand start, stop, and step.
-   Use an accumulator to calculate a running total.
-   Use `while` loops.
-   Recognize how an infinite loop can happen.
-   Write a multiplication-table program independently.

## 1. Why loops?

A loop repeats instructions. Instead of writing the same `print()`
statement hundreds of times, a program can repeat it automatically.

Python's two main loop types: - `for`: useful for iterating through a
sequence or a known range. - `while`: repeats as long as a condition
remains true.

## 2. First `for` loop

``` python
for i in range(5):
    print("NYXARA AI")
```

This prints the message five times.

-   `for` starts a loop.
-   `i` is the loop variable.
-   `range(5)` produces `0, 1, 2, 3, 4`.
-   The indented `print()` runs once for each value.

The user correctly predicted that:

``` python
for i in range(3):
    print(i)
```

prints:

``` text
0
1
2
```

The loop runs three times. The stop value `3` is excluded.

## 3. Understanding `range()`

### `range(stop)`

``` python
for i in range(5):
    print(i)
```

Values: `0, 1, 2, 3, 4`.

### `range(start, stop)`

``` python
for i in range(2, 6):
    print(i)
```

Values: `2, 3, 4, 5`.

### `range(start, stop, step)`

``` python
for i in range(2, 11, 2):
    print(i)
```

Values: `2, 4, 6, 8, 10`.

The step is the amount added each time. The stop value is excluded.

### Correction exercise

For:

``` python
for i in range(1, 10, 3):
    print(i)
```

The correct values are `1, 4, 7`.

The user initially answered `1, 3, 6, 9`. The correction was that the
loop adds 3 each time, and stops before 10.

For:

``` python
for i in range(5, 16, 5):
    print(i)
```

The correct values are `5, 10, 15`. The user initially missed the
starting value 5.

These corrections highlight two useful habits: - Include the start value
if it is within the range. - Add exactly the step each iteration. -
Never include the stop value.

## 4. Accumulator pattern

An accumulator stores a running result, such as a sum.

Example: add numbers 1 through 5.

``` python
total = 0

for i in range(1, 6):
    total = total + i

print(total)
```

Output: `15`.

The important line:

``` python
total = total + i
```

means: 1. Read the current value of `total`. 2. Add the current loop
value `i`. 3. Store the result back in `total`.

Dry run:

    Iteration   `i`   Previous total   New total
  ----------- ----- ---------------- -----------
            1     1                0           1
            2     2                1           3
            3     3                3           6
            4     4                6          10
            5     5               10          15

The user correctly solved this challenge:

``` python
total = 0

for i in range(1, 5):
    total = total + (i * 2)

print(total)
```

Final result: `20`.

Dry run: add 2, then 4, then 6, then 8.

Accumulator patterns are useful in data processing and AI, for example
when adding values or calculating totals across batches.

## 5. The `while` loop

A `while` loop repeats while its condition is true.

Countdown example:

``` python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Go!")
```

Output:

``` text
5
4
3
2
1
Go!
```

How it works: 1. Start with `count = 5`. 2. Check `count > 0`. 3. If
true, print the count. 4. Subtract one. 5. Check again. 6. When count
reaches zero, the condition is false and the loop ends.

### Infinite loops

If the update `count = count - 1` is removed, `count` remains 5. The
condition `count > 0` remains true, so the loop continues indefinitely.

This is an infinite loop. A `while` loop must have a clear way to reach
a false condition, unless an intentionally endless loop is being used
with a controlled exit mechanism.

The user correctly predicted the output of:

``` python
x = 2

while x <= 10:
    print(x)
    x = x + 2
```

Output: `2, 4, 6, 8, 10`. The loop executes five times and stops when
`x` becomes 12.

## 6. `for` versus `while`

  -----------------------------------------------------------------------
  `for` loop                          `while` loop
  ----------------------------------- -----------------------------------
  Iterates through a sequence or      Repeats while a condition is true
  range                               

  Often useful when the number of     Useful when stopping depends on a
  iterations is known                 condition

  `range()` is a common partner       The loop condition controls
                                      continuation

  The loop advances through its       The programmer often updates a
  iterable                            variable manually
  -----------------------------------------------------------------------

Examples in AI: - `for`: process a known set of training examples or
batches. - `while`: continue an operation until a stopping condition is
met.

## 7. Independent coding challenge: multiplication table

### Requirements

1.  Ask the user for a number.
2.  Convert it to an integer.
3.  Use a `for` loop to print its multiplication table from 1 to 10.

### User's submitted code

``` python
n = int(input('Enter a number:'))

for i in range(1, 11):
    print(f'{i} x {n} = {i*n}')
```

### Review

The code is correct: - `input()` receives text from the user. - `int()`
converts the text to an integer. - `range(1, 11)` generates 1 through
10. - `i * n` calculates each product. - The loop prints ten lines.

The requested display format was `5 x 1 = 5`. The user's version prints
`1 x 5 = 5`. Both calculations are mathematically equivalent. To match
the requested format exactly, use:

``` python
print(f'{n} x {i} = {n * i}')
```

## 8. Progress record

-   `range(stop)`: understood.
-   `range(start, stop)`: introduced.
-   `range(start, stop, step)`: practised, with corrections for step and
    start value.
-   Accumulator pattern: correctly solved a calculation challenge.
-   `while` loop: understood and correctly dry-run.
-   Infinite-loop cause: explained.
-   Multiplication-table program: independently written and reviewed.

## 9. Review before the next lesson

1.  What values does `range(3)` produce?
2.  What values does `range(2, 10, 2)` produce?
3.  Why is the stop value excluded?
4.  What does an accumulator do?
5.  What could cause a `while` loop to run forever?
6.  When would you choose a `for` loop instead of a `while` loop?

**Next lesson:** Day 8 --- Python Functions.
