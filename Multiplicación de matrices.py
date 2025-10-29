matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
#Definimos las dos matrices


print("Primera matriz:")
for fila in matriz1:
    print(fila)

print("\nSegunda matriz:")
for fila in matriz2:
    print(fila)
#Mostramos las matrices


resultado = []
#Esta sera la matriz final

for i in range(3):  
    fila = []

    for j in range(3):  
        suma = 0

        for k in range(3):  
            suma += matriz1[i][k] * matriz2[k][j]    
        fila.append(suma)
        #Invocamos a las dos matrices para multiplicarlas

    resultado.append(fila)
#Multiplicamos cada elemento de la matriz 1 con el de la matriz 2
#Y lo añadimos a la nueva matriz 


print("\nResultado de la multiplicación de las dos matrices:")
for fila in resultado:
    print(fila)
#Mostramos la matriz multiplicada
