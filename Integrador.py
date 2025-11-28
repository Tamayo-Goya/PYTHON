class Persona:
    #clase base
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self): 
    #polimórfico
        print(f"Soy {self.nombre} y tengo {self.edad} años.")

class Alumno(Persona):
    #subclase Alumno
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)
        self.__nota = nota 
        #Encapsulado

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

    def obtener_nota(self):
        return self.__nota

    def presentarse(self):  
        #Polimorfismo
        print(f"Soy el alumno {self.nombre} y mi nota es {self.__nota}.")


class Profesor(Persona):
    #subclase Profesor
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        print(f"{self.nombre} enseña {self.materia}.")

    def presentarse(self):  
        #polimorfismo
        print(f"Soy el profesor {self.nombre}, enseño {self.materia}.")


alumno = Alumno("Ana", 16, 8)
profesor = Profesor("Carlos", 40, "Matemáticas")

alumno.estudiar()
profesor.enseñar()
#Llamamos las funciones

for persona in [alumno, profesor]:
    persona.presentarse()
#Poliformismo en metodo presentarse
