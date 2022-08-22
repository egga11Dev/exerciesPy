from math import factorial
import re


def factor(number):
    """"
    calculate the factor of n
    n int > 0
    return n!
    """
    print(number)
    if number == 1:
        return 1
    return number * factor(number - 1)


def main():
    """"
    is the function initial of program factor of form math n! = n *(n-1)!
    """
    inputINT = int(input('write one number type int: '))
    print(factor(inputINT))


if __name__ == "__main__":
    main()
