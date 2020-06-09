def calculate_order(price, cash, percent):
    TAXRATE = .06
    cash_subtotal = price -cash
    print(cash_subtotal)
    subtotal = cash_subtotal - (cash_subtotal * percent/100)
    tax = subtotal * TAXRATE
    print(subtotal)
    if  subtotal < 10:
        shipping = 5.95
        total = subtotal + shipping + tax
        print(f'shipping:{shipping} \n' f'Sales tax: {tax} \n' f'Total is {total}')





if __name__ == '__main__':
    price = float(input('Please enter price: '))
    cash = float(input('Enter cash off coupon amount; '))
    percent = float(input('Enter percentage discount amount: '))
    calculate_order(price, cash, percent)
