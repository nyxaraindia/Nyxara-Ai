def calculate(price,quantity=2,discount=0):
    total=price*quantity
    final=total-discount
    return final
a=calculate(100)
b=calculate(100,discount=10)
c=calculate(100,quantity=3)
d=calculate(200,quantity=2,discount=50)
print(a)
print(b)
print(c)
print(d)