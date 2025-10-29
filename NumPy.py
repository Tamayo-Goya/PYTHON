import numpy as np
#Importamos numpy y le cambiaamos el nombre a np
#Esto es solo para simplificar a la hora de llamarla

matriz = np.array([[1, 2], [3, 4]])
print("Matriz original:")
print(matriz)
#Creamos la matriz usan numpy.array


transpuesta = matriz.T
print("\nTranspuesta:")
print(transpuesta)
#Transponemos la matriz antes creada con .T


otra_matriz = np.array([[5, 6], [7, 8]])
suma = matriz + otra_matriz
print("\nSuma con otra matriz:")
print(suma)
#Sumamos con otra matriz del mismo tamaño con el uso de numpy.array 


multiplicacion = matriz * otra_matriz
print("\nMultiplicación elemento a elemento:")
print(multiplicacion)
#Multiplicamos elemento a elemento usando las dos variables antes definidas


identidad = np.eye(2)
print("\nMatriz identidad:")
print(identidad)
#Mostramos la matriz identidad de 2x2 con numpy.eye


ceros = np.zeros((2, 2))
print("\nMatriz de ceros:")
print(ceros)
#Mostramos la matriz de ceros de 2x2 con numpy.zeros
