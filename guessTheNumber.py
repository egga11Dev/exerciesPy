import random
from time import sleep

print("**********Guess the number I thought**********")
tryGame = input("\nyou want to try: ")


def tryLogic(counter, number):
    while True:
        tryDecision = int(input("try to guess 1 a 100: "))
        if (tryDecision == number):
            print("in good time you guessed it")
            print(f'after {counter} attempts bye')
            break
        elif (tryDecision > number):
            print("try of new is minor")
            counter += 1
        elif (tryDecision < number):
            print("try of new is elderly")
            counter += 1


def main(decision):
    if (decision == 'yes' or decision == 'y'):
        print("let me think of a number")
        number = random.randint(1, 100)
        sleep(3)
        print("I already thought it\n")
        counter = 0
        tryLogic(counter, number)
    else:
        print("bye")


if __name__ == '__main__':
    main(tryGame)
