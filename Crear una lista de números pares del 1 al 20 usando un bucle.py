lista = []
#Creamos la lista vacia

for i in range(1, 21):
#Utilizamos for para que recorra i del 1 al 20 (ponemos 21 para incluir al 20)

    if i % 2 == 0:
        lista.append(i)
#Utilizamos if para comprobar si i es par o no y lo añadimos a la lista

print(lista)
#Imprimimos la lista