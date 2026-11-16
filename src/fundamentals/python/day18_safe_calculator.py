try:
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
except ValueError:
    print("Must be integer")
try:
    c=a/b
except ZeroDivisionError:
    print("Second number not be zero")
else:
    print(c)
finally:
    print('Completed')