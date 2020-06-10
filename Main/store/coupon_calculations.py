"""
Program : coupon_calculations.py
Author : Chris Geralds
Date: 06/09/2020
Program to total a bill plus tax and shipping using inputted price, cash-discount, and percent-discount.
"""


def calculate_order(pr, cashdis, perdiscount):
    taxrate = .06
    cash_subtotal = float(pr) - float(cashdis)
    if perdiscount == 0:
        subtotal = cash_subtotal
    else:
        subtotal = cash_subtotal - (cash_subtotal * perdiscount/100)
    tax = subtotal * taxrate
    if subtotal <= 10:
        shipping = 5.95
        return round(subtotal + shipping + tax, 2)
    elif 10 < subtotal < 30:
        shipping = 7.95
        return round(subtotal + shipping + tax, 2)
    elif 30 < subtotal < 50:
        shipping = 11.95
        return round(subtotal + shipping + tax, 2)
    elif subtotal >= 50:
        shipping = 0
        return round(subtotal + shipping + tax, 2)





if __name__ == '__main__':
    price = float(input('Please enter price: '))
    cash = float(input('Enter cash off coupon amount: '))
    percent = float(input('Enter percentage discount amount: '))
    calculate_order(price, cash, percent)
    print(f'Your total is {calculate_order(price, cash, percent)}')
