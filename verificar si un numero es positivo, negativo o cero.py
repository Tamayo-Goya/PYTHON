num = (int(input("Introduce un número: ")))
#Solicitamos el numero

if num > 0:
    print("El numero", num, "es positivo")
#Utilizamos if para comprobar si es positivo 

elif num == 0:
    print("El numero", num, "es igual a 0")
#Utilizamos elif para comprobar si es 0 despues de comprobar que no es positivo 

else:
    print("El numero", num, "es negativo")
#Utilizamos else para imprimir en pantalla negativo 
