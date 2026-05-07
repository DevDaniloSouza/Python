class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0
    
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


g1 = Gafanhoto()
g1.nome = "João"
g1.idade = 25
g1.aniversario()  # Incrementa a idade em 1
g1.mensagem()  # Output: Olá, meu nome é João e tenho 26 anos.

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 30
g2.aniversario()  # Incrementa a idade em 1
g2.mensagem()  # Output: Olá, meu nome é Maria e tenho 31 anos.

g3 = Gafanhoto()
g3.mensagem()  # Output: Olá, meu nome é  e tenho 0 anos.
