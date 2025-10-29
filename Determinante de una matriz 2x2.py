matriz = [
    [3, 5],
    [2, 7]
]
#Definimos la matriz 2x2


determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
#Calculamos el determinante
#Fórmula para matriz 2x2: determinante = a*d - b*c
#a = es el elemento fila 0, columna 0
#b = es el elemento fila 0, columna 1
#c = es el elemento fila 1, columna 0
#d = es el elemento fila 1, columna 1

print(f"Matriz:")
for fila in matriz:
    print(fila)
#Mostramos la matriz

print(f"Determinante de la matriz: {determinante}")
#Mostramos el valor de determinante
