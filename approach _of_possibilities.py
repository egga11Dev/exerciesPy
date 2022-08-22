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