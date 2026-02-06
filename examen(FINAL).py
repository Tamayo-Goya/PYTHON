#ej1
class Almacenamiento:
    def __init__(self, espacio_gb):
        
        if espacio_gb < 0:
            self.__espacio_gb = 0
        
        else:
            self.__espacio_gb = espacio_gb

    def obtener_info(self):
        
        return self.__espacio_gb

#ej2
class DispositivoRed:
    def __init__(self, nombre, mac_address):
        self.nombre = nombre
        self.mac_address = mac_address 


class Switch(DispositivoRed):
    
    
    def __init__(self, nombre, mac_address, puertos_totales):
        super().__init__(nombre, mac_address)
        self.puertos_totales = puertos_totales
        self.conexiones_activas = []

    
    
    def conectar_equipo(self, nombre_equipo):
        
        if len(self.conexiones_activas) < self.puertos_totales:
            self.conexiones_activas.append(nombre_equipo)
            print("Equipo", {nombre_equipo}, "conectado correctamente.")
        else:
            print("No hay puertos disponibles para conectar el equipo.")

#ej3
class AuditoriaServidor:
   
   
    def __init__(self, nombre_servidor, capacidad_total, capacidad_usada):
        self.nombre_servidor = nombre_servidor
        self.capacidad_total = capacidad_total
        self.capacidad_usada = capacidad_usada

    
    def porcentaje_uso(self):
        return (self.capacidad_usada / self.capacidad_total) * 100

    
    def alerta(self):
        if self.porcentaje_uso() > 80:
            print("ALERTA: Espacio crítico")
        else:
            print("Estado OK")


servidor = AuditoriaServidor("Servidor_Principal", 1000, 850)
servidor.alerta()

#ej4
class Credencial:
   
    def __init__(self, clave_inicial):
        
   
        if len(clave_inicial) >= 8:
            self.__password = clave_inicial
        else:
            self.__password = "Admin123"

   
    def ver_oculta(self):
      
        return "*" * (len(self.__password) - 2) + self.__password[-2:]


credencial = Credencial("SMR2026")
print(credencial.ver_oculta())



#ej5
class Servicio:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def verificar(self):
        print("Iniciando comprobación genérica...")


class ServicioWeb(Servicio):
    
    def verificar(self):
        print("Haciendo petición HTTP al puerto 80")


class ServicioSSH(Servicio):
    
    def verificar(self):
        print("Comprobando handshake en puerto 22")



servicios = [
    ServicioWeb("Web"),
    ServicioSSH("SSH")
]

for servicio in servicios:
    servicio.verificar()
