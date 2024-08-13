class Caneca:
    formato = "Cilíndrico"
    status = "vazia"

    def __init__(self, nome, marca, capacidade):
        self.nome = nome
        self.marca = marca
        self.capacidade = capacidade

    def encherCaneca(self):
        self.status = "cheia"

    def esvaziarCaneca(self):
        self.status = "vazia"

    def exibirStatusCaneca(self):
        print(f"Sua caneca está {self.status}")

caneca1 = Caneca("Top Caneca", "Stanley", "700mL")
caneca2 = Caneca("Canequinha", "Pacco", "525mL")

caneca1.exibirStatusCaneca()
caneca1.encherCaneca()
caneca1.exibirStatusCaneca()

class Teclado:
    cor = "Preto"

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

print(nossoTeclado.cor)
