texto = input("Introduce una cadena de texto: ")
#Pedimos el texto mediante un input

invertida = ""
#Creamos una variable "vacia"

for i in texto:
    invertida = i + invertida
#creamos un bucle donde i reccore todo el texto
#le asignamos a invertida el valor de i + su valor

print("Cadena invertida:", invertida)
#Mostramos por pantalla el valor de invertida 