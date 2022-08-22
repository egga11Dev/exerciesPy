def approach():
    # este es un algorithmo de mayor acercamiento a la repuesta o a las posibilidades
    objective = int(input('select one number type int: '))
    epsilon = 0.01
    step = epsilon**2
    answer = 0.0

    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        answer += step

    if abs(answer**2 - objective) >= epsilon:
        print(f'no se encontro la raiz cuadrada de {objective}')
    else:
        print(f'la raiz cuadrada de {objective} es {answer}')


def exhaustive_numbering():
    objective = int(input('select one number type int: '))
    raiz = 0

    while raiz**2 < objective:
        raiz += 1

    if raiz**2 == objective:
        print(f'la raiz cuadrada de {objective} es {raiz}')
    else:
        print(f'{objective} no tiene raiz cuadrada')


def search_binary():
    #es la busqueda binaria funciona cuando solo se utiliza linealmente
    objective = int(input('select one number type int: '))
    epsilon = 0.01
    bass = 0.0
    tall = max(1.0, objective)
    answer = (tall + bass) / 2

    while abs(answer**2 - objective) >= epsilon:
        print(f'bass={bass}, tall={tall}, answer={answer}')
        if answer**2 < objective:
            bass = answer
        else:
            tall = answer
        answer = (tall + bass) / 2
    print(f'la raiz cuadrada de {objective} es {answer}')


def main():
    print("1-approach")
    print("2-exhaustive numbering")
    print("3-search binary")
    option = input("cual algorithmo quieres verificar:")

    if option == "1":
        approach()
    elif option == "2":
        exhaustive_numbering()
    elif option == "3":
        search_binary()


if __name__ == "__main__":
    main()
