matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Definimos la matriz 


print("Matriz original:")
for fila in matriz:
    print(fila)
#Imprimimos la matriz


escalar = int(input("\nIntroduce el escalar para multiplicar la matriz: "))
#Pedimos al usuario el escalar


resultado = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(matriz[i][j] * escalar)
    resultado.append(fila)
#Multiplicamos cada valor de la matriz por el numero escalar dado por el usuario


print("\nMatriz después de la multiplicación escalar:")
for fila in resultado:
    print(fila)
#Mostramos la matriz
