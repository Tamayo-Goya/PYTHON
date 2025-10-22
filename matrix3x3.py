matriz = []  
#Definimos la lista donde almacenara todo

contador = 1
#Definimos un contador solo para mostrar el numero
#del elemento que estamos añadiendo

for i in range(3):  
#Ya que la matriz es 3x3 solo vamos a recorrer 3 veces
    
    fila = []  
    #Definimos fila para almacenar los datos

    for j in range(3):  

        valor = int(input(f"Elemento {contador}: "))
        #Pedimos al usuario los valores para la matriz

        fila.append(valor) 
        #Añadimos el numero a la fila

        contador = contador + 1
        
    matriz.append(fila)  
    #Añadimos todo a la matrix


for fila in matriz:
    print(fila)
#Mostramos por pantalla la matriz