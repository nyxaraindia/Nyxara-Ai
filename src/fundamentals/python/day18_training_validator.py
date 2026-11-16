try:
    batch=input('Enter a batch number:')
    n=int(batch)
    if n<=0:
        raise ValueError("Not be zero or less than zero")
except ValueError:
    print("Value must be integer")
else:
    print(n)
finally:
    print('Configuration check completed!')
