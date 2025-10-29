matriz = []  
# Definimos la lista donde almacenará todo

contador = 1
# Definimos un contador solo para mostrar el número
# del elemento que estamos añadiendo

for i in range(3):  
    # Ya que la matriz es 3x3, solo vamos a recorrer 3 veces
    
    fila = []  
    # Definimos fila para almacenar los datos

    for j in range(3):  
        valor = int(input(f"Elemento {contador}: "))
        # Pedimos al usuario los valores para la matriz

        fila.append(valor) 
        # Añadimos el número a la fila

        contador = contador + 1
        
    matriz.append(fila)  
    # Añadimos toda la fila a la matriz


print("\nMatriz completa:")
for fila in matriz:
    print(fila)
# Mostramos la matriz   


print("\nElementos de la matriz uno por uno:")
for n in range(len(matriz)):         
    # Recorre las filas

    for p in range(len(matriz[n])):  
        # Recorre las columnas

        print(f"Elemento en [{n}][{p}] = {matriz[n][p]}")
#Recorremos toda la matriz e imprimimos cada elemento
