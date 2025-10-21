def merge_sort(lista):
   
    if len(lista) > 1:
     
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        #Dividimos la lista en dos mitades

     
        merge_sort(izquierda)
        merge_sort(derecha)
        #Ordenamos cada mitad

     
        indice_izquierda = 0
        indice_derecha = 0
        indice_lista = 0
        #Creamos unos indices para recorrer las sublistas

        while indice_izquierda < len(izquierda) and indice_derecha < len(derecha):
            if izquierda[indice_izquierda] < derecha[indice_derecha]:
                lista[indice_lista] = izquierda[indice_izquierda]
                indice_izquierda += 1
            else:
                lista[indice_lista] = derecha[indice_derecha]
                indice_derecha += 1
            indice_lista += 1
        #Combinamos las sublistas ordenadas



        while indice_izquierda < len(izquierda):
            lista[indice_lista] = izquierda[indice_izquierda]
            indice_izquierda += 1
            indice_lista += 1  
        #Agregamos los elementos restantes de la sublista izquierda
        

       
        while indice_derecha < len(derecha):
            lista[indice_lista] = derecha[indice_derecha]
            indice_derecha += 1
            indice_lista += 1
         #Y ahora agregamos los elementos restantes de la sublista derecha



datos = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", datos)
merge_sort(datos)
print("Lista ordenada:", datos)

#Ejemplo de ejecucion
