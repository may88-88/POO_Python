# Programa sencillo de Programación Orientada a Objetos
# Autora: Marilyn Intriago
# Segundo semestre

# -------------------------
# CLASE BASE
# -------------------------
class Dispositivo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print("El dispositivo se está encendiendo")


# -------------------------
# CLASE DERIVADA (HERENCIA)
# -------------------------
class Telefono(Dispositivo):
    def __init__(self, marca, modelo, numero):
        super().__init__(marca)
        self.modelo = modelo
        # Encapsulación
        self.__numero = numero

    def mostrar_numero(self):
        print("Número del teléfono:", self.__numero)

    # Polimorfismo
    def encender(self):
        print("El teléfono", self.marca, self.modelo, "está encendido")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
telefono1 = Telefono("Samsung", "A55", "0988653970")

telefono1.encender()
telefono1.mostrar_numero()
