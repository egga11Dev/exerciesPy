print("checked numbers if cousins or not")


def ifCousin(date):
    counter = 0
    for i in range(2, date):
        if date % i == 0:
            return False
    return True


def main():
    number = int(input("\ninsert number: "))
    if (ifCousin(number)):
        print("is cousin")
    else:
        print("not is cousin")


if (__name__ == "__main__"):
    main()
