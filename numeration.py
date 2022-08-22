#este es el algiritmo de evalucion de todas las posibilidades

objective = int(input('select one number type int: '))
raiz = 0

while raiz**2 < objective:
    raiz += 1

if raiz**2 == objective:
    print(f'la raiz cuadrada de {objective} es {raiz}')
else:
    print(f'{objective} no tiene raiz cuadrada')

#esta es la mejora para la raiz cuadrada mas rapido

comprobacion = objective // 2
if comprobacion * comprobacion == objective:
    print(f'la raiz cuadrada de {objective} es {raiz}')
else:
    print(f'{objective} no tiene raiz cuadrada')