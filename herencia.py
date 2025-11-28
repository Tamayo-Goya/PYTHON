class Empleado:
    def __init__(self, nombre, salario):
    #constructor que inicializa los atributos comunes a todos los empleados

        self.nombre = nombre      
        #nombre del empleado
        
        self.salario = salario    
        #salario del empleado

    def mostrar_info(self):
    #método para mostrar la información del empleado
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")

class Gerente(Empleado):
    #constructor del Gerente. Usa super() para reutilizar el constructor de Empleado
    def __init__(self, nombre, salario, equipo):
        
        super().__init__(nombre, salario)  
        #llama al constructor de la clase padre
        self.equipo = equipo               
        #nuevo atributo exclusivo de Gerente

    def dirigir(self):
    #nuevo método exclusivo del Gerente
        print(f"El gerente {self.nombre} está dirigiendo al equipo: {self.equipo}")

    def mostrar_info(self):
    #podemos sobrescribir (opcional) el método mostrar_info para añadir más datos
        super().mostrar_info()             
        #llamamos al método original de la clase padre
        print(f"Equipo a cargo: {self.equipo}")


empleado1 = Empleado("Laura", 2500)
#creamos un empleado normal

gerente1 = Gerente("Carlos", 4500, ["Ana", "Luis", "Marta"])
#creamos un gerente

empleado1.mostrar_info()   
#mostramos información

gerente1.mostrar_info()    
#muestra datos básicos

gerente1.dirigir()
#llamamos al método exclusivo del gerente
