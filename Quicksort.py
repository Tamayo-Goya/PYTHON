def quicksort(lista):
    
    if len(lista) <= 1:
        return lista 
    #Si una lista esta vacía o es de un solo elemento está ordenada
    
    pivote = lista[-1]  
    #Definimos el último elemento como pivote

    menores = []
    mayores = []
    #Creamos dos listas para almacenar los numeros

   
    for elemento in lista[:-1]:
        if elemento <= pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)
    #Añadimos los elementos a las listas según el pivote
    

    return quicksort(menores) + [pivote] + quicksort(mayores)
    #Ordenamos de manera recursiva las sublistas


numeros = [40, 21, 8, 17, 51, 34]
ordenados = quicksort(numeros)
#Ejemplo de ejecucion

print("Lista original:", numeros)
print("Lista ordenada:", ordenados)
#Mostramos por pantalla el resultado
