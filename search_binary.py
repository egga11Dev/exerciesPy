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