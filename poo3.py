class VideoGame:
    
    def __init__(self, nome, desenvolvedora, plataforma, genero):
        self.nome = nome
        self.desenvolvedora = desenvolvedora
        self.plataforma = plataforma
        self.genero = genero

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Desenvolvedora: {self.desenvolvedora}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Gênero: {self.genero}")

class Aventura(VideoGame):
    
    def __init__(self, nome, desenvolvedora, plataforma, tipo_aventura):
        super().__init__(nome, desenvolvedora, plataforma, "Aventura")
        self.tipo_aventura = tipo_aventura
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo de Aventura: {self.tipo_aventura}")

class Sandbox(VideoGame):
    
    def __init__(self, nome, desenvolvedora, plataforma, criacao_mundo):
        super().__init__(nome, desenvolvedora, plataforma, "Sandbox")
        self.criacao_mundo = criacao_mundo
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Criacao do Mundo: {self.criacao_mundo}")

class Corrida(VideoGame):
    
    def __init__(self, nome, desenvolvedora, plataforma, tipo_corrida):
        super().__init__(nome, desenvolvedora, plataforma, "Corrida")
        self.tipo_corrida = tipo_corrida
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tipo de Corrida: {self.tipo_corrida}")

jogo1 = Sandbox("Minecraft", "Mojang", "Multiplataforma", "Construção e Exploração")
jogo2 = Aventura("The Legend of Zelda: Breath of the Wild", "Nintendo", "Nintendo Switch", "Mundo Aberto")
jogo3 = Corrida("Forza Horizon 5", "Playground Games", "Xbox", "Simulação")

jogo4 = Aventura("Red Dead Redemption 2", "Rockstar Games", "Multiplataforma", "Mundo Aberto")
jogo5 = Sandbox("Terraria", "Re-Logic", "Multiplataforma", "Construção e Exploração")
jogo6 = Corrida("Gran Turismo 7", "Polyphony Digital", "PS5", "Simulação")
jogo7 = Aventura("Horizon Zero Dawn", "Guerrilla Games", "PS4, PC", "Mundo Aberto")
jogo8 = Sandbox("No Man's Sky", "Hello Games", "Multiplataforma", "Exploração Espacial")
jogo9 = Corrida("Need for Speed Heat", "Ghost Games", "Multiplataforma", "Arcade")

jogo1.exibir_informacoes()
print()  
jogo2.exibir_informacoes()
print()
jogo3.exibir_informacoes()
print()
jogo4.exibir_informacoes()
print()
jogo5.exibir_informacoes()
print()
jogo6.exibir_informacoes()
print()
jogo7.exibir_informacoes()
print()
jogo8.exibir_informacoes()
print()
jogo9.exibir_informacoes()
