class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} está comendo")

class Gato(Animal):
    def comer(self):
        print("O gato comeu ração felina!")

garfield = Gato("Garfield", "Laranja")
garfield.comer()


class Cachorro(Animal):

    def __init__(self, nome, cor, raca):
        super().__init__(nome, cor)
        self.raca = raca

ScoobyDoo = Cachorro("Scooby-Doo", "Marrom", "Doberman")
ScoobyDoo.comer()

# Separação #
import time

class Jogos:
    def __init__(self, nome, genero, status):
        self.nome = nome
        self.genero = genero
        self.status = status

    def instalar(self):
        print(f"O {self.nome} está instalando...")
        time.sleep(2)
        print("O jogo instalou com sucesso :)")


class JogosExclusivos(Jogos):
    def __init__(self, nome, genero, status, plataforma):
        super().__init__(nome, genero, status)
        self.plataforma = plataforma

gow = JogosExclusivos("God of War", "RPG e Aventura", "i", "PlayStation")
mine = Jogos("Minecraft", "Sandbox e Aventura", "n")



if mine == "i":
    print("O jogo já está instalado =)")
else:
    print("O jogo não está instalado. Gostaria de instalá-lo? 's' para sim e 'n' para não")
    escolha = input()
    if escolha == "s":
        mine.instalar()
    elif escolha == "n":
        print("Tudo bem. Até a próxima! :D")
    
        




