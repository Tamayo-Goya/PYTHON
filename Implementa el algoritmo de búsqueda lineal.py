numero = int(input("Introduce el numero del 1 al 10: "))

lista = [3, 5, 6, 2, 7, 1, 4, 9, 10, 8]
posicion = 0

for i in lista:
    posicion = posicion + 1
    if i == numero:
        print("El numero",numero,"esta en la posicion:", posicion)