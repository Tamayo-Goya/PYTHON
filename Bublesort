def bubble_sort(prueba):
    n = len(prueba)  
    #Definimos n como la longitud de la lista
    
    for i in range(n - 1):
    #Recorremos toda la lista n-1 pasadas con for
      
        print("--- Paso", i + 1, "---")  
        #Indicamos el número de pasada
       
        cambio = False  
        #Definimos cambio para verificar si se hizo algún intercambio
        
   
        for j in range(n - i - 1):  
            #En cada pasada vamos a comparar los elementos adyacentes
            #Los últimos i elementos que ya están ordenados

            print("Comparando", prueba[j], "y", prueba[j + 1], end=" -> ")
            #Si el elemento actual es mayor que el siguiente, se intercambian

            if prueba[j] > prueba[j + 1]:
                prueba[j], prueba[j + 1] = prueba[j + 1], prueba[j]  
                #Intercambiamos las posiciones

                cambio = True  
                #Definimos que hubo un intercambio

                print("intercambio:", prueba)  
                #Mostramos por pantalla el estado actual de la lista

            else:
                print("no se intercambia")  
                #Si no cumple la condición, no hace nada
      
        if not cambio:
            print("No se realizaron intercambios en este paso (la lista puede estar ordenada).")
        #Verificamos si no hubo intercambios
    
   
    return prueba
    #Devolvemos la lista ya ordenada 



prueba = [5, 1, 4, 2, 8]
print("Lista original:", prueba)
ordenada = bubble_sort(prueba)  
print("Lista ordenada:", ordenada) 
#Ejemplo de ejecucion 
