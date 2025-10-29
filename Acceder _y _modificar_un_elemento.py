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
#Mostramos por pantalla la matriz 



print("\n--- Modificar un elemento ---")
fila_mod = int(input("Introduce el número de fila (0, 1 o 2): "))
col_mod = int(input("Introduce el número de columna (0, 1 o 2): "))
nuevo_valor = int(input("Introduce el nuevo valor: "))
#Ahora pedimos al usuario qué elemento quiere modificar


matriz[fila_mod][col_mod] = nuevo_valor
#Modificamos el valor seleccionado


print("\nMatriz modificada:")
for fila in matriz:
    print(fila)  
#Mostramos por pantalla la matriz cambiada

