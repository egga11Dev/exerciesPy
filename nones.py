def numberRange(list):
    """"
    that in function have one list a iteration element and the print in a screen 
    """
    for i in list:
        print(i)


def main():
    """"
  is the function initial 
  """
    numberLIST = range(1, 102, 2)
    numberRange(numberLIST)


if __name__ == "__main__":
    """"
  start a function
  """
    main()
