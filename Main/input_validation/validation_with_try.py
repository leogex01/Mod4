"""
Program : validation_with_try.py
Author : Chris Geralds
Date : 06/10/2020
Small program to take three test scores and average them out
"""
import unittest


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError("Only positive integers are allowed")
    return float((score1 + score2 + score3) / NUMBER_TESTS)


if __name__ == '__main__':
    last_name = input("Please enter your last name. ")
    first_name = input("Please enter your first name. ")
    age = str(input("Please enter your age. "))
    test1 = int(input("Enter first score:  "))
    test2 = int(input("Enter second score:  "))
    test3 = int(input("Enter last score:  "))
    average = average(test1, test2, test3)
    print(f'{last_name}, {first_name} age:{age} average score:  {average}')
