matriz1 = [
    [1, 2, 2],
    [4, 4, 6],
    [1, 2, 5]
]
matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
#Definimos las dos matrices directamente

print("Primera matriz:")
for fila in matriz1:
    print(fila)

print("\nSegunda matriz:")
for fila in matriz2:
    print(fila)
#Imprimimos por pantalla las matrices 


resultado = []
for i in range(3):
    fila = []
    for m in range(3):
        suma = matriz1[i][m] + matriz2[i][m]
        fila.append(suma)
    resultado.append(fila)
#Sumamos las dos matrices valor por valor

print("\nResultado de la suma de las dos matrices:")
for fila in resultado:
    print(fila)
#Imprimimos por pantalla las matrices sumadas

