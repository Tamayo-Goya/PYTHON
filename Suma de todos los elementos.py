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


print("\nMatriz completa:")
for fila in matriz:
    print(fila)
#Mostramos la matriz completa

suma_total = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma_total += matriz[i][j]
#Hacemos la suma de todos los elementos


print(f"\nLa suma de todos los elementos de la matriz es: {suma_total}")
#Mostramos el resultado final
