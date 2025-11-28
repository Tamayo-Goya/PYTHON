class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial   
    #el constructor inicializa la cuenta con un saldo
    #atributo privado (no accesible directamente desde fuera)

    def obtener_saldo(self):
        return self.__saldo            
        #devuelve el valor del saldo privado
    #getter: método para consultar el saldo

    def depositar(self, cantidad):
    #método para depositar dinero
        if cantidad > 0:               
        #validamos que la cantidad sea positiva
            self.__saldo += cantidad   
        #sumamos al saldo privado
            print(f"Depósito realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
    #método para retirar dinero

        if cantidad <= 0:              
        #Validamos que no sea negativa o cero
        
            print("Error: La cantidad a retirar debe ser positiva.")
        elif cantidad > self.__saldo:  
        #Validamos que haya suficiente saldo
        
            print("Error: Saldo insuficiente para retirar esa cantidad.")
        else:
            self.__saldo -= cantidad   
            #Restamos del atributo privado

            print(f"Retiro realizado. Nuevo saldo: {self.__saldo}")


cuenta = CuentaBancaria(1000)
#creamos una cuenta con saldo inicial de 1000

print("Saldo actual:", cuenta.obtener_saldo())
#consultamos el saldo

cuenta.depositar(500)
#depositamos dinero

cuenta.retirar(300)
#intentamos retirar una cantidad válida

cuenta.retirar(2000)
#intentamos retirar más de lo que hay
