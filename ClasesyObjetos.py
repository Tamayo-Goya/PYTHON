class Coche:
#definimos una clase llamada Coche

   
    def __init__(self, marca, modelo, año):     
        self.marca = marca
        self.modelo = modelo
        self.año = año
#guardamos los valores que recibe el constructor en atributos del objeto

    
    def mostrar_datos(self):
#método para mostrar los datos del coche
        
        print(f"Marca: {self.marca}")   
        #mostramos la marca del coche
        
        print(f"Modelo: {self.modelo}") 
        #mostramos el modelo del coche
        
        print(f"Año: {self.año}")       
        #mostramos el año del coche
     

coche1 = Coche("Toyota", "Corolla", 2020) 
coche2 = Coche("Ford", "Mustang", 1969)    
coche3 = Coche("Tesla", "Model 3", 2023)  
#creamos tres objetos (instancias) de la clase Coche


coche1.mostrar_datos() 
coche2.mostrar_datos() 
coche3.mostrar_datos() 
#llamamos al método mostrar_datos para cada objeto
