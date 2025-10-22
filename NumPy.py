import numpy as np

# Crear matriz
matriz = np.array([[1, 2], [3, 4]])
print("Matriz original:")
print(matriz)

# Transpuesta
transpuesta = matriz.T
print("\nTranspuesta:")
print(transpuesta)

# Suma con otra matriz (del mismo tamaño)
otra_matriz = np.array([[5, 6], [7, 8]])
suma = matriz + otra_matriz
print("\nSuma con otra matriz:")
print(suma)

# Multiplicación (elemento a elemento)
multiplicacion = matriz * otra_matriz
print("\nMultiplicación elemento a elemento:")
print(multiplicacion)

# Matriz identidad (de 2x2)
identidad = np.eye(2)
print("\nMatriz identidad:")
print(identidad)

# Matriz de ceros (de 2x2)
ceros = np.zeros((2, 2))
print("\nMatriz de ceros:")
print(ceros)
