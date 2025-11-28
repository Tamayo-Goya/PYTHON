class Coche:
    #definimos la clase Coche

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    #constructor que inicializa los atributos del coche

   
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")   
        #muestra la marca del coche

        print(f"Modelo: {self.modelo}") 
        #muestra el modelo del coche

        print(f"Año: {self.año}")       
        #muestra el año del coche

    #Método para mostrar la información del coche
        
 
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} está arrancando...")
    #Método arrancar: simula que el coche está encendiendo


   
    def detener(self):
        print(f"El coche {self.marca} {self.modelo} se ha detenido.")
    #Método detener: simula que el coche se detiene


coche1 = Coche("Toyota", "Corolla", 2020)
#creamos un objeto de ejemplo

coche1.mostrar_datos()   
#Muestra los datos del coche

coche1.arrancar()        
#Llama al método arrancar

coche1.detener()         
#Llama al método detener
