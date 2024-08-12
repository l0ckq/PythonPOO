class Caneca:
    formato = "Cilíndrico"

    def __init__(self, nome, marca, capacidade):
        self.nome = nome
        self.marca = marca
        self.capacidade = capacidade

caneca1 = Caneca("Top Caneca", "Stanley", "700mL")
caneca2 = Caneca("Canequinha", "Pacco", "525mL")

class Teclado:
    def __init__(self, mecanismo, marca, bluetooth):
        self.mecanismo = mecanismo
        self.marca = marca
        self.bluetooth = bluetooth

nossoTeclado = Teclado("Membrana", "Logitech", False)
print(nossoTeclado.marca)

teclado1 = Teclado("Mecânico", "Hyperx", True)
print(nossoTeclado.mecanismo)

teclado2 = Teclado("Mecânico", "Dell", False)
print(nossoTeclado.bluetooth)
