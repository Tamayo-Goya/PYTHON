class Perro:
    def hablar(self):
        print("Guau") 
    #método hablar específico del perro

class Gato:
    def hablar(self):
        print("Miau")  
    #método hablar específico del gato


animal1 = Perro()
animal2 = Gato()
#creamos objetos de tipo Perro y Gato

animales = [animal1, animal2]
#los metemos en una lista de animales

for animal in animales:
#recorremos la lista y llamamos al mismo método hablar()
    animal.hablar()  
    #por el polimorfismo, cada uno ejecuta su propia versión
