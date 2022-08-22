import random

CAPITAL_LETTERS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'
]
MINUS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'
]
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARS = [
    '*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',',
    ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"'
]


def generatePass():
    password = []
    characters = CAPITAL_LETTERS + MINUS + NUMS + CHARS
    while len(password) < 15:
        random_Pass = random.choice(characters)
        password.append(random_Pass)
    password = "".join(password)
    return password


def main():
    password = generatePass()
    print("your new password is: ", password)
    print(round(10.3456, 2))


if __name__ == "__main__":
    main()
