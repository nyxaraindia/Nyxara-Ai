# NYXARA AI — Day 2

## Topic
Conditions and Decision Logic

## Learning objectives
- Understand conditions.
- Learn comparison operators.
- Distinguish assignment (=) and equality (==).
- Understand multiple conditions.
- Learn decision chains and mathematical ranges.

## Concepts
A condition is a statement that evaluates to TRUE or FALSE.

### Comparison operators
>  Greater than
<  Less than
>= Greater than or equal
<= Less than or equal
== Equal to
!= Not equal to

### Multiple conditions
A decision chain checks multiple conditions to select an outcome.

### Mathematical range
20 <= T < 30

## Practical challenge
Build an age classification algorithm:
- Below 13: Child
- 13 to 19: Teenager
- 20 or above: Adult

## Progress
- Concepts introduced.
- Independent algorithm challenge pending.
- Python implementation not started.

## Next
Review the submitted algorithm and introduce variables and Python syntax.

## Student's independent algorithm

START
INPUT age
IF age < 13
    DISPLAY "CHILD"
ELSE IF age >= 13 AND age <= 19
    DISPLAY "TEENAGER"
ELSE
    DISPLAY "ADULT"
STOP

## Evaluation
- Correct input.
- Correct first condition.
- Correct second condition.
- Correct use of AND.
- Correct handling of remaining cases using ELSE.

## Improved algorithm
IF age < 13
    DISPLAY "CHILD"
ELSE IF age <= 19
    DISPLAY "TEENAGER"
ELSE
    DISPLAY "ADULT"

The second condition can be simplified because the first
condition has already established that age is at least 13.

## Assessment
Score: 5/5

All five decision-logic questions answered correctly.

## Concepts completed
- Conditions
- Comparison operators
- IF / ELSE IF / ELSE
- AND logical operator
- Decision chains
- Boundary-value testing
- Algorithm simplification

## Next lesson
Variables, storing information, and understanding
how Python represents data.
