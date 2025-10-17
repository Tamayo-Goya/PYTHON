n = int(input("Introduce un número: "))
#Pedimos el numero

factorial = 1
contador = 1
#Definimos dos variables para el bucle while


while contador <= n:
    factorial *= contador
    contador += 1
#Creamos un bucle en el que siempre que el contador sea menor o igual que
#el numero dado por el usuario se siga ejecutando
#En el bucle cambiamos el valor de factorial para que sea 
#factorial = factorial * contador y sumamos a contador su valor + 1



print(f"El factorial de {n} es: {factorial}")
#Mostramos por pantalla el valor final de factorial al salir del bucle