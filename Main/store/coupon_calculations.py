"""
Program : coupon_calculations.py
Author : Chris Geralds
Date: 06/09/2020
Program to total a bill plus tax and shipping using inputted price, cash-discount, and percent-discount.
"""


def calculate_order(pr, cashdis, perdiscount):
    taxrate = .06
    cash_subtotal = float(pr) - float(cashdis)
    print(cash_subtotal)
    subtotal = cash_subtotal - (cash_subtotal * float(perdiscount) / 100)
    tax = subtotal * taxrate
    print(subtotal)
    if subtotal < 10:
        shipping = 5.95
        total = subtotal + shipping + tax
        print(f'shipping:{shipping} \n' f'Sales tax: {tax} ')
        return shipping
    elif 10 < subtotal < 30:
        shipping = 7.95
        total = subtotal + shipping + tax
        print(f'shipping:{shipping} \n' f'Sales tax: {tax} ')
        return shipping



if __name__ == '__main__':
    price = float(input('Please enter price: '))
    cash = float(input('Enter cash off coupon amount; '))
    percent = float(input('Enter percentage discount amount: '))
    calculate_order(price, cash, percent)
    print(f'Your total is {calculate_order(price, cash, percent)}')
