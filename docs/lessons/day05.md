# NYXARA AI --- Day 5

## Python Operators and Expressions

**Status:** Completed\
**Learning style:** Beginner-friendly, logic before syntax, independent
practice

## Learning goals

-   Use arithmetic operators.
-   Compare values and understand Boolean results.
-   Combine conditions with logical operators.
-   Understand operator precedence.
-   Build a small eligibility checker.

## 1. Arithmetic operators

Arithmetic operators perform calculations.

  Operator   Meaning                   Example   Result
  ---------- --------------------- ----------- --------
  `+`        Addition                  `8 + 2`     `10`
  `-`        Subtraction               `8 - 2`      `6`
  `*`        Multiplication            `8 * 2`     `16`
  `/`        Division                 `17 / 5`    `3.4`
  `//`       Floor division          `17 // 5`      `3`
  `%`        Remainder (modulus)      `17 % 5`      `2`
  `**`       Exponentiation           `3 ** 3`     `27`

### Important distinction: `/`, `//`, and `%`

For `17 / 5`: - `/` gives the exact division result: `3.4`. - `//` gives
the floor-division result: `3`. - `%` gives the remainder: `2`.

The user correctly answered: - `17 // 5` → `3` - `17 % 5` → `2` -
`3 ** 3` → `27`

**Arithmetic quiz: 3/3.**

## 2. Comparison operators

Comparison operators compare two values. Their result is a Boolean:
`True` or `False`.

  Operator   Meaning
  ---------- --------------------------
  `>`        Greater than
  `<`        Less than
  `>=`       Greater than or equal to
  `<=`       Less than or equal to
  `==`       Equal to
  `!=`       Not equal to

Examples:

``` python
print(25 > 20)   # True
print(15 == 20)  # False
print(40 >= 40)  # True
print(50 != 50)  # False
print(30 <= 35)  # True
```

The user answered all five comparison questions correctly.

**Comparison quiz: 5/5.**

## 3. Logical operators

Logical operators combine or reverse Boolean conditions.

-   `and`: True only when both sides are True.
-   `or`: True when at least one side is True.
-   `not`: reverses a Boolean value.

  Expression          Result
  ------------------- ---------
  `True and False`    `False`
  `True or False`     `True`
  `not True`          `False`
  `False and False`   `False`
  `not False`         `True`

The user answered all five logical-operator questions correctly.

**Logical-operator quiz: 5/5.**

## 4. Operator precedence

Python follows an order when an expression contains multiple operators.
Parentheses can make the intended order explicit.

A useful simplified order for the operators studied:

1.  Parentheses
2.  Exponentiation (`**`)
3.  Multiplication, division, floor division, modulus (`*`, `/`, `//`,
    `%`)
4.  Addition and subtraction (`+`, `-`)
5.  Comparisons
6.  `not`
7.  `and`
8.  `or`

Examples:

``` python
print(5 + 3 * 2)       # 11
print((5 + 3) * 2)     # 16
print(20 / 5 + 2)      # 6.0
print(2 ** 3 + 4)      # 12
print(10 + 6 // 2)     # 13
```

The user solved all five precedence questions correctly.

**Precedence quiz: 5/5.**

## 5. Independent coding challenge: eligibility checker

### Requirements

-   Ask for a person's age.
-   Ask for their marks.
-   A person is eligible only if age is at least 18 **and** marks are at
    least 40.
-   Display an appropriate result.

### User's submitted code

``` python
age = int(input('Enter Age:'))
mark = int(input('Enter Mark:'))

if age >= 18 and mark > 40:
    print('Elgible')
```

### Review and correction

The user correctly combined the two requirements using `and`.

There was one boundary-condition bug: the requirement was "at least 40",
which includes 40. Therefore, `mark > 40` should be `mark >= 40`.

An `else` branch also makes the program give a result when the person is
not eligible.

A corrected version:

``` python
age = int(input('Enter age:'))
mark = int(input('Enter mark:'))

if age >= 18 and mark >= 40:
    print('Eligible')
else:
    print('Not eligible')
```

The user reported completing the correction. The revised code was not
shown, so the correction is recorded as reported rather than
independently verified.

## 6. Key concepts to remember

-   An operator performs an action on values.
-   A comparison produces `True` or `False`.
-   `and` requires both conditions to be true.
-   `or` requires at least one condition to be true.
-   `not` reverses a Boolean value.
-   Operator precedence determines which operation Python evaluates
    first.
-   Boundary words matter: "at least 40" means `>= 40`, not `> 40`.

## 7. Progress record

-   Arithmetic operators: understood; 3/3.
-   Comparison operators: understood; 5/5.
-   Logical operators: understood; 5/5.
-   Operator precedence: understood; 5/5.
-   Eligibility-checker challenge: independently attempted; boundary
    correction identified and reported completed.

## 8. Review before the next lesson

Try these without running Python:

1.  What is the difference between `17 // 5` and `17 % 5`?
2.  What is the result of `10 >= 10`?
3.  What is the result of `True and False`?
4.  What is the result of `5 + 2 * 3`?
5.  Why is `>=` appropriate when a requirement says "at least"?

**Next lesson:** Day 6 --- Python Conditions, Branching and Nested
Decisions.
