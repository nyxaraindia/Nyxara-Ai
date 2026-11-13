def calculate_discount(price , discount):
    discoun=(price*discount)/100
    result=price-discoun
    return result
final=calculate_discount(1000,10)
print(f'Total price to pay:{final}')