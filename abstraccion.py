from abc import ABC, abstractmethod
#importamos las herramientas para crear clases abstractas


class FiguraGeometrica(ABC):
#clase abstracta
    @abstractmethod
    def area(self):
        pass   
    #las subclases deben implementar este método

class Rectangulo(FiguraGeometrica):
#clase Rectangulo que hereda de FiguraGeometrica

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    #constructor con base y altura

    def area(self):
    #implementación del método abstracto area()
        
        return self.base * self.altura   
        #fórmula del área de un rectángulo

class Circulo(FiguraGeometrica):
#clase Circulo que hereda de FiguraGeometrica

    def __init__(self, radio):
        self.radio = radio
    #constructor con el radio

    def area(self):
    #implementación del método abstracto area()
        return 3.14159 * (self.radio ** 2)   
    #fórmula del área de un círculo

rect = Rectangulo(5, 3)
circ = Circulo(4)
print("Área del rectángulo:", rect.area())  
print("Área del círculo:", circ.area())     
#mostramos por pantalla 
