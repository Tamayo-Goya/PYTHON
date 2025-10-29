matriz = []  
#Definimos la lista donde almacenará todo

contador = 1
#Definimos un contador solo para mostrar el número
#del elemento que estamos añadiendo

for i in range(3):  
    #Ya que la matriz es 3x3, solo vamos a recorrer 3 veces
    
    fila = []  
    #Definimos fila para almacenar los datos

    for j in range(3):  
        valor = int(input(f"Elemento {contador}: "))
        #Pedimos al usuario los valores para la matriz

        fila.append(valor) 
        #Añadimos el número a la fila

        contador = contador + 1
        
    matriz.append(fila)  
    #Añadimos toda la fila a la matriz


print("\nMatriz original:")
for fila in matriz:
    print(fila)
#Mostramos la matriz original


traspuesta = []
#Definimos la traspuesta

for i in range(3):
    fila = []
    for j in range(3):
        fila.append(matriz[j][i])
    traspuesta.append(fila)
#Intercambiamos las filas por columnas

print("\nMatriz traspuesta:")
for fila in traspuesta:
    print(fila)
#Mostramos la matriz traspuesta
