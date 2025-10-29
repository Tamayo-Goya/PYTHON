matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Definimos la matriz original (3x3 como ejemplo)

print("Matriz original:")
for fila in matriz:
    print(fila)
#Imprimimos la matriz 


transpuesta = []
for i in range(len(matriz)):
    fila = []
    for j in range(len(matriz)):
        fila.append(matriz[j][i])
    transpuesta.append(fila)

#Para rotar la matriz 90° en sentido horario
#Primero transponemos la matriz (intercambiamos filas por columnas)


rotada = []
for fila in transpuesta:
    rotada.append(fila[::-1])
#Ahora invertimos las filas de la transpuesta para obtener la rotación


print("\nMatriz rotada 90° en sentido horario:")
for fila in rotada:
    print(fila)
#Mostramos la matriz rotada
